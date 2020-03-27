// REQUEST THE DATA
const url5 = "/TNDeptHealth_counties";
d3.json(url5).then(function(data) {
  console.log(data);
    let county_values = Object.values(data["Cases"])
        console.log(county_values)
    let county_names = Object.values(data["County"])
        console.log(county_names)
    
        var trace1 = {
            x: county_names,
            y: county_values,
            mode: 'bar',
            opacity : .7,
            type: 'bar',
            name: 'Counties',
            text: county_names,
            marker: { color : 'Cornflower Blue',
              size: 12,
              line: {
                color: 'MediumPurple',
                width: 1
            }
           }
          };
        
          
          var data = [ trace1 ];
          
          var layout = {
            title: 'TN Counties and Coronavirus Cases',
            xaxis: {
              tickmode: 'auto'
            },
            yaxis: {
              title: 'Cases'
            },
          };
          
        
        Plotly.newPlot('histogram', data, layout);
        });

const url = "/TNDeptHealth_overall";
d3.json(url).then(function(data) {
  console.log(data);
    let facility = Object.values(data["Laboratory Type"])
        console.log(facility)
    let positive = Object.values(data["Positive Test"])
        console.log(positive)
    let negative = Object.values(data["Negative Tests"])
        console.log(negative)
    let total = Object.values(data["Total"])
        console.log(total)
        var trace1 = {
            x: facility,
            y: total,

            opacity : .7,
            type: 'scatter',
            name: 'Tested',
            text: positive,
            marker: { color : 'Red',
              size: 12,
              line: {
                color: 'MediumPurple',
                width: 1
            }
           }
          };
          var trace2 = {
            x: facility,
            y: negative,
            yaxis: 'y2',
            opacity : .4,
            type: 'bar',
            name: 'negative',
            marker: { color : 'green',
              size: 2,
              line: {
                color: 'MediumPurple',
                width: 2
              }
              }
          };
          var trace3 = {
            x: facility,
            y: positive,
            yaxis: 'y2',
            opacity : .4,
            type: 'bar',
            name: 'positive',
            marker: { color : 'blue',
              size: 2,
              line: {
                color: 'MediumPurple',
                width: 2
              }
              }
          };
          
          var data = [ trace1,trace2,trace3 ];
          
          var layout = {
            title: 'Testing Data',
            xaxis: {
              tickmode: 'auto'
            },
            yaxis: {
              title: 'Testing Data'
            },
            yaxis2:{
              title: 'Negative Tests',
              titlefont: {color: 'rgb(148, 103, 189)'},
              tickfont: {color: 'rgb(148, 103, 189)'},
              overlaying: 'y',
              side: 'right'
            },
            yaxis3:{
                title: 'Negative Tests',
                titlefont: {color: 'rgb(108, 115, 129)'},
                tickfont: {color: 'rgb(108, 115, 129)'},
                overlaying: 'y',
                side: 'right'
              }
          };
          
        
        Plotly.newPlot('one_song', data, layout);
        });

const url2 = "/TNDeptHealth_age";
d3.json(url2).then(function(data) {
  console.log(data);
    let age_groups = Object.values(data["Age Ranges of Confirmed Cases"])
        console.log(age_groups)
    let age_cases = Object.values(data["Number_Cases"])
        console.log(age_cases)


  var trace1 = {
    x: age_groups,
    y: age_cases,
    mode: 'bar',
    opacity : .7,
    type: 'bar',
    name: 'age_groups',
    text: age_groups,
    marker: { color : 'Blue',
      size: 12,
      line: {
        color: 'MediumPurple',
        width: 1
    }
   }
  };

  
  var data = [ trace1 ];
  
  var layout = {
    title: 'TN Age Groups and Coronavirus Cases',
    xaxis: {
      title: 'Age Groups',
      tickmode: 'auto'
    },
    yaxis: {
      title: 'Cases'
    },
  };
  

Plotly.newPlot('my_dataviz', data, layout);
});
