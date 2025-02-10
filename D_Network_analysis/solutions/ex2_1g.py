
scl = 100 # scaling factor for plotting

# save a list of the degrees {NODE1: DEGREE1, NODE2: DEGREE2...}
d = dict(G.degree)

# get the nodes in same order as degrees
nl = list(d.keys()) 
print(nl)

# scale up the sizes
sz = [v*scl for v in d.values()] 
print(sz)

# now we have successfully split them into 2, with matching order
nx.draw(G, nodelist=nl, node_size=sz, with_labels=True)
