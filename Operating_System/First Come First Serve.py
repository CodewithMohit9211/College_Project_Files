sequence = input("enter the sequence delimited by whitespace ").split(" ")
waiting = [0]
for i in range(0,len(sequence)-1):
    waiting.append(waiting[i]+int(sequence[i]))
print("Burst\tWaiting")
for i in range(0,len(waiting)):
    print(sequence[i],"\t",waiting[i])
print ("Average Waiting = ", sum(waiting)/len(waiting))
