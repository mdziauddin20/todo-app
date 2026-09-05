while True:
    user_action=input("type add,show,edit,complete or exit:")
    match user_action:
        case "add":
            todo=input("enter a todo:") + "\n"
            # we can also write like this
            with open("todos.txt",'r') as file:
                todos = file.readlines()
           # file = open("todos.txt", 'r')
           #  todos=file.readlines()
            #file.close()
            todos.append(todo)
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file= open("todos.txt","r")
            todos=file.readlines()
            file.close()

            #new_todo =[item.stript('\n') for item in todos]

            for index, item in enumerate (todos):
                item = item.strip('\n')
                row=f"{index+1}-{item}"
                print(row)
        case 'edit':
            number=int(input("number of the todo to edit:"))
            number=number-1

            with open("todos.txt",'r') as file:
                todos = file.readlines()
               
            new_todo=input("enter a todo:")
            todos[number]= new_todo+'\n'
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'complete':
            number=int(input("number of the todo to complete"))
            with open('todos.txt','r') as file:
                todos = file.readlines()
            index = number-1    
            todo_to_remove = todos[index]
            todos.pop(number-1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
            
            message =f" todo {todo_to_remove} was removed from the list"   
            print(message)
        case'exit':
            break
print('bye')


