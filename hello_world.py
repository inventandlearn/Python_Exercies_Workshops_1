print("Hello World!")

stars = ""
for i in range(5): 
    for j in range(i):
        stars += "*"
        print (i, j)
    print(i)
    print(stars)
