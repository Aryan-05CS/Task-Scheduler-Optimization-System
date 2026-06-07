import pandas as pd
import plotly.express as px
import streamlit as st


def show_kpis(total_tasks, scheduled_tasks, missed_tasks, total_profit):
    """
    Display KPI Cards
    """

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (scheduled_tasks / total_tasks) * 100, 2
        )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Tasks", total_tasks)
    col2.metric("Scheduled", scheduled_tasks)
    col3.metric("Missed", missed_tasks)
    col4.metric("Profit", total_profit)
    col5.metric("Completion %", f"{completion_rate}%")



def profit_chart(schedule_df):
    """
    Profit Per Task
    """

    if schedule_df.empty:
        return

    st.subheader("📈 Profit Analysis")

    fig = px.bar(
        schedule_df,
        x="Task",
        y="Profit",
        title="Profit Per Task"
    )

    st.plotly_chart(fig, use_container_width=True)



def completion_pie_chart(completed, missed):
    """
    Completed vs Missed
    """

    st.subheader("🥧 Task Completion Status")

    status_df = pd.DataFrame(
        {
            "Status": ["Completed", "Missed"],
            "Count": [completed, missed]
        }
    )

    fig = px.pie(
        status_df,
        names="Status",
        values="Count",
        title="Completed vs Missed Tasks"
    )

    st.plotly_chart(fig, use_container_width=True)



def deadline_distribution(tasks_df):
    """
    Deadline Distribution
    """

    if tasks_df.empty:
        return

    st.subheader("📅 Deadline Distribution")

    fig = px.histogram(
        tasks_df,
        x="Deadline",
        nbins=10,
        title="Task Deadlines"
    )

    st.plotly_chart(fig, use_container_width=True)



def priority_distribution(tasks_df):
    """
    Priority Distribution
    """

    if tasks_df.empty:
        return

    st.subheader("⭐ Priority Distribution")

    fig = px.histogram(
        tasks_df,
        x="Priority",
        nbins=10,
        title="Task Priorities"
    )

    st.plotly_chart(fig, use_container_width=True)



def schedule_timeline(schedule_df):
    """
    Gantt Chart Timeline
    """

    if schedule_df.empty:
        return

    st.subheader("⏳ Schedule Timeline")

    timeline_df = schedule_df.copy()

    fig = px.timeline(
        timeline_df,
        x_start="Start",
        x_end="End",
        y="Task",
        color="Profit",
        title="Task Execution Timeline"
    )

    fig.update_yaxes(autorange="reversed")

    st.plotly_chart(fig, use_container_width=True)



def task_tables(completed_df, missed_df):
    """
    Completed and Missed Task Tables
    """

    st.subheader("✅ Scheduled Tasks")
    st.dataframe(
        completed_df,
        use_container_width=True
    )

    st.subheader("❌ Missed Tasks")
    st.dataframe(
        missed_df,
        use_container_width=True
    )



def utilization_meter(total_time_used, max_deadline):
    """
    Resource Utilization
    """

    if max_deadline == 0:
        return

    utilization = (
        total_time_used / max_deadline
    ) * 100

    st.subheader("⚙️ Resource Utilization")

    st.progress(
        min(utilization / 100, 1.0)
    )

    st.write(
        f"Utilization: {utilization:.2f}%"
    )



def before_after_comparison(
        before_profit,
        after_profit,
        before_missed,
        after_missed
):
    """
    Before vs After Optimization
    """

    st.subheader("📊 Before vs After Optimization")

    comparison_df = pd.DataFrame(
        {
            "Metric": [
                "Profit",
                "Missed Tasks"
            ],
            "Before": [
                before_profit,
                before_missed
            ],
            "After": [
                after_profit,
                after_missed
            ]
        }
    )

    st.dataframe(
        comparison_df,
        use_container_width=True
    )



def show_all_analytics(
        tasks_df,
        schedule_df,
        missed_df,
        total_profit
):
    """
    Main Analytics Dashboard
    """

    total_tasks = len(tasks_df)
    scheduled_tasks = len(schedule_df)
    missed_tasks = len(missed_df)

    show_kpis(
        total_tasks,
        scheduled_tasks,
        missed_tasks,
        total_profit
    )

    st.divider()

    profit_chart(schedule_df)

    completion_pie_chart(
        scheduled_tasks,
        missed_tasks
    )

    deadline_distribution(tasks_df)

    priority_distribution(tasks_df)

    schedule_timeline(schedule_df)

    task_tables(
        schedule_df,
        missed_df
    )

    total_time_used = (
        schedule_df["Execution Time"].sum()
        if not schedule_df.empty
        else 0
    )

    max_deadline = (
        tasks_df["Deadline"].max()
        if not tasks_df.empty
        else 0
    )

    utilization_meter(
        total_time_used,
        max_deadline
    )

    before_profit = (
        tasks_df["Profit"].sum()
        if not tasks_df.empty
        else 0
    )

    before_after_comparison(
        before_profit,
        total_profit,
        len(tasks_df) - len(schedule_df),
        missed_tasks
    )