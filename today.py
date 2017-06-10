import os
import glob
import datetime

dest_path = 'today.todo.txt'
today_todo = open(dest_path, 'w')

date_today = datetime.date.today()
date_today = date_today.strftime('%d-%m-%Y')
date_title = date_today + '\n----------\n'

title = '# Today\n\n'
today_todo.write(title)
print title
today_todo.write(date_title)
print date_title

for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):
  with open(file) as fp:
    project = fp.readlines()
    project_title = '\n#' + project[0] + ' \n'
    today_todo.write(project_title)
    print project_title

    for item in project:
      if date_today in item:
        if '- [ ]' in item:
          today_todo.write(item)
          print item

fp.close()
today_todo.close()
