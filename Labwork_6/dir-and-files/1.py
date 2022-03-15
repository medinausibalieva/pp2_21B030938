import os

path = '/Users/Hp/Desktop/Медина/git/pp2_21B030938'

dirs = []
files = []
all = []
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        dirs.append(i)
    if os.path.isfile(os.path.join(path, i)):
        files.append(i) 
    all.append(i)
print('Directories:\n',dirs)  
print('Files:\n',files)      
print('All directories and files:\n',all)