<!-- multipleChart : 최소값, 평균값, 최대값 3개의 value로 시세를 확인하는 차트입니다. -->
<!-- date, 최소값,최대값,평균값에 대한 각각 date에 맞는 데이터가 필요합니다. -->
<template>
    <div id="chartdiv" style="width:1200px"></div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

am4core.useTheme(am4themes_animated);


export default {
    name: 'logChart',
    props :{ 
    chartDatas : { type: Object},
    },
    data: () => ({
        chartDatasList : {}
    }),
    mounted() {
        var chartDatasLists = this.chartDatas['group_by_date']['buckets']
        am4core.ready(function() {

        // Themes begin
        am4core.useTheme(am4themes_animated);
        // Themes end

        // Create chart instance
        var chart = am4core.create("chartdiv", am4charts.XYChart);

        // Increase contrast by taking evey second color
        chart.colors.step = 2;

        // Add data
        chart.data = generateChartData(chartDatasLists);

        // Create axes
        var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
        dateAxis.renderer.minGridDistance = 50;

        // Create series
        function createAxisAndSeries(field, name, opposite, bullet) {
        var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
        
        var series = chart.series.push(new am4charts.LineSeries());
        series.dataFields.valueY = field;
        series.dataFields.dateX = "date";
        series.strokeWidth = 2;
        series.yAxis = valueAxis;
        series.name = name;
        series.tooltipText = "{name}: [bold]{valueY}[/]";
        series.tensionX = 0.8;
        
        var interfaceColors = new am4core.InterfaceColorSet();
        
        switch(bullet) {
            case "triangle":
            var bullet = series.bullets.push(new am4charts.Bullet());
            bullet.width = 12;
            bullet.height = 12;
            bullet.horizontalCenter = "middle";
            bullet.verticalCenter = "middle";
            
            var triangle = bullet.createChild(am4core.Triangle);
            triangle.stroke = interfaceColors.getFor("background");
            triangle.strokeWidth = 2;
            triangle.direction = "top";
            triangle.width = 12;
            triangle.height = 12;
            break;
            case "rectangle":
            var bullet = series.bullets.push(new am4charts.Bullet());
            bullet.width = 10;
            bullet.height = 10;
            bullet.horizontalCenter = "middle";
            bullet.verticalCenter = "middle";
            
            var rectangle = bullet.createChild(am4core.Rectangle);
            rectangle.stroke = interfaceColors.getFor("background");
            rectangle.strokeWidth = 2;
            rectangle.width = 10;
            rectangle.height = 10;
            break;
            default:
            var bullet = series.bullets.push(new am4charts.CircleBullet());
            bullet.circle.stroke = interfaceColors.getFor("background");
            bullet.circle.strokeWidth = 2;
            break;
        }
        
        valueAxis.renderer.line.strokeOpacity = 1;
        valueAxis.renderer.line.strokeWidth = 2;
        valueAxis.renderer.line.stroke = series.stroke;
        valueAxis.renderer.labels.template.fill = series.stroke;
        valueAxis.renderer.opposite = opposite;
        valueAxis.renderer.grid.template.disabled = true;
        }

        createAxisAndSeries("visits", "평균가", false, "circle");
        createAxisAndSeries("views", "최저가", true, "triangle");
        createAxisAndSeries("hits", "최고가", true, "rectangle");

        // Add legend
        chart.legend = new am4charts.Legend();

        // Add cursor
        chart.cursor = new am4charts.XYCursor();

        // generate some random data, quite different range
        function generateChartData(chartDatasLists) {
        var chartData = [];

        var visits = 0;
        var hits = 0;
        var views = 0;
        for (var idx in chartDatasLists) {
            // we create date objects here. In your data, you can have date strings
            // and then set format of your dates using chart.dataDateFormat property,
            // however when possible, use date objects, as this will speed up chart rendering.
            
            var newDate = chartDatasLists[idx]['key_as_string']
            visits = chartDatasLists[idx]['date_avg']['value']
            hits = chartDatasLists[idx]['date_max']['value']
            views = chartDatasLists[idx]['date_min']['value']
            

            chartData.push({
            date: newDate,
            visits: visits,
            hits: hits,
            views: views
            });
        }
        return chartData;
        }
        });
    }
}
</script>
<style>
#chartdiv {
  width: 100%;
  height: 500px;
}

</style>