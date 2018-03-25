import numpy as nm
m=[[1,2],[1,1],[1,3]]
for i in m:
    print(i)
res=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for i in res:
    print(i)
t_mat=zip(*m)
for i in t_mat:
    print(i)
print(nm.transpose(m))