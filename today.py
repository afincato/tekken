path = 'arachne.todo.txt'
todo_file = open(path, 'r')

# print(todo_file.readlines())

title = '# Today \n'

todos = todo_file.read()

today_path = 'today.todo.txt'
today = open(today_path, 'w')

today.write(title)
print(title)

today.write(todos)
print(todos)

todo_file.close()
today.close()
