import os
import glob
import datetime
import re

# --- read from each project.todo
# --- && write a comprehensive list to today.todo

date_today = datetime.date.today()
date_today = date_today.strftime('%d-%m-%Y')
date_title = date_today + '\n----------\n'

for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):
  
  with open(file) as fp:
    project = fp.readlines()
    # print(project)

    print('\n' + project[0])

    tasks_due = [item for item in project
                 if date_today in item
                 if '- [ ]' in item]
    
    tasks_done = [item for item in project
                  if date_today in item
                  if '- [x]' in item]

    # todo: add `~~item~~` right after `- [x]` &&
    #       before any `@due(dd-mm-yyyy)`

    # merge two lists and put done tasks at the end
    items = tasks_due + tasks_done
    print('\n'.join(str(item) for item in items))


# --- write all projects to today.todo
# with open('today.todo.txt', 'w') as tf:

#   title = '# Today\n\n'
#   tf.write(title)
#   print(title)
  
#   tf.write(date_title)
#   print(date_title)


#   # project title
#   project_title = '\n#' + project[0] + ' \n'
#   tf.write(project_title)

#   tf.write('\n'.join(str(item) for item in items))
#   for item in items:
#     print(item)

# ------
# if __name__ = "__main__":
