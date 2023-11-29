import networkx as nx
import matplotlib.pyplot as plt

# Define the structure of the Bayesian Network
nodes = [
    "Market Trends", "Demand Variability",
    "Supplier Performance",
    "Order Fulfillment Speed",
    "Lead Time", "Forecast Accuracy",
    "Service Level Targets", "Technology & Automation"
]

edges = [
    ("Market Trends", "Demand Variability"),
    ("Demand Variability", "Supplier Performance"),
    ("Demand Variability", "Order Fulfillment Speed"),
    ("Lead Time", "Forecast Accuracy"),
    ("Lead Time", "Supplier Performance"),
    ("Supplier Performance", "Order Fulfillment Speed"),
    ("Demand Variability", "Forecast Accuracy"),
    ("Demand Variability", "Service Level Targets"),
    ("Forecast Accuracy", "Technology & Automation"),
    ("Service Level Targets", "Technology & Automation"),
]

# Create a Bayesian Model
bayesian_model = nx.DiGraph()
bayesian_model.add_nodes_from(nodes)
bayesian_model.add_edges_from(edges)

# Visualize the Bayesian Network
pos = nx.spring_layout(bayesian_model)
nx.draw(bayesian_model, pos, with_labels=True, font_weight='bold', node_size=3000,
        node_color='skyblue', font_color='black', font_size=6, arrowsize=20, connectionstyle="arc3,rad=0.1")
plt.title("Bayesian Network for Inventory Optimization Factors")
plt.show()
