import matplotlib.pyplot as plt
import networkx as nx

# Define the factors and their dependencies
factors = [
    ("Demand Variability", ["Forecast Accuracy", "Customer Demand"]),
    ("Lead Time", ["Supplier Performance", "Order Fulfillment Speed"]),
    ("Supplier Performance", ["Lead Time"]),
    ("Ordering Costs", ["EOQ", "Carrying Costs"]),
    ("Carrying Costs", ["EOQ", "Ordering Costs", "Space Constraints"]),
    ("Economic Order Quantity", ["Ordering Costs", "Carrying Costs"]),
    ("Technology and Automation", ["Supply Chain Visibility"]),
    ("Seasonality", ["Forecast Accuracy"]),
    ("ABC Analysis", ["Prioritization"]),
    ("Forecast Accuracy", ["Demand Variability", "Seasonality"]),
    ("Service Level Targets", ["Demand Variability", "Order Fulfillment Speed"]),
    ("Supply Chain Visibility", ["Technology and Automation"]),
    ("Customer Demand Patterns", ["Demand Variability"]),
    ("Order Fulfillment Speed", ["Lead Time", "Customer Demand Patterns"]),
    ("Market Trends", ["Customer Demand Patterns"]),
    ("Regulatory Compliance", ["Space Constraints"]),
    ("Space Constraints", ["Carrying Costs", "Regulatory Compliance"]),
    ("Transportation Costs", ["Global Supply Chain Dynamics"]),
    ("Global Supply Chain Dynamics", ["Transportation Costs"]),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for factor, dependencies in factors:
    G.add_node(factor)
    for dependency in dependencies:
        G.add_edge(dependency, factor)

# Define layout for better visualization
pos = nx.spring_layout(G, k=0.9)

# Draw the graph
plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, font_size=10, node_size=2000, node_color="skyblue", font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

# Add title
plt.title("Interdependencies Among Factors Affecting Inventory Optimization", fontsize=16)

# Show the plot
plt.show()
