import os
import json
import random

#Get KH2 music filenames
currentDir = os.path.realpath(__file__).replace(os.path.basename(__file__),'')
f = open(currentDir+'musiclist.json','r')
musiclist = json.load(f)['KH2']
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
wild  = getmusic('wild')
field = getmusic('field')
fight = getmusic('battle')
cut   = getmusic('cutscene')

#Safeguard if there's too few music tracks
skip = [False, False, False] #Field, Fight, Cut
if len(wild) == 0:
    for i in range(3):
        folder = [field,fight,cut][i]
        if len(folder) == 0:
            skip[i] = True
        else:
            while len(folder) < len(musiclist):
                folder += folder
else:
    while len(wild) < len(musiclist):
        wild += wild

#Randomize the music
def getmusic(category):
    if len(category) > 0:
        old = music['filename']
        chosenindex = random.randint(0,len(category)-1)
        new = category.pop(chosenindex)
        f.write('- name: '+old+'\n  method: copy\n  source:\n  - name: '+new+'\n')
        global index
        index += 1

#Write the mod.yml
f = open(currentDir+'mod.yml','w',encoding='utf-8')
f.write('assets:\n')
index = 0
while index < len(musiclist):
    folder = random.randint(0,2)
    music  = musiclist[index]
    if folder == 0: #Wild
        getmusic(wild)
    else: #Categorical
        if music['type'] == 'field':
            if skip[0]:
                index += 1
            getmusic(field)
        elif music['type'] == 'battle':
            if skip[1]:
                index += 1
            getmusic(fight)
        elif music['type'] == 'cutscene':
            if skip[2]:
                index += 1
            getmusic(cut)

f.close()
