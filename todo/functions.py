FILEPATH = "./todos.txt"


def list_todos(todos):
    """displays the todos"""
    for index, item in enumerate(todos):
        index = index + 1
        print(index, f". ", item, sep="", end="")


def get_todos(filepath=FILEPATH):
    """ reads the list of todos from a text file"""
    with open(filepath, "r") as x_doc_local:
        todos_local = x_doc_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ writes the list of todos to the text file"""
    with open(filepath, "w") as x_doc_local:
        x_doc_local.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos())
