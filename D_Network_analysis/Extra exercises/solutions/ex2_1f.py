
# same approach as in the previous notebook
degs = sorted(G.degree, key=lambda item:item[1], reverse=True)
degs[:5]

# or with regular function
def func(item): 
    return item[1]

degs = sorted(G.degree, key = func, reverse=True)
degs[:5]
