---
layout: single
permalink: /math-gen/10/
author_profile: true
title: Math Genealogy - depth 10 from Sunghee
toc: false
toc_label: "ToC"
toc_icon: "cog"
toc_sticky: true
---

<!--html lang="en"-->
<head>
	<!--title>Math Genealogy - starting from Mr. Funnybunny - depth 10</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Genealogy Graph</title-->
    <!-- Include D3.js from a CDN -->
	<link rel="stylesheet" href="/resource/styles.css">
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        .node {
            //fill: rgba(0, 0, 255, .8);
            stroke: #fff;
            stroke-width: 2px;
        }
        .link {
            stroke: rgba(0, 0, 0, .5);
			stroke-width: 1.5px;
        }
        .node-label {
            font-size: 14px;
            pointer-events: none;
        }
        .tooltip {
            position: absolute;
            background-color: white;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
            pointer-events: none;
        }
	</style>
</head>
<script src="/resource/math-genealogy/animated-graphs/claude/math-genealogy-graph-10.js"></script>

<div id="graph"></div>
