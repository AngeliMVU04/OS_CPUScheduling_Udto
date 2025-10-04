def sjf(processes):
    time = 0
    completed = []
    gantt_chart = []
    timeline = [0]

    while processes:
        available = [p for p in processes if p['AT'] <= time]
        if not available:
            time += 1
            continue
        shortest = min(available, key=lambda x: x['BT'])
        processes.remove(shortest)
        if time < shortest['AT']:
            time = shortest['AT']
        shortest['CT'] = time + shortest['BT']
        shortest['TAT'] = shortest['CT'] - shortest['AT']
        shortest['WT'] = shortest['TAT'] - shortest['BT']
        time = shortest['CT']
        completed.append(shortest)
        gantt_chart.append(shortest['name'])
        timeline.append(time)

    return completed, gantt_chart, timeline

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
    print("\nGantt Chart (SJF):")
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

    scheduled, gantt, timeline = sjf(processes)
    display_table(scheduled)
    display_gantt(gantt, timeline)