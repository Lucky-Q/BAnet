f = open("item_name_T.txt", "w", encoding="utf-8")
n = 1
while n < 40000001:
    f.write("item"+str(n)+"\n")
    n = n+1
f.close()