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
        if ls[0].endswith('*\n') or date_today in ls[0]:
          ls[0] = '#' + ls[0]
          for item in ls:
            due_today.append(item)

        for item in ls:
          # if item.endswith('*\n') or date_today in item and '##' in ls[0]:
          #   if '- [ ]' in item:
          #     # section
          #     sc = ls[0][3:-1]
          #     # task
          #     tk = item[:5] + ' ' + sc + ':' + item[5:]
          #     atdue = tk.find('@due')
          #     tk = tk[:atdue] + '\n'
          #     due_today.append(tk)
          
          
          if '@due' in item and '##' in ls[0]:
            itemdate = item[-13:]
            itemdate = itemdate[1:-2]
            itemdate = datetime.datetime.strptime(itemdate, '%d-%m-%Y').date()

            item_dttoday = datetime.date.today()
            
            if itemdate == item_dttoday and '- [ ]' in item:
                # section
                sc = ls[0][3:-1]
                # task
                tk = item[:5] + ' ' + sc + ':' + item[5:]
                atdue = tk.find('@due')
                tk = tk[:atdue] + '\n'
                due_today.append(tk)
            
            # elif itemdate < item_dttoday:
            #   if '- [ ]' in item:
            #     # section
            #     sc = ls[0][3:-1]
            #     # task
            #     tk = item[:5] + ' ' + sc + ':' + item[5:]
            #     atdue = tk.find('@due')
            #     tk = tk[:atdue] + '\n'
            #     due_today.append(tk)


      if len(due_today) > 0:
        # title w/ @due and tags
        due_today.insert(0, '#' + project[0] + '\n')
      
      for line in due_today:
        print(line)
      
      with open('today.todo.txt', 'w') as f:
        f.write(header)

        for line in due_today:
          f.write(str(line))

# ------
if __name__ == "__main__":
    today_list()
