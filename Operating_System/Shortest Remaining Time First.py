# SRTF - Shortest Remaining Time First

class node:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0


n = int(input("Enter number of processes: "))

nodes = []

for i in range(n):
    arrival, burst = map(int, input(
        f"Enter arrival time and burst time for P{i + 1}: "
    ).split())

    nodes.append(node(i + 1, arrival, burst))


time = 0
completed = 0

while completed < n:

    shortest = -1

    for i in range(n):
        if nodes[i].arrival <= time and nodes[i].remaining > 0:

            if shortest == -1 or nodes[i].remaining < nodes[shortest].remaining:
                shortest = i

    if shortest == -1:
        time += 1
        continue

    # Execute process for 1 unit of time
    nodes[shortest].remaining -= 1
    time += 1

    # Check if process is completed
    if nodes[shortest].remaining == 0:
        nodes[shortest].completion = time

        nodes[shortest].turnaround = (
            nodes[shortest].completion - nodes[shortest].arrival
        )

        nodes[shortest].waiting = (
            nodes[shortest].turnaround - nodes[shortest].burst
        )

        completed += 1


# Display results
print("\nPid\tAT\tBT\tCT\tWT\tTAT")

total_wt = 0
total_tat = 0

for process in nodes:
    print(
        process.pid, "\t",
        process.arrival, "\t",
        process.burst, "\t",
        process.completion, "\t",
        process.waiting, "\t",
        process.turnaround
    )

    total_wt += process.waiting
    total_tat += process.turnaround


print("\nAverage Waiting =", total_wt / n)
print("Average Turnaround =", total_tat / n)
