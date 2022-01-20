list1 = ['python', 23, 'eags', 99, 5, 'spam', 'air', 2]
words = []
digits = []

for el in list1:
    if isinstance(el, int):
        digits.append(el)
    else:
        words.append(el)
words = sorted(words, key=len)
digits.sort()

file = open('test_hw.txt', 'w')
for el in words:
    file.write(el + '\n')
for el in digits:
    file.write(str(el) + '\n')

print('tratata')
