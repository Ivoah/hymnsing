var svg = d3.select("svg"),
    margin = 200,
    width = svg.attr("width") - margin,
    height = svg.attr("height") - margin - 100;

var x = d3.scaleBand().range([0, width]).padding(0.4),
    y = d3.scaleLinear().range([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + 100 + "," + 100 + ")");

d3.csv("history.csv", function (error, data) {
    if (error) {
        console.log("error");
        throw error;
    }
    
    x.domain(data.map(d => d.hymn));
    y.domain([0, d3.max(data, d => parseInt(d.count))]);

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", function (d) {
            return "rotate(-65)"
        });

    g.append("g")
        .call(d3.axisLeft(y).tickFormat(function (d) {
            return d;
        }).ticks(10))
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", 0 - (height / 2))
        .attr("dy", "-4em")
        .attr("text-anchor", "middle")
        .attr("stroke", "black")
        .text("Times Sung Recently");

    g.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .on("mouseover", onMouseOver) //Add listener for the mouseover event
        .on("mouseout", onMouseOut)   //Add listener for the mouseout event
        .attr("x", d => x(d.hymn))
        .attr("y", d => y(d.count))
        .attr("width", x.bandwidth())
        .transition()
        .ease(d3.easeLinear)
        .duration(400)
        .delay((d, i) => i * 50)
        .attr("height", d => height - y(d.count));
});

//mouseover event handler function
function onMouseOver(d, i) {
    d3.select(this).attr('class', 'highlight');
    d3.select(this)
        .transition()     // adds animation
        .duration(400)
        .attr('width', x.bandwidth() + 6)
        .attr('x', x(d.hymn) - 3)
        .attr("y", function (d) { return y(d.count) - 10; })
        .attr("height", function (d) { return height - y(d.count) + 10; });

    g.append("text")
        .attr('class', 'val')
        .attr('x', function () {
            return x(d.hymn) + x.bandwidth() / 2;
        })
        .attr('y', function () {
            return y(d.count) - 15;
        })
        .text(function () {
            return [d.count];  // Value of the text
        });
}

//mouseout event handler function
function onMouseOut(d, i) {
    // use the text label class to remove label on mouseout
    d3.select(this).attr('class', 'bar');
    d3.select(this)
        .transition()     // adds animation
        .duration(400)
        .attr('width', x.bandwidth())
        .attr('x', x(d.hymn))
        .attr("y", function (d) { return y(d.count); })
        .attr("height", function (d) { return height - y(d.count); });

    d3.selectAll('.val')
        .remove()
}
