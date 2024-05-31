import streamlit as st

st.title("Todo app")

st.header("Your Todo List")

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
    
def add_todo_item(todo_item):
        if todo_item:
            st.session_state.todo_list.append(todo_item)
            
def delete_todo_item(todo_item):
    if todo_item in st.session_state.todo_list:
        st.session_state.todo_list.remove(todo_item)
        
new_todo = st.text_input("add a todo item:")
if st.button("add"):
    add_todo_item(new_todo)
    st.experimental_rerun()
    
st.write("### todo list:")
if st.session_state.todo_list:
    for item in st.session_state.todo_list:
        st.write(f"-{item}",st.button(f"delete {item}", key=item, on_click=delete_todo_item, args=(item,)))
    else:
        st.write("no item")