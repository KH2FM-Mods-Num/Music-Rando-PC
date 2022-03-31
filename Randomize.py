import sys
import os
import json
import random

#Get KH2 music filenames
currentDir = sys.argv[0].replace((sys.argv[0].split('\\')[-1]),'')
f = open(currentDir+'musiclist.json','r')
oldmusiclist = json.load(f)['KH2']
newmusiclist = {}
f.close()


#Get new music filenames
dirstart = len(currentDir)
def getmusic(category):
    musicfiles = []
    for root, dirs, files in os.walk(currentDir+category):
        for file in files:
            if file[-4:] == '.scd':
                musicfiles.append(root[dirstart:]+'\\'+file)
    return musicfiles

wildmusiclist = getmusic('wild')
for music in oldmusiclist: #Separate based on type
    musictype = music['type']
    if not musictype in newmusiclist and musictype.lower() != 'wild':
        newmusiclist[musictype] = getmusic(musictype)
wildmusicpool = wildmusiclist.copy()

#Randomize the music
def getmusic(category):
    if len(category) > 0:
        old = music['filename']
        title = music['title']
        chosenindex = random.randint(0, len(category)-1)
        new = category.pop(chosenindex)
        f.write('- name: '+old+' #'+title+
                '\n  method: copy\n  source:\n  - name: '+new+'\n')
        global index
        index += 1
        
#Write the mod.yml
f = open(currentDir+'mod.yml','w',encoding='utf-8')
f.write('assets:\n')
index = 0
while index < len(oldmusiclist):
    music  = oldmusiclist[index]
    newmusicpool = newmusiclist[music['type']]
    #Skip if no available music
    if len(wildmusiclist) + len(newmusicpool) == 0:
        index += 1
        continue
    #1/3 chance for wild
    folder = random.randint(0,2)
    if folder == 0:
        getmusic(wildmusicpool)
        if len(wildmusicpool) == 0: #Reset if all tracks are used
            wildmusicpool = wildmusiclist.copy()
    else:
        getmusic(newmusicpool)
f.close()
