import heapq
import csv
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int
    deadline: int
    execution_time: int
    profit: int

tasks = [
    Task("Assignment", 8, 2, 1, 100),
    Task("Project", 10, 4, 2, 300),
    Task("Presentation", 7, 3, 1, 150),
    Task("Email", 2, 5, 1, 20),
    Task("Research", 9, 6, 2, 250),
]

tasks.sort(key=lambda x: x.deadline)

heap = []
current_time = 0

for task in tasks:

    current_time += task.execution_time

    heapq.heappush(
        heap,
        (task.profit,
         task)
    )

    if current_time > task.deadline:

        removed = heapq.heappop(heap)

        current_time -= removed[1].execution_time

selected_tasks = [item[1] for item in heap]

selected_tasks.sort(key=lambda x: x.deadline)

timeline = []

time_marker = 0

total_profit = 0

for task in selected_tasks:

    start = time_marker
    end = start + task.execution_time

    timeline.append(
        [task.name,
         start,
         end,
         task.deadline,
         task.profit]
    )

    total_profit += task.profit
    time_marker = end

print("\nOPTIMIZED TASK SCHEDULE\n")

for item in timeline:

    print(
        f"{item[0]} | "
        f"Start:{item[1]} "
        f"End:{item[2]} "
        f"Deadline:{item[3]} "
        f"Profit:{item[4]}"
    )

print("\nTOTAL PROFIT:", total_profit)

with open(
    "schedule_report.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "Task",
            "Start",
            "End",
            "Deadline",
            "Profit"
        ]
    )

    writer.writerows(timeline)

print(
    "\nReport saved as schedule_report.csv"
)