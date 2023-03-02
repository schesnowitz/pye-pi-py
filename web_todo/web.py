import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("To Do App")
st.subheader("this is a sub header")
st.write("this is some regular text")
st.code("this is a code box markdown deal")
for todo in todos:
    st.checkbox(todo)

st.text_input(label='some label', label_visibility="hidden",
              placeholder="Enter ToDo", on_change=add_todo,
              key='new_todo')

st.session_state
