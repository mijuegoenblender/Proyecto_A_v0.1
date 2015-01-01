import GameLogic as g
import mathutils
from mathutils import Vector
scene = g.getCurrentScene()

co= g.getCurrentController()
o= co.owner


ray = co.sensors["Ray"]
muro=ray.hitObject

Camera = scene.objects["Camera"]
Empty = scene.objects["cameraTarget"]
Plano = scene.objects["PlanoCamera"]

def Get():
    if ray.positive: 
        Camera.worldPosition= ray.hitPosition 
        #Camera.localPosition.y += 0.5
        Camera.worldOrientation =  Plano.worldOrientation
    else: 
        Camera.worldPosition= Empty.worldPosition
        
Get()
