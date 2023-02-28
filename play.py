import array

lines = []
skey = 'Heliene'

me = ""
contato = ""

with open("chat.txt", "r", encoding="utf8") as f:
    for row in f:
        b = row.split(': ')
        key = b[0].split('-')[1].strip()
        if key == skey:
            contato = contato +" "+ b[1].strip()
            if(me != ""):
                lines.append(me.strip().lower())
                me = "" 
        else:
            me = me +" "+ b[1].strip()
            if(contato != ""):
                lines.append(contato.strip().lower())
                contato = ""
            
        # break
        # lines.append()

print(lines)
