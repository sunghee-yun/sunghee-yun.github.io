// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Load and process the JSON data
    d3.json("/resource/math-genealogy/animated-graphs/claude/my_math_gen - 15.json").then(function(data) {
        const nodes = Object.values(data);
        const links = [];

        // Create links from advisors, handling multiple advisors
        nodes.forEach(node => {
            if (node.advisors) {
                node.advisors.forEach(advisor => {
                    if (data[advisor.id]) {  // Check if advisor exists in the data
                        links.push({
                            source: node.id,
                            target: advisor.id
                        });
                    }
                });
            }
        });

        // Set up the SVG
        //const width = window.innerWidth * .9;
        //const height = window.innerHeight * .9;
        const width = Math.min(600, window.innerWidth * .9)  // window.innerWidth * .4;
        const height = 600 // window.innerHeight * .6;
        const svg = d3.select("#graph")
            .append("svg")
            .attr("width", width)
            .attr("height", height);
        const padding = 20;

        function boundingBoxForce() {
            for (let node of nodes) {
                node.x = Math.max(padding, Math.min(width - padding, node.x));
                node.y = Math.max(padding, Math.min(height - padding, node.y));
            }
        }

        // Add this part
        svg.append("defs").append("marker")
            .attr("id", "arrowhead")
            .attr("viewBox", "-0 -5 10 10")
            .attr("refX", 10)  // Adjust this value to position the arrowhead
            .attr("refY", 0)
            .attr("orient", "auto")
            .attr("markerWidth", 13)
            .attr("markerHeight", 13)
            .attr("xoverflow", "visible")
            .append("svg:path")
            .attr("d", "M 0,-5 L 10 ,0 L 0,5")
            .attr("fill", "rgba(100, 100, 100, .8)")
            .style("stroke", "none");

        // Create a force simulation
		const link_length_ratio = .001;
		const min_dim = Math.min(width, height)
		const link_length = link_length_ratio * min_dim

		const charge_strength_ratio = .05;
		const charge_strength = charge_strength_ratio * min_dim

		console.log(window.innerWidth)
		console.log(window.innerHeight)
		console.log(link_length)
		console.log(charge_strength)
        const simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id).distance(link_length))
            .force("charge", d3.forceManyBody().strength(-charge_strength))
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("boundary", boundingBoxForce); // Add this line

        // Create links
        const link = svg.append("g")
            .selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("class", "link")
            .attr("marker-end", "url(#arrowhead)");  // Add this line

        // Create nodes
        const node = svg.append("g")
            .selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("class", "node")
            .attr("r", 12)
            .attr("fill", "rgba(000,000,255,.8)")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        // Function to determine label color
        function getLabelColor(d) {
            // Add your logic here to determine the color
            // For example, you could use the node's id, name, or any other property
            //if (d.id === "12345") return "red";
			//console.log("Node name:", d.name); // Add
            if (d.name === "Sunghee Yun") {console.log(d.name); return "blue";}
            if (d.name.startsWith("Carl Friedrich")) {console.log(d.name); return "red";}
			if (d.name === "Jean-Baptiste Joseph Fourier") {console.log(d.name); return "red";}
			if (d.name === "Rudolf Otto Sigismund Lipschitz") {console.log(d.name); return "red";}
			if (d.name.includes(" Denis Poisson")) {console.log(d.name); return "red";}
			if (d.name === "Stephen Poythress Boyd") {console.log(d.name); return "red";}
			if (d.name === "Stephen Poythress Boyd") {console.log(d.name); return "red";}
			if (d.name === "Gustav Peter Lejeune Dirichlet") {console.log(d.name); return "red";}
			if (d.name.startsWith("Pierre-Simon")) {console.log(d.name); return "red";}
			if (d.name === "Leonhard Euler") {console.log(d.name); return "red";}
			if (d.name === "Jacob Bernoulli") {console.log(d.name); return "red";}
			if (d.name === "C. Felix (Christian) Klein") {console.log(d.name); return "red";}
            //if (d.id === "283283" ) {console.log(d.name); return "red";}
            //if (d.id === "283283" ) {console.log(d.name); return "red";}
            // Add more conditions as needed
            return "black"; // default color
        }

        // Add labels to nodes with selective coloring
        const label = svg.append("g")
            .selectAll("text")
            .data(nodes)
            .enter().append("text")
            .attr("text-anchor", "middle")
            .attr("class", "node-label")
            .text(d => d.name)
            .attr("fill", getLabelColor);  // Apply the color function here

        // Create tooltip
        const tooltip = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        // Add hover effects
        node.on("mouseover", function(event, d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", .9);
            let advisorNames = d.advisors ? d.advisors.map(a => a.name).join(", ") : "None";
            tooltip.html(`Name: ${d.name}<br>ID: ${d.id}<br>Height: ${d.height}<br>Advisors: ${advisorNames}`)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 28) + "px");
        })
        .on("mouseout", function(d) {
            tooltip.transition()
                .duration(500)
                .style("opacity", 0);
        });

        // Update positions on each tick of the simulation
        simulation.on("tick", () => {
            boundingBoxForce(); //
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => {
                    const dx = d.target.x - d.source.x;
                    const dy = d.target.y - d.source.y;
                    const dr = Math.sqrt(dx * dx + dy * dy);
                    return d.target.x - (dx * 12) / dr;  // 12 is the node radius
                })
                .attr("y2", d => {
                    const dx = d.target.x - d.source.x;
                    const dy = d.target.y - d.source.y;
                    const dr = Math.sqrt(dx * dx + dy * dy);
                    return d.target.y - (dy * 12) / dr;  // 12 is the node radius
                });

            node
                .attr("cx", d => d.x)
                .attr("cy", d => d.y);

            label
                .attr("x", d => d.x + 0)
                .attr("y", d => d.y + 30);
        });

        // Drag functions
        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = clamp(event.x, padding, width - padding);
            d.fy = clamp(event.y, padding, height - padding);
        }

        function dragged(event, d) {
            d.fx = clamp(event.x, padding, width - padding);
            d.fy = clamp(event.y, padding, height - padding);
        }

        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

        function clamp(value, min, max) {
            return Math.max(min, Math.min(max, value));
        }
    }).catch(function(error) {
        console.log("Error loading the JSON file:", error);
    });
});
