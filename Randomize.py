import sys
import os
import json
import random

#Get KH2 music filenames
currentDir = sys.argv[0].replace((sys.argv[0].split('\\')[-1]),'')
f = open(currentDir+'musiclist.json','r')
oldmusiclist = json.load(f)
newmusiclist = {}
newmusicpool = {}
f.close()

#Get old music filenames
dirstart = len(currentDir)
def getmusic(category):
    musicfiles = []
    for root, dirs, files in os.walk(currentDir+category):
        for file in files:
            if file[-4:] == '.scd':
                musicfiles.append(root[dirstart:]+'\\'+file)
    return musicfiles

#Get new music filenames based on type
for music in oldmusiclist:
    musictypes = music['type']
    for musictype in musictypes:
        musictype = musictype.lower()
        if not musictype in newmusiclist:
            newmusiclist[musictype] = getmusic(musictype) #Backup list
            newmusicpool[musictype] = getmusic(musictype) #Usage list

#Randomize the music
def getmusic(category):
    if len(category) > 0:
        old = currentmusic['filename']
        title = currentmusic['title']
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
    currentmusic = oldmusiclist[index]
    #Skip if no tracks can be used
    availablemusic = []
    for i in currentmusic['type']:
        availablemusic += newmusiclist[i.lower()]
    if len(availablemusic) == 0:
        index += 1
        continue
    #Pick tracks from one of the type listed
    availablemusic = []
    while len(availablemusic) == 0:
        chosentype     = random.choice(currentmusic['type']).lower()
        availablemusic = newmusicpool[chosentype]
    #Do the actual randomization
    getmusic(availablemusic)
    #Refill track pool
    if len(availablemusic) == 0:
        newmusicpool[chosentype] = newmusiclist[chosentype].copy()

f.close()
