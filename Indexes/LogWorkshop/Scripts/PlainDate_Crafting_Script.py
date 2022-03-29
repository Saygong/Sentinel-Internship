


file = open("PlainDate.txt", "w")




for i in range(1,32):
    date = "2021-12-"+ str(i) +" "
    for j in range(24):
        time = str(j) + ":00:00.0000"
        file.write(date + time + "\n")
    
for i in range(1,32):
    date = "2022-01-" + str(i) +" "
    for j in range(24):
        time = str(j) + ":00:00.0000"
        file.write(date + time + "\n")

for i in range(1,29):
    date = "2022-02-" + str(i) +" "
    for j in range(24):
        time = str(j) + ":00:00.0000"
        file.write(date + time + "\n")


for i in range(1,31):
    date = "2022-03-" + str(i) +" "
    for j in range(24):
        time = str(j) + ":00:00.0000"
        file.write(date + time + "\n")


file.close()


