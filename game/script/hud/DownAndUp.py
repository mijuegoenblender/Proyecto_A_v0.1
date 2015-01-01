import GameLogic as g
import mathutils
from mathutils import Vector
scene = g.getCurrentScene()

cont = g.getCurrentController()
o= cont.owner

Down = cont.sensors["Down"]
Up = cont.sensors["Up"]
min = 10
max = 50
def GetDownAndUp():
    if Down.positive and o.localPosition[1] > -max:
        o.localPosition[1] = o.localPosition[1]-0.5
    if Up.positive and o.localPosition[1] < -min:
        o.localPosition[1] = o.localPosition[1]+0.5
        
GetDownAndUp()
