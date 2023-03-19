from pathlib import Path
#Wyatt Pierce
# Programming CHallenge 3

f = Path(__file__).with_name('text.txt')
txt_open = f.open('r')
text = txt_open.read()

counts = {}
words = text.split()

# Checking if the word is in the dictionary already
# If not it will add it / but if it is then it will ad +1 to its key
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

values = []
keys = []
for key,value in counts.items():
    values.append(counts[key])
    keys.append(key)

values.sort()
values.reverse()
print(values)







