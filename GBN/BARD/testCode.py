import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes
nodes = [
    "Demand Forecasting / Variability",
    "Lead Time",
    "Safety Stock",
    "Economic Order Quantity (EOQ)",
    "Inventory Shrinkage",
    "Warehouse Management",
    "Supplier Relationships",
    "Technology Integration",
    "Customer Expectations"
]

# Define the edges
edges = [
    ("Demand Forecasting / Variability", "Lead Time"),
    ("Demand Forecasting / Variability", "Safety Stock"),
    ("Lead Time", "Supplier Relationships"),
    ("Lead Time", "Transportation Infrastructure and Logistics"),
    ("Safety Stock", "Inventory Shrinkage"),
    ("Economic Order Quantity (EOQ)", "Lead Time"),
    ("Economic Order Quantity (EOQ)", "Inventory Shrinkage"),
    ("Warehouse Management", "Inventory Shrinkage"),
    # ("Supplier Relationships", "Lead Time"),
    ("Supplier Relationships", "Technology Integration"),
    ("Customer Expectations", "Demand Forecasting / Variability")
]

bayesian_model = nx.DiGraph()
bayesian_model.add_nodes_from(nodes)
bayesian_model.add_edges_from(edges)

# Visualize the Bayesian network
pos = nx.spring_layout(bayesian_model, k=1.2)
nx.draw(bayesian_model, pos, with_labels=True, font_weight='bold', node_size=3000,
        node_color='skyblue', font_color='black', font_size=6, arrowsize=20, connectionstyle="arc3,rad=0.1")
plt.title("Bayesian Network for Inventory Optimization")
plt.show()
