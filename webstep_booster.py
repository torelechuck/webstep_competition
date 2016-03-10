max = 1000000

fns = [0]*max
fns[1] = 1 #n = 1 has sequence [1], thus f(1) = 1 

for i in range(1, max):
    for j in range(2*i, max, i):
        fns[j] += fns[i]
        
        
equalFns = [n for (i,n) in enumerate(fns) if n == i]

print(sum(equalFns))
