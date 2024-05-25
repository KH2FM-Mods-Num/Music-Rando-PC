import sys
import yaml
import os
import copy
import random

#Get KH2 music filenames
currentDir = sys.argv[0].replace((sys.argv[0].split('\\')[-1]),'')
data = yaml.safe_load(open(currentDir+'MusicData.yml','r'))
newmusiclist = {}

#Get a list of all music types
for music in data['Base Music List']:
    for musictype in music['type']:
        musictype = musictype.lower() #Make it case-insensitive
        if musictype not in newmusiclist:
            newmusiclist[musictype] = []

#Make a dictionary of all replacement music & type
if data['Replacement Music Location'] == '':
    replaceDir = currentDir #Use the python file's location (can't be empty for os.walk to work)
    truncateDir = len(currentDir)
else:
    replaceDir = data['Replacement Music Location']
    truncateDir = 0

for root, dirs, files in os.walk(replaceDir):
    if replaceDir == currentDir: #Revert replaceDir
        replaceDir = ''

    for folder in reversed(root.split('\\')): #Get type of new music (whichever folder name match that comes last)
        folder = folder.lower()
        if folder in newmusiclist:
            musictype = folder
            break;
    else: #Stop scanning current path if the music isn't part of any type
        continue
    
    for file in files:
        if file[-4:] != '.scd':
            continue
        newmusiclist[musictype].append(root[truncateDir:]+'\\'+file)

#Randomization Function
def getmusic(category):
    category = category.lower()
    currentpool = newmusicpool[category]
    if len(currentpool) == 0: #Skip if no music is available
        return False
    newmusic = currentpool.pop(random.randint(0, len(currentpool)-1)) #Randomly choose new music and remove it from the pool
    if len(currentpool) == 0: #Refresh if ran out of available music
        newmusicpool[category] = copy.deepcopy(newmusiclist[category])
    return newmusic

#Do the randomization & write the mod.yml
newmusicpool = copy.deepcopy(newmusiclist)
musicresult = {}
f = open(currentDir+'mod.yml','w',encoding='utf-8')
f.write('assets:\n')
for music in data['Base Music List']:
    types = music['type']
    for i in range(len(types)): #Repick a type on unsuccessful attempts
        chosentype = types.pop(random.randint(0,len(types)-1)) #Pick a type and remove it from the pool
        newmusic = getmusic(chosentype) #Do the randomization
        if newmusic:
            break

    if not newmusic: #Skip current music if all types are exhausted
        continue

    #Write the mod.yml
    f.write('- name: '+music['filename']+' #'+music['title']+'\n')
    f.write('  method: copy\n')
    f.write('  source:\n')
    f.write('  - name: '+newmusic+'\n')

f.close()
