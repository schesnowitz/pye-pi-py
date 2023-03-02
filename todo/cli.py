# from functions import list_todos, get_todos, write_todos
import functions
import time

date_time = time.strftime('%A, %B %d,%G %r')

print(date_time)

while True:
    user_action = input("Enter Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip().lower()
    if user_action.startswith('add'):
        # gets user input
        todo = user_action[4:]  # slice the "add " from input
        todo = todo.strip().lower().capitalize() + "\n"
        if len(todo) < 4:
            print("This todo is not valid-- Must be 4 characters long")
        else:
            # opens and reads the file
            todos = functions.get_todos()

            todos.append(todo)

            # recreates file with new items --  writes file
            functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # print function
        functions.list_todos(todos)

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            functions.list_todos(todos)

            number = int(input("number of the todo you want to edit? "))

            number = number - 1
            edit_todo = todos[number]
            print(edit_todo)
            replace_todo = input("Edit: ")
            replace_todo = replace_todo.strip().lower().capitalize()
            todos[number] = replace_todo + '\n'

            functions.write_todos(todos)

        except (ValueError, IndexError):
            print("there was an error")
            continue
    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            # print function
            functions.list_todos(todos)

            number = int(input("number of the todo you want to remove? "))
            number = number - 1
            remove_todo = todos[number]
            remove_todo = todos.pop(number)

            functions.write_todos(todos)

            print(f"{remove_todo} has been removed from the list.")
        except (ValueError, IndexError) as e:
            print(f'There was an error {e}')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("I don't understand that command")

print("Program has stopped")
