import os
import random

#Get KH2 music filenames
currentDir = os.path.realpath(__file__).replace(os.path.basename(__file__),'')
musiclist = []
for folder in ['bgm','vagstream']:
    files = os.listdir(currentDir+folder)
    for file in files:
        if file[-4:] == '.scd':
            musiclist.append(folder+'\\'+file)

#Get new music filenames
randomlist = musiclist.copy()
dirstart = len(currentDir)
for root, dirs, files in os.walk(currentDir+'bgmnew'):
    for file in files:
        if file[-4:] == '.scd':
            randomlist.append(root[dirstart:]+'\\'+file)
random.shuffle(randomlist)

#Write the mod.yml
f = open(currentDir+'mod.yml','w')
f.write('assets:\n')
for i in range(len(musiclist)):
    old = musiclist[i]
    new = randomlist[i]
    f.write('- name: '+old+'\n  method: copy\n  source:\n  - name: '+new+'\n')
f.close()
