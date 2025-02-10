
btws = nx.betweenness_centrality(G2, normalized=True)
ccos = nx.algorithms.cluster.clustering(G2)
degs = [val for (node, val) in G2.degree] 

import pandas as pd

dfc = pd.DataFrame(list(zip(btws.values(), ccos.values(), degs)),
                   columns=['Betweeness', 'Clust-Coefficient', 'Degree'],
                   index = btws.keys())
print(dfc)
