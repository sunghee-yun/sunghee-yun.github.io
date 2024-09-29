import json
import networkx as nx


def create_graph(data_file):
    """Creates a NetworkX graph from a JSON file.

    Args:
        data_file: Path to the JSON file.

    Returns:
        A NetworkX DiGraph object.
    """

    with open(data_file, "r") as f:
        data = json.load(f)

    G = nx.DiGraph()

    for node_id, node_data in data.items():
        G.add_node(node_id, name=node_data["name"], height=node_data["height"])
        for advisor in node_data["advisors"]:
            G.add_edge(advisor["id_"], node_id)

    return G


# Example usage
data_file = "../../crawl/my_math_gen.json"
graph = create_graph(data_file)
