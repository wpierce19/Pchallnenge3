from pathlib import Path
#Wyatt Pierce
# Programming CHallenge 3


#Provided a way to find the current path of the .py file
# allows it to work on any computer and no matter where the file is
file_input = input("Please enter file name: ")
f = Path(__file__).with_name(file_input)
txt_open = f.open('r')
text = txt_open.read()

#Removes all Punctuation and converts to lower case
punct = '''!()-[];:'"\,<>./?@#$%^&*_~'''

for z in text:
    if z in punct:
        text = text.replace(z, "")

text = text.lower()

counts = {}
words = text.split()

# Checking if the word is in the dictionary already
# If not it will add it / but if it is then it will ad +1 to its key
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1


# Seperates the keys and values into 2 different lists
values = []
keys = []
for key,value in counts.items():
    values.append(counts[key])
    keys.append(key)

values.sort()
values.reverse()

new = {}


# finds the correct key that matches the given value from the list values
# then adds them to a new dictionary
for x in values:
    for key,value in counts.items():
        if value == x:
            new[key] = value

print("The most frequent words in descending frequency: ")

t_count = 0
for k,v in new.items():
    if t_count != 10:
        print(f"{k:<15} {':':<10}{v}")
        t_count += 1
