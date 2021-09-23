"""
	Route mapping for the VMA API
"""
import importlib
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from model.vma2 import VMA
from model.advanced_controls import get_vma_for_param
from api.config import get_settings, get_db
from api.transforms.variable_paths import varProjectionNamesPaths
from api.transforms.reference_variable_paths import varRefNamesPaths
from api.routers.auth import get_current_active_user
from api.queries.resource_queries import (
  get_entity_by_name,
  publish_entity
)
from api.db import models

settings = get_settings()
router = APIRouter()
default_provider = settings.default_provider

@router.get("/vma/mappings/{technology}",
        summary="Get VMA mappings for a given technology",
        tags=["VMA"]
        )
async def get_vma_mappings(technology: str, db: Session = Depends(get_db)):
  paths = varProjectionNamesPaths + varRefNamesPaths
  importname = 'solution.' + technology
  m = importlib.import_module(importname)
  result = []
  for path in paths:
    vma_titles = get_vma_for_param(path[0])
    for title in vma_titles:
      vma_file = m.VMAs.get(title)
      if vma_file and vma_file.filename:
        db_file = get_entity_by_name(db, vma_file.filename.name, technology, models.VMA)
        if db_file:
          result.append({
            'var': path[0],
            'vma_title': title,
            'vma_filename': vma_file.filename.name,
            'path': db_file.path,
            'file': db_file,
          })
  return result

@router.get("/vma_csv/{id}",
        summary="Retrieve a VMA CSV with the given id",
        tags=["VMA"]
        )
async def get_vma_csv(id: str, db: Session = Depends(get_db)):
  return db.query(models.VMA_CSV).get(id)

@router.post("/vma_csv",
        summary="Upload a custom VMA CSV",
        tags=["VMA"]
        )
async def post_vma_csv(
  name: str = Form(...),
  technology: str = Form(...),
  variable: str = Form(...),
  data: UploadFile = File(...),
  db_active_user: models.User = Depends(get_current_active_user),
  db: Session = Depends(get_db)):
  vma_csv = models.VMA_CSV(
    data = data.file.read(),
    author = db_active_user,
    name = name,
    technology = technology,
    variable = variable
  )
  db.add(vma_csv)
  db.commit()
  db.refresh(vma_csv)
  return vma_csv

@router.put('/vma_csv/{input_id}/publish',
  summary='publish VMA CSV to be public',
  description='publishing VMA CSV to be public, if public, the VMA CSV ' +
    'are then accessable for other users',
    tags=["VMA"])
async def publish_vma_by_id(input_id: int, database: Session = Depends(get_db),
  db_active_user: models.User = Depends(get_current_active_user)):
  """
    Make VMA CSV publically accessable

    Parameters:
    ----
    input_id: int
      VMA CSV id
    database: Session
      current DB session
    db_active_user: User
      logged in user
  """
  try:
    return publish_entity(database, models.VMA_CSV, input_id, db_active_user, True)
  except NoResultFound:
    raise HTTPException(status_code=404, detail="VMA CSV not found")

@router.delete('/vma_csv/{input_id}/publish',
  summary='unpublish VMA CSV to make it private',
  description='unpublish a VMA CSV to private and make it accessable only to author',
  tags=["VMA"])
async def unpublish_vma_by_id(input_id: int, database: Session = Depends(get_db),
  db_active_user: models.User = Depends(get_current_active_user)):
  """
    Make VMA CSV private

    Parameters:
    ----
    input_id: int
      VMA CSV id
    database: Session
      current DB session
    db_active_user: User
      logged in user
  """
  try:
    return publish_entity(database, models.VMA_CSV, input_id, db_active_user, False)
  except NoResultFound:
    raise HTTPException(status_code=404, detail="VMA CSV not found")
  
@router.get("/vma/calculation",
        summary="Get VMA calculation",
        description="For a given variable, calculate the VMA values from the corresponding CSVs. " +
        "This will return low, mean, and high values for the variable, as well as the source name and path",
        tags=["VMA"]
        )
async def calculate_vma_groupings(
  variable: str,
  stat_correction: bool,
  use_weight: bool,
  db: Session = Depends(get_db)):

  vma_csvs = db.query(models.VMA_CSV).filter(
    models.VMA_CSV.variable == variable
  ).all()
  results = []
  for csv in vma_csvs:
    vma = VMA(csv.data, stat_correction=stat_correction, use_weight=use_weight)
    [mean, high, low] = vma.avg_high_low()
    results.append({
      'path': csv.path,
      'source': csv.name,
      'mean': mean,
      'high': high,
      'low': low
    })
  return results
