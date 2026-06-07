import heapq
import pandas as pd


def optimize_schedule(tasks_df):
    """
    Optimize task scheduling using:
    - Greedy Algorithm
    - Min Heap (Profit-Based)
    """

    if tasks_df.empty:
        return pd.DataFrame(), pd.DataFrame(), 0

    tasks = tasks_df.sort_values(
        by="Deadline"
    ).to_dict("records")

    heap = []

    current_time = 0

    task_map = {}

    for task in tasks:

        current_time += task["Execution Time"]

        heapq.heappush(
            heap,
            (
                task["Profit"],
                task
            )
        )

        task_map[task["Task"]] = task

        if current_time > task["Deadline"]:

            removed_profit, removed_task = heapq.heappop(heap)

            current_time -= removed_task["Execution Time"]

    selected_tasks = []

    for profit, task in heap:
        selected_tasks.append(task)

    selected_tasks.sort(
        key=lambda x: x["Deadline"]
    )

    scheduled_names = {
        task["Task"]
        for task in selected_tasks
    }

    missed_tasks = []

    for task in tasks:

        if task["Task"] not in scheduled_names:
            missed_tasks.append(task)

    timeline = []

    start_time = 0

    total_profit = 0

    for task in selected_tasks:

        end_time = (
            start_time
            + task["Execution Time"]
        )

        timeline.append(
            {
                "Task": task["Task"],
                "Start": start_time,
                "End": end_time,
                "Deadline": task["Deadline"],
                "Execution Time": task["Execution Time"],
                "Priority": task["Priority"],
                "Profit": task["Profit"]
            }
        )

        total_profit += task["Profit"]

        start_time = end_time

    schedule_df = pd.DataFrame(timeline)

    missed_df = pd.DataFrame(missed_tasks)

    return (
        schedule_df,
        missed_df,
        total_profit
    )