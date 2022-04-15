import re
import os

list_files = os.listdir()
print(list_files)
for fname in list_files:
    if not fname.endswith('.md') or not fname.startswith('2022-04-15'):
        continue
    contents = ""

    with open(fname, 'r') as f:
        
        while True:
            line = f.readline()
            
            if not line:
                break
            x = re.search("\$\$.*\$\$", line)
            if x:
                o = re.sub("\$\$", "\[[ ", x.string, 1)
                o = re.sub("\$\$", " \]]", o, 1)
                line = o
                
            contents += line
            
    with open(fname, 'w') as f:
        f.write(contents)
