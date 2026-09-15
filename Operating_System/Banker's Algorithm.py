def getMatrix(pro, res):
    matrix = []
    for i in range(pro):
        resource = []
        for j in range(res):
            resource.append(int(input("P"+str(i)+" R"+str(j)+":")))
        matrix.append(resource)
    return matrix

#initialization
processes = int(input("Enter the number of processes "))
resources = int(input("Enter the number of resources "))
print("Enter Allocation Matrix")
allocation = getMatrix(processes, resources)
print("Enter Maximum Matrix")
maximum = getMatrix(processes, resources)
print("Enter Available Resources")
available = []
for i in range(resources):
    available.append(int(input("R:" + str(i))))
work = available[:]
need = maximum[:]
finish = []
for i in range(processes):
    finish.append(False)
    for j in range(resources):
        need[i][j] -= allocation[i][j]
        
#main logic
sequence = []
while(True):
    flag = True
    for i in range(processes):
        if(not finish[i]):
            if(need[i]<=work):
                finish[i] = True
                flag = False
                for j in range(resources):
                    work[j] +=  allocation[i][j]
                sequence.append(i)               
    if(flag):
        if(len(sequence)!=processes):
            print("No Safe Sequence found")
        else:
            print("Safe Sequence:" + str(sequence))
        break   