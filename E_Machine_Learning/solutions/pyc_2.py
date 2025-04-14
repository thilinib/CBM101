
# this would work if the cluster numbers were the same. The problem is that they're not
print(sum(y == pred)/y.size)

# what we need to do is to change the cluster numbers same in both groups. 
# In this case clusters are clearly separated and we can use the plots above as a guide which clusters to change

pred2 = pred.copy() # a copy of pred so that we don't write over any cluster
pred2[pred == 3] = 0
pred2[pred == 2] = 3
pred2[pred == 0] = 2

sum(y == pred2)/y.size # 0,989... or 178/180
