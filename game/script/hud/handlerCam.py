from bge import logic, events, render
import bpy as D

cont = logic.getCurrentController()
Escena = logic.getCurrentScene()

TECLA_A = events.AKEY
TECLA_D = events.DKEY
TECLA_W = events.WKEY
TECLA_S = events.SKEY 
TECLA_PARAR = events.PKEY

ACTIVO = logic.KX_INPUT_ACTIVE 
RECIEN_ACTIVADO = logic.KX_INPUT_JUST_ACTIVATED 
RECIEN_DESACTIVADO = logic.KX_INPUT_JUST_RELEASED
obj = cont.owner
objPos = obj.worldPosition
teclado = logic.keyboard
myMouse = logic.mouse
ray = cont.sensors["Ray"]
# Mostrar raton
myMouse.visible = 1

# Dimensiones de pantalla
xMin = 20
xMax = ((render.getWindowWidth()) - 20)
yMin = 20
yMax = ((render.getWindowHeight()) - 20)
zmin = 10
zmax = 50

def GetMovimiento():
    # Posicion del raton
    myMousePos = myMouse.position
    myMousePosX = ((myMousePos[0])*(render.getWindowWidth()))
    myMousePosY = ((myMousePos[1])*(render.getWindowHeight()))
    if myMousePosX <= xMin:
        # Mover camara a la izquierda
        obj.applyMovement([-0.1,0,0],1)
    elif myMousePosX >= xMax:
        # Mover camara a la derecha
        obj.applyMovement([0.1,0,0],1)
    elif myMousePosY <= yMin:
        # Mover camara hacia arriba
        obj.applyMovement([0,0.1,0],1)
    elif myMousePosY >= yMax:
        # Mover camara hacia abajo
        obj.applyMovement([0,-0.1,0],1)
    elif teclado.events[TECLA_A] == ACTIVO:
        obj.applyRotation([0,0,0.01],1)
    elif teclado.events[TECLA_D] == ACTIVO:
        obj.applyRotation([0,0,-0.01],1)
    elif teclado.events[TECLA_W] == ACTIVO and GetDistancia() < zmax:
        obj.applyMovement([0,0,0.1],1)
    elif teclado.events[TECLA_S] == ACTIVO and GetDistancia() > zmin:
        obj.applyMovement([0,0,-0.1],1)
        
def GetDistancia():
    z = objPos[2] - ray.hitPosition[2]
    return z 
    
GetMovimiento()

