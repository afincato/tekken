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
  date_title = date_today + '\n----------\n\n'

  header = title + date_title
  print(header)

  # ---

  for file in set(glob.glob('*todo.txt')) - set(glob.glob('today.todo.txt')):

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

      due_today = []
      for ls in section:

        for item in ls:

          #-- due tasks
          if '@due' in item and '##' in ls[0]:

            #-- date
            itemdate = item[-13:]
            itemdate = itemdate[1:-2]
            itemdate = datetime.datetime.strptime(itemdate, '%d-%m-%Y').date()
            item_dttoday = datetime.date.today()

            #-- due today
            if itemdate == item_dttoday and '- [ ]' in item:
              # section
              if '@due' in ls[0]:
                scdue = ls[0].find('@due')
                sc = ls[0][3:scdue].strip()
              elif ls[0].endswith('*\n'):
                sc = ls[0][3:-3]
              else:
                sc = ls[0][3:-1]

              # task
              tk = item[:5] + ' ' + sc + ':' + item[5:]
              atdue = tk.find('@due')
              tk = tk[:atdue] + '\n'
              due_today.append(tk)

            #-- overdue
            elif itemdate < item_dttoday and '- [ ]' in item:
              # section
              if '@due' in ls[0]:
                scdue = ls[0].find('@due')
                sc = ls[0][3:scdue].strip()
              elif ls[0].endswith('*\n'):
                sc = ls[0][3:-3]
              else:
                sc = ls[0][3:-1]

              # task w/ overdue date
              tk = item[:5] + ' ' + sc + ':' + item[5:]
              due_today.append(tk)

          #-- starred task
          elif item.endswith(('*', '*\n')) and '- [ ]' in item:
            # section
            if '@due' in ls[0]:
              scdue = ls[0].find('@due')
              sc = ls[0][3:scdue].strip()

            elif ls[0].endswith('*\n'):
              sc = ls[0][3:-3]
            else:
              sc = ls[0][3:-1]

            tk = item[:5] + ' ' + sc + ':' + item[5:]
            due_today.append(tk)

      #-- title w/ @due and tags
      if len(due_today) > 0:
        due_today.insert(0, '#' + project[0] + '\n')

      #-- print today list
      for line in due_today:
        print(line)

      #-- write today list to file
      with open('today.todo.txt', 'w') as f:
        f.write(header)

        for line in due_today:
          f.write(str(line))


      # task done `- [x]`
      # item_done = []
      # if item.endswith(('*', '*\n')) and '- [x]' in item:
      #   item_done.append(item)

      # # add done tasks to `due_today`
      # if len(item_done) > 0:
      #   due_today.extend(item_done)


# ------
if __name__ == "__main__":
    today_list()
