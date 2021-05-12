import glob, os
#print("libraries important")
cwd = os.getcwd()
#print(cwd)
mypath = cwd+"\images"
mylist = []
for file in os.listdir(mypath):
    if file.endswith(".jpg"):
        mylist.append(os.path.join(mypath, file))
        #print(os.path.join(mypath, file))
print(mylist)

#print(os.chdir("/images"))
#for file in glob.glob(".jpg"):
#    print(file)

