var dashboard = {
    stars: function() {
        this.carga()
    },
    carga() {
        Highcharts.chart({
            chart: {
              renderTo: 'container',
              type: 'column',
              options3d: {
                enabled: true,
                alpha: 15,
                beta: 15,
                depth: 50,
                viewDistance: 25
              }
            },
            title: {
              text: 'Comportamiento de ventas semanal'
            },
            subtitle: {
              text: 'Este es el comportamiento de las ventas de peipert'
            },
            xAxis: {
              categories: ['Lunes', 'Martes', 'Miercoles']
            },
            credits:{
                enabled: false
            },
            plotOptions: {
              column: {
                depth: 25
              }
            },
            series: [{
              name:'Ventas',
              data: [0, 2, 15]
            }]
        });
        Highcharts.chart({
            chart: {
              renderTo: 'container2',
              type: 'column',
              options3d: {
                enabled: true,
                alpha: 15,
                beta: 15,
                depth: 50,
                viewDistance: 25
              }
            },
            title: {
              text: 'Comportamiento de visitantes'
            },
            subtitle: {
              text: 'Este es el comportamiento de las visitas en el ultimo año'
            },
            xAxis: {
              categories: ['Enero', 'Febrero', 'Marzo']
            },
            credits:{
                enabled: false
            },
            plotOptions: {
              column: {
                depth: 25
              }
            },
            series: [{
              name:'Visitantes',
              data: [150, 250, 500]
            }]
        });
        Highcharts.chart({
            chart: {
              renderTo: 'container3',
              type: 'column',
              options3d: {
                enabled: true,
                alpha: 15,
                beta: 15,
                depth: 50,
                viewDistance: 25
              }
            },
            title: {
              text: 'Comportamiento de visitantes'
            },
            subtitle: {
              text: 'Este es el comportamiento de las visitas en el ultimo año'
            },
            xAxis: {
              categories: ['Enero', 'Febrero', 'Marzo']
            },
            credits:{
                enabled: false
            },
            plotOptions: {
              column: {
                depth: 25
              }
            },
            series: [{
              name:'Visitantes',
              data: [150, 250, 500]
            }]
        });
        Highcharts.chart('container1', {
            chart: {
              type: 'column'
            },
            title: {
              text: 'Browser market shares. January, 2018'
            },
            subtitle: {
              text: 'Click the columns to view versions. Source: <a href="http://statcounter.com" target="_blank">statcounter.com</a>'
            },
            accessibility: {
              announceNewData: {
                enabled: true
              }
            },
            xAxis: {
              type: 'category'
            },
            yAxis: {
              title: {
                text: 'Total percent market share'
              }
  
            },
            legend: {
              enabled: false
            },
            plotOptions: {
              series: {
                borderWidth: 0,
                dataLabels: {
                  enabled: true,
                  format: '{point.y:.1f}%'
                }
              }
            },
  
            tooltip: {
              headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
              pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
            },
  
            series: [
              {
                name: "Browsers",
                colorByPoint: true,
                data: [
                  {
                    name: "Chrome",
                    y: 62.74,
                    drilldown: "Chrome"
                  },
                  {
                    name: "Firefox",
                    y: 10.57,
                    drilldown: "Firefox"
                  },
                  {
                    name: "Internet Explorer",
                    y: 7.23,
                    drilldown: "Internet Explorer"
                  },
                  {
                    name: "Safari",
                    y: 5.58,
                    drilldown: "Safari"
                  },
                  {
                    name: "Edge",
                    y: 4.02,
                    drilldown: "Edge"
                  },
                  {
                    name: "Opera",
                    y: 1.92,
                    drilldown: "Opera"
                  },
                  {
                    name: "Other",
                    y: 7.62,
                    drilldown: null
                  }
                ]
              }
            ],
            drilldown: {
              series: [
                {
                  name: "Chrome",
                  id: "Chrome",
                  data: [
                    [
                      "v65.0",
                      0.1
                    ],
                    [
                      "v64.0",
                      1.3
                    ],
                    [
                      "v63.0",
                      53.02
                    ],
                    [
                      "v62.0",
                      1.4
                    ],
                    [
                      "v61.0",
                      0.88
                    ],
                    [
                      "v60.0",
                      0.56
                    ],
                    [
                      "v59.0",
                      0.45
                    ],
                    [
                      "v58.0",
                      0.49
                    ],
                    [
                      "v57.0",
                      0.32
                    ],
                    [
                      "v56.0",
                      0.29
                    ],
                    [
                      "v55.0",
                      0.79
                    ],
                    [
                      "v54.0",
                      0.18
                    ],
                    [
                      "v51.0",
                      0.13
                    ],
                    [
                      "v49.0",
                      2.16
                    ],
                    [
                      "v48.0",
                      0.13
                    ],
                    [
                      "v47.0",
                      0.11
                    ],
                    [
                      "v43.0",
                      0.17
                    ],
                    [
                      "v29.0",
                      0.26
                    ]
                  ]
                },
                {
                  name: "Firefox",
                  id: "Firefox",
                  data: [
                    [
                      "v58.0",
                      1.02
                    ],
                    [
                      "v57.0",
                      7.36
                    ],
                    [
                      "v56.0",
                      0.35
                    ],
                    [
                      "v55.0",
                      0.11
                    ],
                    [
                      "v54.0",
                      0.1
                    ],
                    [
                      "v52.0",
                      0.95
                    ],
                    [
                      "v51.0",
                      0.15
                    ],
                    [
                      "v50.0",
                      0.1
                    ],
                    [
                      "v48.0",
                      0.31
                    ],
                    [
                      "v47.0",
                      0.12
                    ]
                  ]
                },
                {
                  name: "Internet Explorer",
                  id: "Internet Explorer",
                  data: [
                    [
                      "v11.0",
                      6.2
                    ],
                    [
                      "v10.0",
                      0.29
                    ],
                    [
                      "v9.0",
                      0.27
                    ],
                    [
                      "v8.0",
                      0.47
                    ]
                  ]
                },
                {
                  name: "Safari",
                  id: "Safari",
                  data: [
                    [
                      "v11.0",
                      3.39
                    ],
                    [
                      "v10.1",
                      0.96
                    ],
                    [
                      "v10.0",
                      0.36
                    ],
                    [
                      "v9.1",
                      0.54
                    ],
                    [
                      "v9.0",
                      0.13
                    ],
                    [
                      "v5.1",
                      0.2
                    ]
                  ]
                },
                {
                  name: "Edge",
                  id: "Edge",
                  data: [
                    [
                      "v16",
                      2.6
                    ],
                    [
                      "v15",
                      0.92
                    ],
                    [
                      "v14",
                      0.4
                    ],
                    [
                      "v13",
                      0.1
                    ]
                  ]
                },
                {
                  name: "Opera",
                  id: "Opera",
                  data: [
                    [
                      "v50.0",
                      0.96
                    ],
                    [
                      "v49.0",
                      0.82
                    ],
                    [
                      "v12.1",
                      0.14
                    ]
                  ]
                }
              ]
            }
        });  
        dashboard.asiVamos();
    },
    asiVamos: function() {
      
      $.ajax({
        url: 'asiVamos',
        type: 'GET',
        dataType: 'json'
      })
      .done(function(data) {
        console.log(data);
        Highcharts.chart({
          chart: {
            renderTo: 'container2',
            type: 'column',
            options3d: {
              enabled: true,
              alpha: 15,
              beta: 15,
              depth: 50,
              viewDistance: 25
            }
          },
          title: {
            text: 'Comportamiento de registros'
          },
          subtitle: {
            text: 'Este es el comportamiento de los registros en landing'
          },
          xAxis: {
            categories: data[0]
          },
          credits:{
              enabled: false
          },
          plotOptions: {
            column: {
              depth: 25
            }
          },
          series: [{
            name:'Registros',
            data: data[1]
          }]
        });
      });
      Highcharts.chart('container3', {
        chart: {
          type: 'line'
        },
        title: {
          text: 'Monthly Average Temperature'
        },
        subtitle: {
          text: 'Source: WorldClimate.com'
        },
        xAxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        yAxis: {
          title: {
            text: 'Temperature (°C)'
          }
        },
        plotOptions: {
          line: {
            dataLabels: {
              enabled: true
            },
            enableMouseTracking: false
          }
        },
        series: [{
          name: 'Tokyo',
          data: [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }, {
          name: 'London',
          data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
        }]
      });
    },
};
dashboard.stars();
