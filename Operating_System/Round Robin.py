sequence = input("Enter the burst time sequence: ").split(" ")
quantum = int(input("Enter Time Quantum: "))
burst = []
remaining = []
waiting = []
for i in range(len(sequence)):
    burst.append(int(sequence[i]))
    remaining.append(int(sequence[i]))
    waiting.append(0)
time = 0
while True:
    done = True
    for i in range(len(sequence)):
        if remaining[i] > 0:
            done = False
            if remaining[i] > quantum:
                time += quantum
                remaining[i] -= quantum
            else:
                time += remaining[i]
                waiting[i] = time - burst[i]
                remaining[i] = 0
    if done:
        break
print("Pid\tBurst\tWaiting")
for i in range(len(sequence)):
    print(i + 1, "\t", burst[i], "\t", waiting[i])
print("Average Waiting = ", sum(waiting) / len(waiting))