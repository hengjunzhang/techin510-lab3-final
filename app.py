import sqlite3
import streamlit as st
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TaskState(str, Enum):
    planned = "planned"
    in_progress = "in-progress"
    done = "done"

class Task(BaseModel):
    name: str
    description: str
    state: TaskState
    created_at: datetime
    created_by: str
    category: str


conn = sqlite3.connect('tasks.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            state TEXT,
            created_at TEXT,
            created_by TEXT,
            category TEXT
        )
    ''')
    conn.commit()

create_table()

def insert_task(task_data):
    c.execute('''
        INSERT INTO tasks (name, description, state, created_at, created_by, category)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (task_data.name, task_data.description, task_data.state, 
          task_data.created_at.strftime("%Y-%m-%d %H:%M:%S"), 
          task_data.created_by, task_data.category))
    conn.commit()

def update_task_state(id, new_state):
    c.execute('UPDATE tasks SET state = ? WHERE id = ?', (new_state, id))
    conn.commit()

def delete_task(id):
    c.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()

def list_tasks(query="", category_filter="All"):
    query = f"%{query}%"
    if category_filter == "All":
        return c.execute('SELECT * FROM tasks WHERE name LIKE ? OR description LIKE ?', (query, query)).fetchall()
    else:
        return c.execute('SELECT * FROM tasks WHERE (name LIKE ? OR description LIKE ?) AND category = ?', (query, query, category_filter)).fetchall()

def task_form():
    with st.form(key='task_form'):
        name = st.text_input('Name')
        description = st.text_area('Description')
        state = st.selectbox('State', [s.value for s in TaskState])
        created_at_date = st.date_input('Created at', datetime.now())
        created_by = st.text_input('Created by')
        category = st.selectbox('Category', ['school', 'work', 'personal'])
        submitted = st.form_submit_button('Submit')

        if submitted:
            # 转换日期为 datetime 类型
            created_at_datetime = datetime.combine(created_at_date, datetime.min.time())
            return Task(
                name=name, description=description, state=state, 
                created_at=created_at_datetime, created_by=created_by, category=category
            )

task_data = task_form()
if task_data:
    insert_task(task_data)
    st.success("Task added successfully!")

search_query = st.sidebar.text_input("Search tasks")
category_filter = st.sidebar.selectbox("Filter by category", ["All", "school", "work", "personal"])

st.write("Tasks:")
tasks = list_tasks(search_query, category_filter)
for task in tasks:
    st.write(f"Name: {task[1]}, Description: {task[2]}, State: {task[3]}, Created at: {task[4]}, Created by: {task[5]}, Category: {task[6]}")
    if st.button("Mark as Done", key=f"done{task[0]}"):
        update_task_state(task[0], "done")
    if st.button("Delete", key=f"delete{task[0]}"):
        delete_task(task[0])
        st.experimental_rerun()
