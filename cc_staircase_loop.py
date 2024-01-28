stars = ""
for i in range(0, 5, 1): 
    for j in range(0, i, 1):
        stars += "*"
        print (i, j)
    print(stars)

# i = 0; stars = ""
# i = 1; j = 0; stars = "*"
# i = 2; j = 0, 1; stars = "***"      
# i = 3; j = 0, 1, 2; stars = "******"
# i = 4; j = 0, 1, 2, 3; stars = "**********"