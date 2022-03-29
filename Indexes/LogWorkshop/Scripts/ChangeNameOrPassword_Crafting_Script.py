import random as r

file = open("ChangeNameOrPassword_Logs.txt", "w")
list= ["4723", "24724", "4781"]




for i in range(35):
    towrite = "2022-12-31"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)


for i in range(23):
    towrite = "2022-12-30"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)

for i in range(15):
    towrite = "2022-03-14"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)
    towrite = "2022-03-15"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)
    towrite = "2022-03-16"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)
    towrite = "2022-03-17"+" "+str(r.randint(0,23))+":00:00.000,"+list[r.randint(0,2)]+"\n"
    file.write(towrite)


file.close()


