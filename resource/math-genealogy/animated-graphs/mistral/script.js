// Read the JSON data
fetch('my_math_gen.json')
  .then(response => response.json())
  .then(data => {
    const graphData = Object.values(data);
    const links = [];
    const nodes = {};

    // Prepare nodes and links data
    graphData.forEach(nodeData => {
      nodes[nodeData.id] = { id: nodeData.id, name: nodeData.name, height: nodeData.height };
      nodeData.advisors.forEach(advisor => {
        links.push({ source: advisor.id, target: nodeData.id });
      });
    });

    // Set up the simulation
    const width = 960;
    const height = 600;
    const svg = d3.select('body').append('svg')
      .attr('width', width)
      .attr('height', height);

    const simulation = d3.forceSimulation(Object.values(nodes))
      .force('link', d3.forceLink(links).id(d => d.id))
      .force('charge', d3.forceManyBody())
      .force('center', d3.forceCenter(width / 2, height / 2));

    // Draw links
    const link = svg.selectAll('line')
      .data(links)
      .enter().append('line')
      .attr('stroke-width', 1)
      .attr('stroke', 'gray');

    // Draw nodes
    const node = svg.selectAll('circle')
      .data(Object.values(nodes))
      .enter().append('circle')
      .attr('r', 20)
      .call(drag(simulation));

    // Add node labels
    const label = svg.selectAll('text')
      .data(Object.values(nodes))
      .enter().append('text')
      .text(d => d.name)
      .attr('x', d => d.x)
      .attr('y', d => d.y + 20)
      .attr('text-anchor', 'middle')
      .style('font-size', '12px');

    // Update link and node positions
    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);

      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);

      label
        .attr('x', d => d.x)
        .attr('y', d => d.y + 20);
    });

    // Drag and drop nodes
    function drag(simulation) {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.7).restart();
        d.fx = d.x;
        d.fy = d.y;
      }

      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }

      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }

      return d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended);
    }
  })
  .catch(error => console.error('Error fetching data:', error));

