found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False
print(found)

line = "Fouded"
for i in "abcdefghijk":
    if i == "w":
        line = True
        break
else:
    line = False
print(line, i)