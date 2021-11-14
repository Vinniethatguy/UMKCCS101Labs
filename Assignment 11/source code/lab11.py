words = set()
count = {}
doc = ''
while True:
    try:
        doc = input("Enter the name of the file to open: ")
        file = open(doc,'r')
        file.close()
        break
    except:
        print("Could not open file", doc)
        print('Please Try again')



with open(doc,'r') as file:
    for line in file:
        fixed = [''.join([char for char in part if char.isalpha()]).lower() for part in line.split(' ') if len(''.join([char for char in part if char.isalpha()]).lower()) > 3]
        for word in fixed:
            if word in words:
                count[word] += 1
            elif word not in words:
                words.add(word)
                count[word] = 1

container = []
for key in count.keys():
    temp = (count[key], key)
    container.append(temp)
container.sort(reverse=True)

print("{:<12}{:>15}{:>20}".format('#', 'Word','Freq.'))
print('='*47)
count = 0
if len(words) < 11:
    count = len(words) + 1
else:
    count = 11

for num in range(1,count):
    print("{:<12}{:>15}{:>20}".format(num, container[num - 1][1], container[num - 1][0]))

oneValues = 0
container.sort()
for x in container:
    if x[0] == 1:
        oneValues += 1

print('\nThere are', oneValues,'That occur only once')
print('There are', len(words), 'unique words in the document')