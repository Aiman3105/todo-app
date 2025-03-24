import streamlit as st
import functions

todos=functions.get_todos()
einkaufsliste=functions.get_todos(filepath="einkaufen.txt")

def add_todo():
    todo=st.session_state["new_todo"]
    if st.session_state["new_todo"] !="":
        todo=todo + "\n"
        if todo not in todos and todo not in einkaufsliste:
            todos.append(todo)
            functions.write_todos(todos)
            st.session_state["new_todo"]=""
        else:
            st.error("Das Todo existiert bereits!")

def add_einkaufen():
    einkaufen=st.session_state["new_einkaufen"]
    if st.session_state["new_einkaufen"] !="":
        einkaufen=einkaufen + "\n"
        if einkaufen not in einkaufsliste and einkaufen not in todos:
            einkaufsliste.append(einkaufen)
            functions.write_todos(einkaufsliste, filepath="einkaufen.txt")
            st.session_state["new_einkaufen"]=""
        else:
            st.error("Das Produkt existiert bereits!")



st.title("My ToDO App")
st.subheader("Todos:")
for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new ToDo..",
              on_change=add_todo, key="new_todo")


st.subheader("Einkaufen:")
for index, einkaufen in enumerate(einkaufsliste):
    checkbox=st.checkbox(einkaufen, key=einkaufen)
    if checkbox:
        einkaufsliste.pop(index)
        functions.write_todos(einkaufsliste, filepath="einkaufen.txt")
        del st.session_state[einkaufen]
        st.rerun()


st.text_input(label="", placeholder="Add a Product..",
              on_change=add_einkaufen, key="new_einkaufen")


st.session_state