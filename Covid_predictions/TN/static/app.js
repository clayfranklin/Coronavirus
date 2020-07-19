
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
  let new_tests = Object.values(data["NEW_TESTS"])
  let new_hosp = Object.values(data["NEW_HOSPITALIZED"])
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

  var trace5 = {
    x: dates,
    y: new_tests,
    opacity : .7,
    type: 'line',
    color: 'Violet',
    name: 'new tests',
   
  };

  var trace6 = {
    x: dates,
    y: new_hosp,
    opacity : .7,
    type: 'line',
    color: 'Violet',
    name: 'new hospitalizations',
   
  };

  
  var data = [ trace1,trace2,trace3,trace4, trace5, trace6 ];
  
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

// const url11 = "/TNDeptHealth_totals_overtime";
// d3.json(url11).then(function(data) {
//   // console.log(data);
//   let dates2 = Object.values(data["DATE"])
//         // console.log(age_groups)
//   let active_cases2 = Object.values(data["TOTAL_ACTIVE"])
//         // console.log(age_cases)
//   let new_cases2 = Object.values(data["NEW_CASES"])
//   let total_cases2 = Object.values(data["TOTAL_CASES"])
//   let total_recovered2 = Object.values(data["TOTAL_RECOVERED"])
//     console.log(total_cases2)
//     console.log(total_recovered2)
  
//   var trace1 = {
//     x: dates2,
//     y: active_cases2,
//     mode: 'markers',
//     opacity : .7,
//     type: 'bar',
//     name: 'active cases',
//     marker: { color : 'Sky Blue',
//       size: 12,
//       line: {
//         color: 'MediumPurple',
//         width: 1
//     }
//    }
//   };
//   var trace2 = {
//     x: dates2,
//     y: new_cases2,
//     opacity : .7,
//     type: 'line',
//     color: 'Red',
//     name: 'new cases',
  
//   };

//   var trace3 = {
//     x: dates2,
//     y: total_cases2,
//     opacity : .7,
//     type: 'line',
//     color: 'Black',
//     name: 'total cases',
    
//   };

//   var trace4 = {
//     x: dates2,
//     y: total_recovered2,
//     opacity : .7,
//     type: 'line',
//     color: 'Green',
//     name: 'total recovered',
   
//   };

  
//   var data = [ trace2 ];
  
//   var layout = {
//     title: 'TN "ACTIVE CASES vs TOTAL and RECOVERED"',
//     xaxis: {
//       title: 'Date',
//       tickmode: 'auto'
//     },
//     yaxis: {
//       title: 'Cases'
//     },
//     legend: {
//       x: 0,
//       y: 1,
//       traceorder: 'normal',
//       font: {
//         family: 'sans-serif',
//         size: 12,
//         color: '#000'
//       },
//     }
//   };


// Plotly.newPlot('totals_overtime', data, layout);
// });


// function updatePlotly(newdata) {
//   Plotly.restyle("overtime", [newdata.DATE]);
//   Plotly.restyle("overtime", [newdata.NEW_CASES]);
//   Plotly.restyle("overtime", [newdata.TOTAL_ACTIVE]);
//   Plotly.restyle("overtime", [newdata.TOTAL_RECOVERED]);
// }
  
//   // Get new data whenever the dropdown selection changes
// function getData(route) {
//   console.log(route);
//   d3.json(`/${route}`).then(function(data) {
//   console.log("newdata", data);
//   updatePlotly(data);
  
//  });
// }