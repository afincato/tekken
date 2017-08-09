import os
import glob
import datetime
import re

def today_list():
  # --- read from each project.todo

  # title
  title = 'Today \n'

  # date
  date_today = datetime.date.today()
  date_today = date_today.strftime('%d-%m-%Y')
  date_title = date_today + '\n----------\n\n'

  header = title + date_title
  print(header)

  # ---

  for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):

    with open(file) as fp:
      project = fp.readlines()
      # print(project)
     
      # project.todo
     
      # split list into smaller lists 
      # by section '##'
      def group(seq, sep):
        g = []
        for el in seq:
          if sep in el:
            yield g
            g = []
          g.append(el)
        yield g

      section = list(group(project, '##'))

      due_today = []
      for ls in section:
        for item in ls:
          if date_today in item and '##' in ls[0]:
            if '- [ ]' in item:
              # section
              sc = ls[0][3:-1]
              tk = item[:5] + ' ' + sc + ':' + item[5:]
              # task
              due_today.append(tk)
      
      if len(due_today) > 0:
        # title w/ @due and tags
        due_today.insert(0, '#' + project[0] + '\n')
      
      for line in due_today:
        print(line)
      
      with open('today.todo.txt', 'w') as f:
        f.write(header)

        for line in due_today:
          f.write(str(line))

      # tasks_due = [item for item in project
      #              if date_today in item
      #              if '- [ ]' in item]
      
      # tasks_done = [item for item in project
      #               if date_today in item
      #               if '- [x]' in item]

      # merge two lists and put done tasks at the end
      # items = tasks_due + tasks_done
      # print(''.join(str(item) for item in due))

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
if __name__ == "__main__":
    today_list()
