# f = open("C:\\Users\\tliu\\Data\\APDS\\v1.2\\Sprint8\\October\\4.txt")
# content = f.readlines()
# lista = []
# for i in content:
#     # print i
#     a = i.split()
#     lista.append(a)
#     # print a
# # print lista
# b = [];
# for j in lista:
#     if j not in b:
#         b.append(j)
# # print b

# for i in b:
#     # if len(i) != 2:
#     #     print i


#     print i[0] + " " + i[1] + ";"

f = open("C:\\Users\\tliu\\Data\\APDS\\v1.2\\Sprint8\\October\\2.txt")
content = f.read()
a = content.split("; ")
for i in a:
    print i
# APDS
