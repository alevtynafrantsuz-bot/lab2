a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d > b:
    overtraffic = d - b
    total_cost = a + (overtraffic * c)
else:
    total_cost = a
    
print(total_cost)