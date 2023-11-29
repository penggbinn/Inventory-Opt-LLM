import networkx as nx
import matplotlib.pyplot as plt

# Define the factors and their dependencies
factors_dependencies = {
    "Demand Forecasting / Variability": ["Product Life Cycle", "Lead Time", "Safety Stock", "Economic Order Quantity (EOQ)"],
    "Product Life Cycle": ["Demand Forecasting / Variability", "Lead Time"],
    "Lead Time": ["Demand Forecasting / Variability", "Supplier Relationships"],
    "Safety Stock": ["Demand Forecasting / Variability", "Lead Time", "Economic Order Quantity (EOQ)"],
    "Economic Order Quantity (EOQ)": ["Lead Time", "Inventory Shrinkage", "Warehouse Management"],
    "Inventory Shrinkage": ["Warehouse Management", "Technology Integration", "Supplier Relationships"],
    "Warehouse Management": ["Inventory Shrinkage", "Technology Integration", "Supplier Relationships"],
    "Technology Integration": ["Inventory Shrinkage", "Warehouse Management"],
    "Supplier Relationships": ["Lead Time", "Inventory Shrinkage", "Warehouse Management"],
    "Internal Communication": ["Demand Forecasting / Variability", "Product Life Cycle", "Lead Time", "Safety Stock", "Economic Order Quantity (EOQ)", "Inventory Shrinkage", "Warehouse Management", "Technology Integration", "Supplier Relationships"]
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for factor, dependencies in factors_dependencies.items():
    G.add_node(factor)
    for dependency in dependencies:
        G.add_edge(dependency, factor)

# Plot the graph
pos = nx.spring_layout(G, k=1.25)  # You can choose different layout algorithms
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='skyblue', arrowsize=20)
plt.show()
