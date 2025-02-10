
G = nx.DiGraph() #create new directed graph
G.add_nodes_from(nodes) #add nodes
G.add_edges_from(edges) #add one-way edges
m = MatrixPlot(G)

