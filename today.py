import os
import glob
import datetime

dest_path = 'today.todo.txt'
today_todo = open(dest_path, 'w')

title = '# Today \n'
today_todo.write(title)

date_today = datetime.date.today()
date_today = date_today.strftime('%d-%m-%Y')

for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):
  print(file)
  with open(file) as fp:
    project = fp.readlines()
    project_title = '\n#' + project[0] + ' \n'
    today_todo.write(project_title)

    for item in project:
      if '@due' in item:
        if date_today in item:
          today_todo.write(item)
          print(item)


fp.close()
today_todo.close()
