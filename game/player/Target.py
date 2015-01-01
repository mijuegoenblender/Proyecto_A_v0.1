import bge 
g = bge.logic
gd = g.globalDict  
scene = g.getCurrentScene()
con = g.getCurrentController()

mat = con.owner
if mat["target"] == 1:
    player = scene.objects["ActorPlayer"]
    player["caminando"] = 0
    player["atacando"] = 0
    player["picando"] = 0
    mat["target"] = 0
    con.activate("Visibility")