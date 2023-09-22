
# new column for classes
df['species'] = data.target


# to get the target_names:
n = data.target_names 

# you can use map-function ('replace' works too)
df['species'] = df.species.map({0:n[0], 
                                1:n[1], 
                                2:n[2]})
