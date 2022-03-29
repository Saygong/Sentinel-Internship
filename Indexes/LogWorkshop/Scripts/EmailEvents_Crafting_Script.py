
import random as r
file=open("EmailEvents_Logs.txt", "w")
actions =["Sent to quarantine", "No action taken", "Sent to junk", "Redirected", "Deleted"]

def randomID():
    return str(r.randint(111111, 999999))

# Headers:  EmailID, EmailAction


def prob():
    x = r.randint(1,10)
    if x <= 4:
        return 1
    elif x <=6:
        return 3
    elif x <=8:
        return 2
    elif x<=9:
        return 4
    else:
         return 0


for i in range(243):

    towrite=randomID()+","+actions[prob()]+"\n"
    file.write(towrite)


file.close()

