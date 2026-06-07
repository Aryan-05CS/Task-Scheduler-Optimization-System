# 📅 Task Scheduler Optimization System

## 🚀 Project Overview

The Task Scheduler Optimization System is a Data Structures and Algorithms (DSA) project that optimizes task execution based on deadlines, priorities, execution times, and profit values.

The system uses a combination of **Greedy Algorithms**, **Sorting**, and **Heap-based Priority Queues** to maximize total profit while minimizing missed deadlines.

An interactive Streamlit dashboard provides task management, schedule visualization, analytics, and report generation.

---

## 🎯 Problem Statement

In real-world systems, tasks often have:

* Different priorities
* Deadlines
* Execution durations
* Importance or profit values

Executing tasks in random order may result in:

* Missed deadlines
* Reduced productivity
* Loss of valuable opportunities

This project solves the problem by generating an optimized execution schedule.

---

## ✨ Features

* Add and manage tasks dynamically
* Deadline-aware scheduling
* Heap-based Priority Queue implementation
* Greedy scheduling optimization
* Missed task detection
* Profit maximization
* Interactive Streamlit dashboard
* Analytics and visualizations
* Resource utilization tracking
* CSV export functionality
* Performance comparison dashboard

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries

* Pandas
* Plotly
* Heapq

---

## 📚 DSA Concepts Used

### Sorting

Tasks are sorted by deadlines.

Time Complexity:

O(n log n)

### Heap / Priority Queue

Used for efficient task selection.

Operations:

* Insert → O(log n)
* Delete → O(log n)
* Peek → O(1)

### Greedy Algorithm

Selects tasks that maximize total profit while satisfying scheduling constraints.

---

## 🏗️ System Workflow

Task Input
↓
Validation
↓
Deadline Sorting
↓
Priority Queue (Heap)
↓
Greedy Scheduling
↓
Optimized Task Order
↓
Timeline Generation
↓
Analytics Dashboard
↓
Report Generation

---

## 📂 Project Structure

Task-Scheduler-Optimization-System/

├── app.py

├── requirements.txt

├── README.md

├── src/

│ ├── scheduler.py

│ └── analytics.py

├── data/

├── outputs/

├── images/

└── docs/

---

## 📊 Analytics Dashboard

The dashboard includes:

* Total Tasks
* Scheduled Tasks
* Missed Tasks
* Total Profit
* Completion Percentage
* Profit Analysis Chart
* Task Completion Pie Chart
* Deadline Distribution
* Priority Distribution
* Timeline (Gantt Chart)
* Resource Utilization
* Before vs After Optimization Comparison

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Task-Scheduler-Optimization-System.git

cd Task-Scheduler-Optimization-System
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
streamlit run app.py
```

---

## 📝 Sample Tasks

| Task                   | Priority | Deadline | Execution Time | Profit |
| ---------------------- | -------- | -------- | -------------- | ------ |
| DSA Project            | 10       | 4        | 2              | 300    |
| Internship Application | 10       | 3        | 1              | 280    |
| Research Paper         | 8        | 5        | 2              | 250    |
| Coding Practice        | 9        | 6        | 2              | 220    |
| Bug Fixing             | 9        | 4        | 1              | 200    |

---

## 📈 Expected Output

### Optimized Schedule

| Task                   | Start | End | Profit |
| ---------------------- | ----- | --- | ------ |
| Internship Application | 0     | 1   | 280    |
| DSA Project            | 1     | 3   | 300    |
| Bug Fixing             | 3     | 4   | 200    |
| Research Paper         | 4     | 6   | 250    |

### Metrics

* Total Profit
* Completed Tasks
* Missed Tasks
* Resource Utilization

---

## 📷 Screenshots

### Dashboard

Add screenshot here:

images/dashboard_home.png

### Task List

Add screenshot here:

images/tasks_loaded.png

### Optimized Schedule

Add screenshot here:

images/optimized_schedule.png

### Analytics Dashboard

Add screenshot here:

images/analytics_kpi.png

### Timeline Chart

Add screenshot here:

images/timeline_chart.png

---

## 🔍 Time Complexity Analysis

### Sorting

O(n log n)

### Heap Operations

O(n log n)

### Overall Complexity

O(n log n)

---

## 🌍 Real-World Applications

* CPU Scheduling
* Cloud Computing Job Scheduling
* Project Management Systems
* Workflow Automation
* Resource Allocation Systems
* Manufacturing Scheduling
* Task Management Platforms

---

## 🚀 Future Enhancements

* User Authentication
* Database Integration
* Multi-user Scheduling
* Real-time Collaboration
* AI-based Priority Prediction
* Task Dependency Management
* Email Notifications
* REST API Integration

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Greedy Algorithms
* Heap Data Structure
* Priority Queues
* Scheduling Optimization
* Time Complexity Analysis
* Data Visualization
* Streamlit Development
* Software Engineering Practices
* GitHub Project Documentation

---

## 👨‍💻 Author

Aryan Choughule

Engineering Student | DSA Enthusiast | Aspiring Cybersecurity & Software Developer

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
