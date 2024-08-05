import time
from functions import get_todos, write_todos

now = time.strftime("%d/%m/%Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # ---Removing \n from each string item in list
        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        # ---List comprehensions
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new ToDo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Use number after 'edit' !")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos(todos)

            message = f"ToDo {todo_to_remove.strip("\n").capitalize()} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Your command is not valid. Use number after 'complete' !")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("Bye!")
