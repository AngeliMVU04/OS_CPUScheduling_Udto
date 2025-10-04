def rr(processes, quantum):
    time = 0
    queue = []
    gantt_chart = []
    timeline = [0]
    remaining_bt = {p['name']: p['BT'] for p in processes}
    completed = {}
    arrived = []

    while len(completed) < len(processes):
        # Add newly arrived processes to the queue
        for p in processes:
            if p['AT'] <= time and p['name'] not in arrived:
                queue.append(p['name'])
                arrived.append(p['name'])

        # If no process has arrived yet, move time forward
        if not queue:
            time += 1
            continue

        # Execute current process
        current = queue.pop(0)
        exec_time = min(quantum, remaining_bt[current])
        time += exec_time
        remaining_bt[current] -= exec_time
        gantt_chart.append(current)
        timeline.append(time)

        # Check if new processes arrived during execution
        for p in processes:
            if p['AT'] <= time and p['name'] not in arrived:
                queue.append(p['name'])
                arrived.append(p['name'])

        # If process still has remaining burst time, requeue it
        if remaining_bt[current] > 0:
            queue.append(current)
        else:
            # Process is completed
            proc = next(p for p in processes if p['name'] == current)
            proc['CT'] = time
            proc['TAT'] = proc['CT'] - proc['AT']
            proc['WT'] = proc['TAT'] - proc['BT']
            completed[current] = proc

    return list(completed.values()), gantt_chart, timeline


def display_table(processes):
    print("\n| Process | AT | BT | CT | TAT | WT |")
    print("|---------|----|----|----|-----|----|")
    for p in processes:
        print(f"| {p['name']:<7} | {p['AT']:<2} | {p['BT']:<2} | {p['CT']:<2} | {p['TAT']:<3} | {p['WT']:<2} |")

    avg_tat = sum(p['TAT'] for p in processes) / len(processes)
    avg_wt = sum(p['WT'] for p in processes) / len(processes)
    print(f"\nAverage TAT = {avg_tat:.2f}")
    print(f"Average WT = {avg_wt:.2f}")


def display_gantt(gantt_chart, timeline):
    print("\nGantt Chart (RR):")
    print(" | " + " | ".join(gantt_chart) + " |")
    print(" ", end="")
    for t in timeline:
        print(f"{t:<4}", end="")
    print("\n")


if __name__ == "__main__":
    print("=== Round Robin CPU Scheduling ===")
    quantum = int(input("Enter Time Quantum: "))
    n = int(input("Enter number of processes: "))

    processes = []
    for i in range(n):
        print(f"\nProcess P{i+1}")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        processes.append({'name': f'P{i+1}', 'AT': at, 'BT': bt})

    scheduled, gantt, timeline = rr(processes, quantum)
    display_table(scheduled)
    display_gantt(gantt, timeline)
