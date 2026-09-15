class node:
    def __init__(this, pid, burst):
        this.pid = pid
        this.burst = burst
sequence = input("enter the sequence delimited by whitespace ").split(" ")
nodes = []
waiting = [0]
for i in range(0,len(sequence)):
    nodes.append(node(i+1,int(sequence[i])))
for i in range(0,len(sequence)):
    for j in range(0,len(sequence)-1-i):
        if(nodes[j].burst>nodes[j+1].burst):
            temp = nodes[j]
            nodes[j] = nodes[j+1]
            nodes[j+1] = temp
            
for i in range(0,len(sequence)-1):
    waiting.append(waiting[i]+nodes[i].burst)
print("Pid\tBurst\tWaiting")
for i in range(0,len(waiting)):
    print(nodes[i].pid,"\t",nodes[i].burst,"\t",waiting[i])
print ("Average Waiting = ", sum(waiting)/len(waiting))