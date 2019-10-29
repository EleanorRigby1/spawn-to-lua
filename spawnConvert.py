import xml.etree.ElementTree as ET
tree = ET.parse('spawn.xml')
root = tree.getroot()

#remove npc spawn from spawns.xml
'''
spawns = root.findall('spawn')
for spawn in spawns:
    npcs = spawn.findall('npc') # change to monster to select monster
    for npc in npcs:
        spawn.remove(npc) #remove npc tag from spawns
tree.write('out.xml')
'''

#get all npc/monster spawns
f = open("monsterSpawnList.lua", "x") #create a new file. make sure the file dont exist already
i = 0
for child in root:
    for spawns in child:
        if spawns.tag == 'npc': #change to monster/nps to get all monster/npc spawns
            #i = i + 1
            centerx = int(child.get('centerx')) + int(spawns.get('x'))
            centery = int(child.get('centery')) + int(spawns.get('y'))
            centerz = int(child.get('centerz'))
            name = spawns.get('name')
            i = i + 1
            f = open("spawnList.lua", "a")
            f.write("[" + str(i) + "] = " + "{name = \"" + name + "\"," + " pos = {x=" + str(centerx) + ",y=" + str(centery) +",z="+ str(centerz) + "}},\n") #write to new file
            f.close()
