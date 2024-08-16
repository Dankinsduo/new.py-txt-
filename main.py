files = ['1.py', '2.py', '3.py']
list_1 = []

for file in files:
  with open (file, 'r', encoding = 'UTF-8') as f: 
    lines = f.readlines()
    list_1.extend([file, str(len(lines)), lines])
    
  with open('new.py', 'w', encoding='UTF-8') as f:
    for lst in list_1:
      f.write(''.join(lst) + '\n')
