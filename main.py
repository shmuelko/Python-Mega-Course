user_text = "Enter a todo: "
todos = []
while 1:
    prompt = input(user_text)
    if prompt == "exit":
        break
    else:
        todos.append(prompt)

print(todos)
