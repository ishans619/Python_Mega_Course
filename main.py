
while True:
    # get user input and strip space characters from it
    user_action = input("type add,exit,edit,complete or show: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ") + "\n"

            with open('todos.txt','r') as file:
                todos = file.readlines()


            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt','r') as file:
                todos = file.readlines()

            for index,item in enumerate(todos):
                item = item.strip()
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("enter the number of todo to edit: "))
            number = number - 1

            with open('todos.txt','r') as file:
                todos = file.readlines()

            new_todo = input("enter the new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt','w') as file:
               file.writelines(todos)

        case 'complete':
            number = int(input("enter the completed todo: "))

            with open('todos.txt','r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w') as file:
               file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
















