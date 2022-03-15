import os

path = '/Users/Hp/Desktop/Медина/git/pp2_21B030938/Labwork_6/dir-and-files/file_for_delete'

if os.path.exists(path):
    os.remove(path)
else:
    print('The file does not exist')    