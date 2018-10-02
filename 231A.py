n = int(input())
count = 0
for i in range(n):
    a = list(map(int, input().strip().split( " ")))        
    if sum(a) >= 2:
        count = count + 1
print (count)
        
       
