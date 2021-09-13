varProjectionNamesPaths = [
  ["name", "technologies.solarpvutil.name", "", "", ""],
  ["vmas", "technologies.solarpvutil.vmas", "", "", ""],
  ["description", "technologies.solarpvutil.description", "", "", ""],
  ["emissions_use_co2eq", "technologies.solarpvutil.emissions_use_co2eq", "", "", ""],
  ["pds_source_post_2014", "technologies.solarpvutil.pds_source_post_2014", "", "", ""],
  ["conv_2014_cost","technologies.fossilfuelelectricity.start_year_cost","start_year_cost","First Cost per Implementation Unit","dollars"],
  ["conv_first_cost_efficiency_rate","technologies.fossilfuelelectricity.first_cost_efficiency_rate","first_cost_efficiency_rate","First Cost Efficiency Rate","float"],
  ["conv_fixed_oper_cost_per_iunit","technologies.fossilfuelelectricity.fixed_oper_cost_per_iunit","fixed_oper_cost_per_iunit","Operating Cost per Functional Unit per Annum","dollars"],
  ["conv_fuel_cost_per_funit","technologies.fossilfuelelectricity.fuel_cost_per_funit","fuel_cost_per_funit","Fuel Cost per Functional Unit","dollars"],
  ["conv_lifetime_capacity","technologies.fossilfuelelectricity.lifetime_capacity","lifetime_capacity","Lifetime Capacity","float"],
  ["conv_var_oper_cost_per_funit","technologies.fossilfuelelectricity.var_oper_cost_per_funit","var_oper_cost_per_funit","Variable Operating Cost (VOM) per Functional Unit","dollars"],
  ["conv_emissions_per_funit","technologies.fossilfuelelectricity.emissions_per_funit","emissions_per_funit","Direct Emissions per Functional Unit","float"],
  ["conv_fuel_consumed_per_funit","technologies.fossilfuelelectricity.fuel_consumed_per_funit","fuel_consumed_per_funit","Fuel Consumed per Functional Unit","float"],
  ["conv_fuel_emissions_factor","technologies.fossilfuelelectricity.fuel_emissions_factor","fuel_emissions_factor","Fuel Emissions Factor","float"],
  ["conv_indirect_co2_is_iunits","technologies.fossilfuelelectricity.indirect_co2_is_iunits","indirect_co2_is_iunits","Implementation or Functional Units?","enum(Implementation,Functional)"],
  ["conv_indirect_co2_per_unit","technologies.fossilfuelelectricity.indirect_co2_per_unit","indirect_co2_per_unit","Indirect CO2 Emissions per Unit","float"],
  ["conv_annual_energy_used","technologies.fossilfuelelectricity.annual_energy_used","annual_energy_used","Total Energy Used per Functional Unit'","float"],
  ["conv_avg_annual_use","technologies.fossilfuelelectricity.avg_annual_use","avg_annual_use","Average Annual Use","float"],
  ["pds_adoption_final_percentage","technologies.solarpvutil.adoption_final_percentage","final_percentage","Final Adoption Percentage [TODO: Finalize Name]","percent"],
  ["soln_pds_adoption_basis","technologies.solarpvutil.adoption_basis","basis","Adoption Basis","enum(DEFAULT,DEFAULT_LINEAR,...)"],
  ["soln_pds_adoption_prognostication_growth","technologies.solarpvutil.adoption_prognostication_growth","prognostication_growth","Prognostication Growth","enum(low,medium,high)"],
  ["soln_pds_adoption_prognostication_source","technologies.solarpvutil.adoption_prognostication_source","prognostication_source","Prognostication Source","reference"],
  ["soln_pds_adoption_prognostication_trend","technologies.solarpvutil.adoption_prognostication_trend","prognostication_trend","Prognostication Trend","enum(linear,2nd poly,3rd poly,exp)"],
  ["soln_pds_adoption_regional_data","technologies.solarpvutil.adoption_regional_data","regional_data","Regional Data","reference"],
  ["soln_pds_adoption_custom_name","technologies.solarpvutil.adoption_custom_name","custom_name","Adoption Name","reference-string"],
  ["solution_category","technologies.solarpvutil.solution_category","solution_category","Category","string"],
  ["ch4_co2_per_funit","technologies.solarpvutil.ch4_co2_per_funit","ch4_co2_per_funit","CH4-CO2eq Tons Reduced","float"],
  ["ch4_is_co2eq","technologies.solarpvutil.ch4_is_co2eq","ch4_is_co2eq","CH4-CO2eq Tons Reduced: Based on CO2eq?","boolean"],
  ["n2o_co2_per_funit","technologies.solarpvutil.n2o_co2_per_funit","n2o_co2_per_funit","N2O-CO2eq Tons Reduced","float"],
  ["n2o_is_co2eq","technologies.solarpvutil.n2o_is_co2eq","n2o_is_co2eq","N20-CO2eq Tons Reduced: Based on CO2eq?","boolean"],
  ["soln_emissions_per_funit","technologies.solarpvutil.emissions_per_funit","emissions_per_funit","Direct Emissions per Functional Unit","float"],
  ["soln_energy_efficiency_factor","technologies.solarpvutil.energy_efficiency_factor","energy_efficiency_factor","Energy Efficiency Factor","float"],
  ["soln_fuel_efficiency_factor","technologies.solarpvutil.fuel_efficiency_factor","fuel_efficiency_factor","Fuel Cost Learning Rate","float"],
  ["soln_fuel_emissions_factor","technologies.solarpvutil.fuel_emissions_factor","fuel_emissions_factor","Direct Fuel Emissions per Functional Unit","float"],
  ["soln_indirect_co2_per_iunit","technologies.solarpvutil.indirect_co2_per_iunit","indirect_co2_per_iunit","Indirect CO2 Emissions per Unit","float"],
  ["co2eq_conversion_source","technologies.solarpvutil.co2eq_conversion_source","co2eq_conversion_source","CH4-CO2eq Tons Reduced: Conversion Source","enum(AR5 with feedback, AR4, SAR)"],
  ["npv_discount_rate","technologies.solarpvutil.npv_discount_rate","npv_discount_rate","NPV Discount Rate","float"],
  ["pds_2014_cost","technologies.solarpvutil.start_year_cost","start_year_cost","","currency"],
  ["soln_first_cost_below_conv","technologies.solarpvutil.first_cost_below_conv","first_cost_below_conv","Allow solution First Cost to go Below Conventional?","boolean"],
  ["soln_first_cost_efficiency_rate","technologies.solarpvutil.first_cost_efficiency_rate","first_cost_efficiency_rate","First Cost Learning Rate","float"],
  ["soln_fixed_oper_cost_per_iunit","technologies.solarpvutil.fixed_oper_cost_per_iunit","fixed_oper_cost_per_iunit","Operating Cost per Functional Unit per Annum","currency"],
  ["soln_fuel_cost_per_funit","technologies.solarpvutil.fuel_cost_per_funit","fuel_cost_per_funit","Fuel Cost (functional units)","currency"],
  ["soln_lifetime_capacity","technologies.solarpvutil.lifetime_capacity","lifetime_capacity","Lifetime Capacity","float"],
  ["soln_var_oper_cost_per_funit","technologies.solarpvutil.var_oper_cost_per_funit","var_oper_cost_per_funit","Variable Operating Cost (VOM) per Functional Unit","currency"],
  ["emissions_grid_range","technologies.solarpvutil.grid_range","grid_range","REF Case Grid Emission Factors - Range",""],
  ["emissions_grid_source","technologies.solarpvutil.grid_source","grid_source","REF Case Grid Emission Factors - Source","reference"],
  # ["report_end_year","technologies.solarpvutil.report_end_year","report_end_year","End Year","year"],
  # ["report_start_year","technologies.solarpvutil.report_start_year","report_start_year","Start Year","year"],
  ["report_end_year","report_end_year","report_end_year","End Year","year"],
  ["report_start_year","report_start_year","report_start_year","Start Year","year"],
  ["soln_annual_energy_used","technologies.solarpvutil.annual_energy_used","annual_energy_used","Total Energy Used per Functional Unit","float"],
  ["soln_avg_annual_use","technologies.solarpvutil.avg_annual_use","avg_annual_use","Average Annual Use","float"],
  ["pds_adoption_use_ref_years","technologies.solarpvutil.adoption_use_ref_years","use_ref_years","Years for which the Helpertables PDS adoption for 'World' should use the REF adoption values","int"],
  ["pds_base_adoption","technologies.solarpvutil.adoption_base_adoption","base_adoption","Base Adoption [PDS]","float"],
  ["source_until_2014","categories.electricity_generation.source_until_start_year","source_until_start_year","CURRENT Market","reference"],
  ["source_after_2014","categories.electricity_generation.tam_source_after_start_year","source_after_start_year","2020 - 2050 REF Market","regionalize_referencs(tam_sources OR tam_source_groups)"],
  ["trend","categories.electricity_generation.tam_trend","trend","","regionalize_enum(linear, 2nd poly, 3rd poly, exp)"],
  ["growth","categories.electricity_generation.tam_growth","growth","","regionalize_enum(low,medium,high)"],
  ["low_sd_mult","categories.electricity_generation.tam_low_sd_mult","low_sd_mult","","regionalize_float"],
  ["high_sd_mult","categories.electricity_generation.tam_high_sd_mult","high_sd_mult","","regionalize_float"],

  # Custom uploaded source
  ["pds_tam_custom_source","categories.electricity_generation.pds_tam_custom_source","pds_tam_custom_source","",""],
  ["pds_adoption_custom_source","categories.solarpvutil.pds_adoption_custom_source","pds_adoption_custom_source","",""],

  #land
  ["use_custom_tla","technologies.solarpvutil.use_custom_tla","use_custom_tla","","boolean"],
  ["custom_tla_fixed_value","technologies.solarpvutil.custom_tla_fixed_value","custom_tla_fixed_value","","float"],
  ["conv_expected_lifetime","technologies.fossilfuelelectricity.expected_lifetime","expected_lifetime","","float"],
  ["yield_from_conv_practice","technologies.fossilfuelelectricity.yield","yield","","float"],
  ["soln_expected_lifetime","technologies.solarpvutil.expected_lifetime","expected_lifetime","","float"],
  ["yield_gain_from_conv_to_soln","technologies.solarpvutil.yield_gain","yield_gain","","float"],
  ["emissions_use_agg_co2eq","technologies.solarpvutil.emissions_use_agg_co2eq","emissions_use_agg_co2eq","",""],
  ["emissions_use_agg_co2eq","technologies.solarpvutil.emissions_use_agg_co2eq","emissions_use_agg_co2eq","",""],
  ["tco2eq_reduced_per_land_unit","technologies.solarpvutil.tco2eq_reduced_per_land_unit","tco2eq_reduced_per_land_unit","",""],
  ["tco2eq_rplu_rate","technologies.solarpvutil.tco2eq_rplu_rate","tco2eq_rplu_rate","",""],
  ["tco2_reduced_per_land_unit","technologies.solarpvutil.tco2_reduced_per_land_unit","tco2_reduced_per_land_unit","",""],
  ["tco2_rplu_rate","technologies.solarpvutil.tco2_rplu_rate","tco2_rplu_rate","",""],
  ["tn2o_co2_reduced_per_land_unit","technologies.solarpvutil.tn2o_co2_reduced_per_land_unit","tn2o_co2_reduced_per_land_unit","",""],
  ["tn2o_co2_rplu_rate","technologies.solarpvutil.tn2o_co2_rplu_rate","tn2o_co2_rplu_rate","",""],
  ["tch4_co2_reduced_per_land_unit","technologies.solarpvutil.tch4_co2_reduced_per_land_unit","tch4_co2_reduced_per_land_unit","","float"],
  ["tch4_co2_rplu_rate","technologies.solarpvutil.tch4_co2_rplu_rate","tch4_co2_rplu_rate","",""],
  ["land_annual_emissons_lifetime","technologies.solarpvutil.land_annual_emissons_lifetime","land_annual_emissons_lifetime","","float"],
  ["seq_rate_global","technologies.solarpvutil.seq_rate_global","seq_rate_global","","float"],
  ["carbon_not_emitted_after_harvesting","technologies.solarpvutil.carbon_not_emitted_after_harvesting","carbon_not_emitted_after_harvesting","","float"],
  ["disturbance_rate","technologies.solarpvutil.disturbance_rate","disturbance_rate","","float"],
  ["harvest_frequency","technologies.solarpvutil.harvest_frequency","harvest_frequency","","float"],
  ["global_multi_for_regrowth","technologies.solarpvutil.global_multi_for_regrowth","global_multi_for_regrowth","","float"],
  ["degradation_rate","technologies.solarpvutil.degradation_rate","degradation_rate","","float"],
  ["tC_storage_in_protected_land_type","technologies.solarpvutil.tC_storage_in_protected_land_type","tC_storage_in_protected_land_type","","float"],
  ["delay_protection_1yr","technologies.solarpvutil.delay_protection_1yr","delay_protection_1yr","","boolean"],
  ["delay_regrowth_1yr","technologies.solarpvutil.delay_regrowth_1yr","delay_regrowth_1yr","","boolean"],
  ["include_unprotected_land_in_regrowth_calcs","technologies.solarpvutil.include_unprotected_land_in_regrowth_calcs","include_unprotected_land_in_regrowth_calcs","","boolean"],
  ["direct_emissions_saved_land","technologies.solarpvutil.direct_emissions_saved_land","direct_emissions_saved_land","",""],

  #food
  ["soln_ref_adoption_basis","technologies.solarpvutil.soln_ref_adoption_basis","soln_ref_adoption_basis","","reference_string"],
  ["soln_ref_adoption_custom_name","technologies.solarpvutil.soln_ref_adoption_custom_name","soln_ref_adoption_custom_name","","reference_string"],
  ["soln_ref_adoption_regional_data","technologies.solarpvutil.soln_ref_adoption_regional_data","soln_ref_adoption_regional_data","","boolean"],

  #buildings and cities
]
