import xml.etree.ElementTree as ET
tree = ET.parse('spawn.xml')
root = tree.getroot()

#remove npc spawn from spawns.xml
spawns = root.findall('spawn')
for spawn in spawns:
    npcs = spawn.findall('npc') # change to monster to select monster
    for npc in npcs:
        spawn.remove(npc) # remove npc tag from spawns.xml
tree.write('out.xml') # write a new file without selected tags
