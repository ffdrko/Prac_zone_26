user_prompt = "Enter a todo: "

todo_list = []

while True:
    todo_item = input(user_prompt)
    todo_list.append(todo_item.capitalize())
    print(todo_list)