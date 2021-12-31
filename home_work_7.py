#ex1
# string = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
# splt = string.split(' ')
# maxx = len(splt[0])
# res = splt[0]
# for i in range(len(splt)):
#     if len(splt[i]) > maxx:
#         maxx = len(splt[i])
#         res = splt[i]
# print(res)

#ex2
string = 'Lorem Ipsum? is simply dummy text of the printing, and typesetting industry!'
new_string = ''
for i in string:
    if i.isalpha():
        new_string += i
    if i == ' ':
        new_string += i
print(new_string.split(' '))