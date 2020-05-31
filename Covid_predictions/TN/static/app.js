// REQUEST THE DATA
const url5 = "/TNDeptHealth_counties";
d3.json(url5).then(function(data) {
  // console.log(data);
  let dates = Object.values(data["DATE"])
  // console.log(age_groups)
  let active_cases = Object.values(data["TOTAL_ACTIVE"])
  // console.log(age_cases)
  let counties = Object.values(data['COUNTY'])
  let new_cases = Object.values(data["NEW_CASES"])
  let total_cases = Object.values(data["TOTAL_CASES"])
  let total_recovered = Object.values(data["TOTAL_RECOVERED"])
  console.log(total_cases)
  console.log(total_recovered)

  var trace1 = {
x: dates,
y: active_cases,
mode: 'markers',
opacity : .7,
type: 'bar',
name: 'active cases',
text: counties,
marker: { color : 'Sky Blue',
size: 12,
line: {
  color: 'MediumPurple',
  width: 1
}
}
};
  var trace2 = {
x: dates,
y: new_cases,
opacity : .7,
type: 'line',
color: 'Red',
name: 'new cases',

};

  var trace3 = {
x: dates,
y: total_cases,
opacity : .7,
type: 'line',
color: 'Black',
name: 'total cases',

};

  var trace4 = {
x: dates,
y: total_recovered,
opacity : .7,
type: 'line',
color: 'Green',
name: 'total recovered',
};


var data = [ trace1,trace2,trace3,trace4 ];

var layout = {
title: 'All Counties "ACTIVE CASES vs TOTAL and RECOVERED"',
xaxis: {
title: 'Date',
tickmode: 'auto'
},
yaxis: {
title: 'Cases'
},
legend: {
x: 0,
y: 1,
traceorder: 'normal',
font: {
  family: 'sans-serif',
  size: 12,
  color: '#000'
},
}
};
          
        
Plotly.newPlot('histogram', data, layout);
});

const url = "/TNDeptHealth_overall";
d3.json(url).then(function(data) {
  // console.log(data);
    let facility = Object.values(data["Laboratory Type"])
        // console.log(facility)
    let positive = Object.values(data["Positive Test"])
        // console.log(positive)
    let negative = Object.values(data["Negative Tests"])
        // console.log(negative)
    let total = Object.values(data["Total"])
        // console.log(total)
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
  // console.log(data);
    let age_groups = Object.values(data["Age Ranges of Confirmed Cases"])
        // console.log(age_groups)
    let age_cases = Object.values(data["Number_Cases"])
        // console.log(age_cases)


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

const url8 = "/TNDeptHealth_overtime";
d3.json(url8).then(function(data) {
  // console.log(data);
  let dates = Object.values(data["DATE"])
        // console.log(age_groups)
  let active_cases = Object.values(data["TOTAL_ACTIVE"])
        // console.log(age_cases)
  let counties = Object.values(data['COUNTY'])
  let new_cases = Object.values(data["NEW_CASES"])
  let total_cases = Object.values(data["TOTAL_CASES"])
  let total_recovered = Object.values(data["TOTAL_RECOVERED"])
    console.log(total_cases)
    console.log(total_recovered)
  
  var trace1 = {
    x: dates,
    y: active_cases,
    mode: 'markers',
    opacity : .7,
    type: 'bar',
    name: 'active cases',
    text: counties,
    marker: { color : 'Sky Blue',
      size: 12,
      line: {
        color: 'MediumPurple',
        width: 1
    }
   }
  };
  var trace2 = {
    x: dates,
    y: new_cases,
    opacity : .7,
    type: 'line',
    color: 'Red',
    name: 'new cases',
  
  };

  var trace3 = {
    x: dates,
    y: total_cases,
    opacity : .7,
    type: 'line',
    color: 'Black',
    name: 'total cases',
    
  };

  var trace4 = {
    x: dates,
    y: total_recovered,
    opacity : .7,
    type: 'line',
    color: 'Green',
    name: 'total recovered',
   
  };

  
  var data = [ trace1,trace2,trace3,trace4 ];
  
  var layout = {
    title: 'Davidson "ACTIVE CASES vs TOTAL and RECOVERED"',
    xaxis: {
      title: 'Date',
      tickmode: 'auto'
    },
    yaxis: {
      title: 'Cases'
    },
    legend: {
      x: 0,
      y: 1,
      traceorder: 'normal',
      font: {
        family: 'sans-serif',
        size: 12,
        color: '#000'
      },
    }
  };
  

Plotly.newPlot('overtime', data, layout);
});

