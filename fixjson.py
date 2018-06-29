import re
file = open("gervsmex.json", "r+")
lines = ['{"tweets" : [']

for idx, line in enumerate(file):
    newLine = re.sub("}\r\n","},",line)
    lines.extend([newLine])
lines.extend("]}")
fileout = open("fixedjson.json", "w+")
lst = map(str, lines)  
# Join the items together with commas                   
line = "".join(lst)
# Write to the file
fileout.write(line)