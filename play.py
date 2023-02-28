import array

lines = array.array('s',[])

with open("chat.txt", "r", encoding="utf8") as f:
    for row in f:
        lines.append(row)

print(lines)
