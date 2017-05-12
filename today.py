import re
import datetime

source_path = 'arachne.todo.txt'
todo_file = open(source_path, 'r')
todos = todo_file.readlines()

dest_path = 'today.todo.txt'
today_todo = open(dest_path, 'w')

title = '# Today \n\n'
today_todo.write(title)

date_today = datetime.date.today()
date_today = date_today.strftime('%Y-%m-%d')

project_title = '#' + todos[0] + ' \n'
today_todo.write(project_title)

for item in todos:
  if '@due' in item:
    if date_today in item:
      today_todo.write(item)


todo_file.close()
today_todo.close()
