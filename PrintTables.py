start=1
End=20
for i in range(start,End):
    for j in range (1,10):
        print (f"{i}*{j}={i*j}")
    
    print("----------------------")
        
start = 1
end = 20

while start <= end:
    cont = 1  
    while cont <= 10:
        print(f"{start} * {cont} = {start * cont}")
        cont += 1
    print("----------------------") 
    start += 1