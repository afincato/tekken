import os
import glob
import datetime
import re

def today_list():
  # --- read from each project.todo

  # title
  title = '# today.todo \n\n'

  # date
  date_today = datetime.date.today()
  date_today = date_today.strftime('%d-%m-%Y')
  date_title = date_today + '\n----------\n'

  header = title + date_title
  print(header)

  # ---
  due_today = []
  for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):

    due_today_prj = []
    with open(file) as fp:
      project = fp.readlines()

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

      for ls in section:
        for item in ls:

          #-- due tasks
          if '@due' in item and '##' in ls[0]:

            #-- date
            duemark = item.find('@due')
            itemdate = item[duemark:]
            itemdate = itemdate[5:-2]
            itemdate = datetime.datetime.strptime(itemdate, '%d-%m-%Y').date()
            item_dttoday = datetime.date.today()

            #-- due today
            if itemdate == item_dttoday and '- [ ]' in item:
              # section
              if '@due' in ls[0]:
                scdue = ls[0].find('@due')
                sc = ls[0][3:scdue].strip()
              elif ls[0].endswith(('*', '*\n')):
                sc = ls[0][3:-3]
              else:
                sc = ls[0][3:-1]

              # task
              tk = item[:5] + ' ' + sc + ':' + item[5:]
              atdue = tk.find('@due')
              tk = tk[:atdue] + '\n'
              if not ls[-1].endswith('\n'):
                ls[-1] = ls[-1] + '\n'
              due_today_prj.append(tk)

            #-- overdue
            elif itemdate < item_dttoday and '- [ ]' in item:
              # section
              if '@due' in ls[0]:
                scdue = ls[0].find('@due')
                sc = ls[0][3:scdue].strip()
              elif ls[0].endswith(('*', '*\n')):
                sc = ls[0][3:-3]
              else:
                sc = ls[0][3:-1]

              # task w/ overdue date
              tk = item[:5] + ' ' + sc + ':' + item[5:]
              if not ls[-1].endswith('\n'):
                ls[-1] = ls[-1] + '\n'
              due_today_prj.append(tk)

          #-- starred task
          elif item.endswith(('*', '*\n')) and '- [ ]' in item:
            # section
            if '@due' in ls[0]:
              scdue = ls[0].find('@due')
              sc = ls[0][3:scdue].strip()
            elif ls[0].endswith(('*', '*\n')):
              sc = ls[0][3:-3]
            else:
              sc = ls[0][3:-1]

            tk = item[:5] + ' ' + sc + ':' + item[5:]
            if not ls[-1].endswith('\n'):
              ls[-1]= ls[-1] + '\n'
            due_today_prj.append(tk)

      #-- title w/ @due and tags
      if len(due_today_prj) > 0:
        due_today_prj.insert(0, '\n#' + project[0] + '\n')

    #-- print today list
    # for line in due_today_prj:
      # print(line)

    #-- add each `due_today_prj` to `due_today`
    due_today.append(due_today_prj)

  print(due_today)

  #-- write today list to file
  with open('today.todo.txt', 'w') as f:
    f.write(header)

    for due_today_prj in due_today:
      for line in due_today_prj:
        f.write(line)

# ------
if __name__ == "__main__":
    today_list()
