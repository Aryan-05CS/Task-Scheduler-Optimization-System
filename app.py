import streamlit as st
import pandas as pd

from src.scheduler import optimize_schedule
from src.analytics import show_all_analytics

st.set_page_config(
    page_title="Task Scheduler Optimization System",
    layout="wide"
)

st.title("📅 Task Scheduler Optimization System")

st.sidebar.title("DSA Concepts")

st.sidebar.info(
    """
    • Greedy Algorithm

    • Heap / Priority Queue

    • Sorting

    • Scheduling Optimization

    Time Complexity:
    O(n log n)
    """
)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.header("➕ Add Task")

col1, col2 = st.columns(2)

with col1:

    task_name = st.text_input(
        "Task Name"
    )

    priority = st.number_input(
        "Priority",
        min_value=1,
        max_value=10,
        value=5
    )

with col2:

    deadline = st.number_input(
        "Deadline",
        min_value=1,
        value=1
    )

    execution_time = st.number_input(
        "Execution Time",
        min_value=1,
        value=1
    )

profit = st.number_input(
    "Profit",
    min_value=1,
    value=100
)

if st.button("Add Task"):

    if task_name.strip() == "":
        st.error("Enter task name")

    else:

        st.session_state.tasks.append(
            {
                "Task": task_name,
                "Priority": priority,
                "Deadline": deadline,
                "Execution Time": execution_time,
                "Profit": profit
            }
        )

        st.success("Task Added")

tasks_df = pd.DataFrame(
    st.session_state.tasks
)

st.header("📋 Current Tasks")

if not tasks_df.empty:

    st.dataframe(
        tasks_df,
        use_container_width=True
    )

else:

    st.info("No tasks added yet.")

col1, col2 = st.columns(2)

with col1:

    if st.button("Load Sample Tasks"):

        st.session_state.tasks = [
            {
                "Task": "Project",
                "Priority": 10,
                "Deadline": 4,
                "Execution Time": 2,
                "Profit": 300
            },
            {
                "Task": "Assignment",
                "Priority": 8,
                "Deadline": 2,
                "Execution Time": 1,
                "Profit": 100
            },
            {
                "Task": "Research",
                "Priority": 9,
                "Deadline": 6,
                "Execution Time": 2,
                "Profit": 250
            },
            {
                "Task": "Email",
                "Priority": 2,
                "Deadline": 3,
                "Execution Time": 1,
                "Profit": 20
            }
        ]

        st.rerun()

with col2:

    if st.button("Clear Tasks"):

        st.session_state.tasks = []

        st.rerun()

st.divider()

if st.button("🚀 Optimize Schedule"):

    if tasks_df.empty:

        st.warning("Add tasks first.")

    else:

        schedule_df, missed_df, total_profit = optimize_schedule(
            tasks_df
        )

        st.header("✅ Optimized Schedule")

        st.dataframe(
            schedule_df,
            use_container_width=True
        )

        st.header("❌ Missed Tasks")

        st.dataframe(
            missed_df,
            use_container_width=True
        )

        st.metric(
            "💰 Total Profit",
            total_profit
        )

        st.divider()

        show_all_analytics(
            tasks_df,
            schedule_df,
            missed_df,
            total_profit
        )

        csv = schedule_df.to_csv(
            index=False
        )

        st.download_button(
            label="⬇ Download Optimized Schedule",
            data=csv,
            file_name="optimized_schedule.csv",
            mime="text/csv"
        )

with st.expander("Algorithm Details"):

    st.write(
        "Sorting Complexity: O(n log n)"
    )

    st.write(
        "Heap Operations: O(n log n)"
    )

    st.write(
        "Overall Complexity: O(n log n)"
    )