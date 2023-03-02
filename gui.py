import functions
import PySimpleGUI as sg
import time

# sg.theme_previewer()
sg.theme('Dark Teal 4')
clock = sg.Text('', key='clock')

label = sg.Text("Enter a To-do")
input_area = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_area = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Exit("Exit")

cancel_button = sg.Button("Cancel")

window = sg.Window(
    "To Do",
    layout=[[clock],
            [label],
            [input_area, add_button, cancel_button],
            [list_area, edit_button, complete_button],
            [exit_button],
            ],
    font=("Helvetica", 20),
)
while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime('%A, %B %d,%G %r'))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todo"].update(value="")
            window["todos"].update(values=todos)
        case "Edit":
            try:
                edit_todo = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                complete_todo = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Cancel":
            todos = functions.get_todos()
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        # allows closure of gui
        case sg.WIN_CLOSED:
            break
window.close()
