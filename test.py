import glob, os

cwd = os.getcwd()

mypath = cwd-"\CodingNomads\labs\python_fundamentals-master"
mylist = []
for file in os.listdir(mypath):
    if file.endswith(".jpg"):
        mylist.append(os.path.join(mypath, file))

print(mylist)
