import json

s = '''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------ '''
s1 = '                            '
s2 = ' '
f = open('sample-data.json.txt', 'r')
text = f.read() 
my = json.loads(text) 

print(s)
for i in range(len(my["imdata"])):
    print(my["imdata"][i]["l1PhysIf"]["attributes"]["dn"],s1, 
    my["imdata"][i]["l1PhysIf"]["attributes"]['speed'],s2,my["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])