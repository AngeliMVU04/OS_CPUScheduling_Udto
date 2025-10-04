def fcfs(processes):
    processes.sort(key=lambda x: x['AT'])
    time = 0
    gantt_chart = []
    timeline = [0]

    for p in processes:
        if time < p['AT']:
            time = p['AT']
        p['CT'] = time + p['BT']
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']
        time = p['CT']
        gantt_chart.append(p['name'])
        timeline.append(time)

    return processes, gantt_chart, timeline

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
    print("\nGantt Chart (FCFS):")
    print(" | " + " | ".join(gantt_chart) + " |")
    print(" ", end="")
    for t in timeline:
        print(f"{t:<4}", end="")

if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        at = int(input(f"Arrival Time of P{i+1}: "))
        bt = int(input(f"Burst Time of P{i+1}: "))
        processes.append({'name': f'P{i+1}', 'AT': at, 'BT': bt})

    scheduled, gantt, timeline = fcfs(processes)
    display_table(scheduled)
    display_gantt(gantt, timeline)