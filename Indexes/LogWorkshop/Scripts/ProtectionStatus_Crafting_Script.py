import random as r
file=open("ProtectionStatus_Logs.txt", "w")
osname = ["Linux", "Microsoft Windows 10", "Microsoft Windows 11", "Ubuntu Server", "macOS"]
status = ["Real time protection", "Signtures out of date", "Unprotected"]

# Headers:  ProtectionStatus, OSName

for i in range(87):

    towrite=status[r.randint(0, 2)]+","+osname[r.randint(0,4)]+"\n"
    file.write(towrite)

for i in range(15):
    towrite=status[0]+","+osname[4]+"\n"
    file.write(towrite)


file.close()

