import functions
import PySimpleGUI as sg

label = sg.Text("Enter a To-do")
input_area = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button("Add")

window = sg.Window('To Do',
                   layout=[[label], [input_area, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            # allows closure of gui
        case sg.WIN_CLOSED:
            break
window.close()
