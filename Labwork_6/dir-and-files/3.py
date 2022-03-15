import os

path = '/Users/Hp/Desktop/Медина/git/pp2_21B030938/Labwork_6'

print('Existense:\n', os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))