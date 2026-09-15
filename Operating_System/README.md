# Operating System Algorithms & Concepts Simulations

This folder contains Python simulations of standard Operating System (OS) concepts, specifically covering **CPU Scheduling Algorithms**, **Process Synchronization**, **Inter-Process Communication (IPC)**, and **Deadlock Avoidance**.

These scripts are written in Python and serve as educational implementations of core operating system theories.

---

## Table of Contents

1. [CPU Scheduling Algorithms](#1-cpu-scheduling-algorithms)
   - [First Come First Serve (FCFS)](#first-come-first-serve-fcfs)
   - [Shortest Job First (SJF)](#shortest-job-first-sjf)
   - [Round Robin (RR)](#round-robin-rr)
2. [Process Synchronization & IPC](#2-process-synchronization--ipc)
   - [Inter-Process Communication (IPC)](#inter-process-communication-ipc)
   - [Producer-Consumer Problem](#producer-consumer-problem)
3. [Deadlock Avoidance](#3-deadlock-avoidance)
   - [Banker's Algorithm](#bankers-algorithm)
4. [Prerequisites & Running the Code](#4-prerequisites--running-the-code)

---

## 1. CPU Scheduling Algorithms

These scripts simulate how the CPU allocates execution time to processes based on different scheduling strategies. They assume all processes arrive at time `0` (non-preemptive for FCFS/SJF, and preemptive with quantum for Round Robin) and compute the waiting times along with the average waiting time.

### First Come First Serve (FCFS)
* **File:** `First Come First Serve.py`
* **Concept:** Processes are dispatched in the order they arrive.
* **Input:** Space-delimited sequence of burst times (e.g., `10 5 8`).
* **Output:** Table showing each process's burst time, waiting time, and the average waiting time of the sequence.

### Shortest Job First (SJF)
* **File:** `Shortest Job First.py`
* **Concept:** Non-preemptive scheduling where the process with the smallest burst time is executed next.
* **How it works:** The script reads a space-delimited list of burst times, creates process objects, sorts them in ascending order of their burst times, and then calculates and displays their waiting times.

### Round Robin (RR)
* **File:** `Round Robin.py`
* **Concept:** Preemptive scheduling where each process is assigned a fixed time slot (Time Quantum) in a cyclic order.
* **Input:**
  - Space-delimited sequence of burst times (e.g., `24 3 3`).
  - An integer representing the Time Quantum.
* **Output:** Displays the Pid, burst time, and computed waiting time for each process, followed by the overall average waiting time.

---

## 2. Process Synchronization & IPC

These scripts demonstrate concurrency concepts utilizing Python's built-in `multiprocessing` library to create and coordinate actual system processes.

### Inter-Process Communication (IPC)
* **File:** `Demonstrate  Inter-Process Communication.py`
* **Concept:** Demonstrates how two separate processes (a Reader and a Writer) communicate and share data through shared memory.
* **How it works:** Uses `multiprocessing.Value('i', 0)` to instantiate a shared integer variable. The Writer process continuously updates this value, while the Reader process reads and prints it with synchronization simulated using delays.

### Producer-Consumer Problem
* **File:** `Demonstrate Producer-Consumer.py`
* **Concept:** Resolves the classical multi-process synchronization problem using Semaphores.
* **How it works:**
  - Uses `multiprocessing.Array` as a shared buffer.
  - Employs three Semaphores to coordinate process execution:
    - `empty`: initialized to `1` (tracks empty slots in buffer).
    - `full`: initialized to `0` (tracks filled slots in buffer).
    - `mutex`: initialized to `1` (ensures mutual exclusion in the critical section).
  - The producer process generates data and releases the `full` semaphore, while the consumer process acquires `full` and releases `empty` to consume.

---

## 3. Deadlock Avoidance

### Banker's Algorithm
* **File:** `Banker's Algorithm.py`
* **Concept:** A resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of pre-determined maximum possible resources.
* **How it works:**
  1. Requests input for the number of processes and types of resources.
  2. Asks for the **Allocation Matrix** and the **Maximum Need Matrix**.
  3. Prompts for the current **Available Resources** vector.
  4. Automatically computes the **Need Matrix** (`Need = Max - Allocation`).
  5. Determines and prints a **Safe Sequence** if one exists, verifying if the system can safely execute all processes without deadlock. If not, it outputs `No Safe Sequence found`.

---

## 4. Prerequisites & Running the Code

### Prerequisites
* **Python 3.x** installed. No external packages are required as all scripts utilize standard built-in libraries (`multiprocessing`, `time`).

### Running a script
To run any of the simulation scripts, open your terminal/command prompt, navigate to this folder, and run:

```bash
python "Name_of_Script.py"
```

For scripts with spaces in their names, make sure to wrap the filename in quotation marks. For example:

```bash
python "Round Robin.py"
```
