import { 
  VictoryChart,
  VictoryStack,
  VictoryArea,
  VictoryAxis,
  VictoryLegend,
  VictoryTooltip,
  VictoryVoronoiContainer
} from "victory"
import { Grid, GridItem } from "@chakra-ui/react"
import {
  useObjectPathSelector,
} from "redux/selectors.js"
import colors from "theme/colors"

const generateAxis = (data, label) => {
  const axis = []

  data.forEach((obj) => {
    axis.push({
      x: obj.year,
      y: obj.value,
      l: label
    })
  })

  return axis
}

const ClusterSummaryChart = ({ sourceListObjectpath }) => {
  const sourceObj = useObjectPathSelector(
    sourceListObjectpath,
    {}
  );

  if (!sourceObj.data) {
    return <></>
  }

  const lldc = generateAxis(sourceObj.data.LLDC, "LLDC");
  const mdc = generateAxis(sourceObj.data.MDC, "MDC");
  const aofp = generateAxis(sourceObj.data.AOFP, "Non-differential");

  return (
      <Grid minW="100%">
        <GridItem>
          <VictoryChart
            height={150}
            padding={{ left: 60, right: 20, bottom: 30, top: 10 }}
            containerComponent={
              <VictoryVoronoiContainer voronoiDimension="x"
                labels={({ datum }) => `${datum.l}: ${datum.y.toFixed(2)} Gt CO2-eq`}
                labelComponent={
                  <VictoryTooltip
                    center={{ x: 225, y: 30 }}
                    style={{fontSize: '6px'}}
                    cornerRadius={1}
                    flyoutStyle={{
                      fill: "white",
                      strokeWidth: 0.5
                    }}
                  />
                }
              />
            }
            >
            <VictoryAxis
              tickFormat={(v) => v.toString()}
              style={{
                axis: { stroke: "#f2f2f2" },
                tickLabels: {
                  fontSize: 2,
                  fill: "#a3a3a3"
                },
                ticks: { stroke: "#bababa", size: 2, verticalAnchor: "middle" },
                grid: { stroke: "#f2f2f2", strokeWidth: 0.5 }
              }}
            />
            <VictoryAxis
              dependentAxis
              style={{
                axisLabel: {fontSize: 8, padding: 40, fill: "#bababa"},
                axis: { stroke: "#f2f2f2" },
                tickLabels: {
                  fill: "#a3a3a3",
                  fontSize: 8
                },
                ticks: { stroke: "#bababa", size: 2, verticalAnchor: "middle" },
                grid: { stroke: "#f2f2f2", strokeWidth: 0.5 }
              }}
              label="Culmulative Gt CO2-eq"
              fixLabelOverlap={true}
            />
            <VictoryStack>
              <VictoryArea
                data={lldc}
                style={{ data: { fill: colors.brand.health[700] } }}
                interpolation="natural"
              />

              <VictoryArea
                data={mdc}
                style={{ data: { fill: colors.brand.health[500] } }}
                interpolation="natural"
              />

              <VictoryArea
                data={aofp}
                style={{ data: { fill: colors.brand.health[300] } }}
                interpolation="natural"
              />
            </VictoryStack>
            
          </VictoryChart>
        </GridItem>
        <GridItem>
          <VictoryLegend
            x={125} y={5}
            orientation="horizontal"
            height={25}
            style={{ labels: {fontSize: 4 } }}
            data={[
              { name: "Least & Less Developed Countries", symbol: { fill: colors.brand.health[700] } },
              { name: "More Developed Countries", symbol: { fill: colors.brand.health[500] } },
              { name: "Non-differential", symbol: { fill: colors.brand.health[300] } },
            ]}/>
        </GridItem>
      </Grid>
  )
}

export default ClusterSummaryChart