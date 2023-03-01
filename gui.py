import functions
import PySimpleGUI as sg

label = sg.Text("Enter a To-do")
input_area = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button("Add")
list_area = sg.Listbox(values=functions.get_todos(),
                       key='list_todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window('To Do',
                   layout=[[label], [input_area, add_button], [list_area, edit_button]],
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
            window['list_todos'].update(values=todos)
        case "Edit":
            edit_todo = values['list_todos'][0]
            update_todo = values['todo'] + '\n'
            print(edit_todo[0])
            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = update_todo
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
            # allows closure of gui

        case 'list_todos':
            window['todo'].update(value=values['list_todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
