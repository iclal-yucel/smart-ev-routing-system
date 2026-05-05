import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read dataset
print("Loading dataset...")
df = pd.read_csv("data/network_data.csv")

# Calculate total weight
df['weight'] = df['distance'] + df['traffic']

# Create graph
G = nx.Graph()

# Add edges to graph
for index, row in df.iterrows():
    G.add_edge(
        row['source'],
        row['target'],
        weight=row['weight'],
        distance=row['distance'],
        traffic=row['traffic']
    )

# Unavailable charging stations
unavailable_stations = ['C']

# Remove unavailable stations
for station in unavailable_stations:
    if station in G:
        G.remove_node(station)

# User input
start_node = input("Enter your starting location: ")
target_node = input("Enter charging station destination: ")

# Battery limit
battery_limit = 20

try:
    # Calculate shortest path
    shortest_path = nx.shortest_path(
        G,
        source=start_node,
        target=target_node,
        weight='weight'
    )

    # Calculate total cost
    total_cost = nx.shortest_path_length(
        G,
        source=start_node,
        target=target_node,
        weight='weight'
    )

    print("\n===== OPTIMIZATION RESULT =====")
    print("Optimal Route:", " -> ".join(shortest_path))
    print("Total Cost:", total_cost)

    # Battery feasibility check
    if total_cost > battery_limit:
        print("WARNING: Battery level insufficient for this route.")
    else:
        print("Battery level sufficient.")

    # Save results
    with open("results/solution_output.txt", "w") as file:
        file.write("SMART EV CHARGING ROUTING SYSTEM\n")
        file.write("================================\n")
        file.write(f"Optimal Route: {' -> '.join(shortest_path)}\n")
        file.write(f"Total Cost: {total_cost}\n")

    # Visualization

    plt.figure(figsize=(12,8))
    
    pos = nx.kamada_kawai_layout(G)

    node_colors = []

    charging_stations = [
   	 'EV Station Metro',
   	 'EV Station Home',
 	 'EV Station Akasya'
    ]

    for node in G.nodes():
    	if node in charging_stations:
            node_colors.append('mediumseagreen')
    	elif node == start_node:
            node_colors.append('deepskyblue')
    	else:
            node_colors.append('silver')

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=3000
    )

    station_nodes = [node for node in G.nodes() if node in charging_stations]

    nx.draw_networkx_nodes(
    	G,
    	pos,
    	nodelist=station_nodes,
    	node_color='mediumseagreen',
    	node_size=3500,
    	node_shape='s'
    )

    # Draw labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10,
        font_weight='bold'
    )

    # Draw all edges
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color='gray',
        width=2
    )

    # Highlight shortest path
    path_edges = list(zip(shortest_path, shortest_path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color='crimson',
        width=4
    )

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Smart EV Charging Routing Optimization", fontsize=18, fontweight='bold')

    plt.savefig("results/highlighted_route.png")

    plt.show()

except nx.NetworkXNoPath:
    print("No route found.")

except nx.NodeNotFound:
    print("Invalid node entered.")




