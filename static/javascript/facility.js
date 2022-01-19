d3.csv("../../static/csv/data.csv", function (data) {
    function tabulate(data, columns) {
        let table = d3.select("#csvHere")
            , columnNames = columns
            , thead = table.append("thead")
            , tbody = table.append("tbody");

        thead.append("tr")
            .selectAll("th")
            .data(columnNames)
            .enter()
            .append("th")
            .text(function (columnNames) {return columnNames; });

        // create a row for each object in the data
        let rows = tbody.selectAll("tr")
            .data(data)
            .enter()
            .append("tr");

        // create a cell in each row for each column
        let cells = rows.selectAll("td")
            .data(function (row) {
                return columns.map(function (column) {
                    return { column: column, value: row[column] };
                });
            })
            .enter()
            .append("td")
            .html(function (d) {return d.value; });
        return table;
    };
    tabulate(data, ["name", "address", "latitude", "longitude"])//The names of the columns in the CSV file
});

let btn1 = document.getElementById('btn1')
let btn2 = document.getElementById('btn2')
let btn3 = document.getElementById('btn3')
let btn4 = document.getElementById('btn4')
let btn5 = document.getElementById('btn5')
const map1 = document.querySelector('#map1');
const map2 = document.querySelector('#map2');
const map3 = document.querySelector('#map3');
const map4 = document.querySelector('#map4');
const map5 = document.querySelector('#map5');

btn1.onclick = function() {
    map1.style.display = 'block';
    map2.style.display = 'none';
    map3.style.display = 'none';
    map4.style.display = 'none';
    map5.style.display = 'none';
}
btn2.onclick = function() {
    map1.style.display = 'none';
    map2.style.display = 'block';
    map3.style.display = 'none';
    map4.style.display = 'none';
    map5.style.display = 'none';
}
btn3.onclick = function() {
    map1.style.display = 'none';
    map2.style.display = 'none';
    map3.style.display = 'block';
    map4.style.display = 'none';
    map5.style.display = 'none';
}
btn4.onclick = function() {
    map1.style.display = 'none';
    map2.style.display = 'none';
    map3.style.display = 'none';
    map4.style.display = 'block';
    map5.style.display = 'none';
}
btn5.onclick = function() {
    map1.style.display = 'none';
    map2.style.display = 'none';
    map3.style.display = 'none';
    map4.style.display = 'none';
    map5.style.display = 'block';
}
