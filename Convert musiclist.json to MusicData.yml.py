import sys
import json
import yaml

Path = sys.argv[0].replace((sys.argv[0].split('\\')[-1]),'')
Filename = Path + 'musiclist.json'
Filename2 = Path + 'MusicData.yml'
f = json.load(open(Filename))
g = {}
g['Replacement Music Location'] = ""
g['Base Music List'] = f
yaml.dump(g,open(Filename3,'w'))
