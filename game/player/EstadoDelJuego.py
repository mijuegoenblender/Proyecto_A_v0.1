import bge
from script.AccionesPersonaje import AccionesPersonaje
g = bge.logic
gd = g.globalDict         
scene = g.getCurrentScene()
con = g.getCurrentController()
mouse = g.mouse
mouse.visible = 1
cLeft = con.sensors["cLeft"]
cRight = con.sensors["CRight"]
over = con.sensors["over"]
#Al acciones del personaje se manejan segun el estado del juego
#Hacemos las preguntas y segun la respuesta indicamos la accion
#Estas acciones las manejo desde el archivo AccionesPersonaje.py

if over.hitObject != None:
    if over.hitObject.name != "BarraHerramientas":
        if "overSlot" in over.hitObject.name:
           print("SS")
        elif cRight.positive:
            #Accion de caminar
            if "Roca" in over.hitObject.name or "drop" in over.hitObject.name:
                print("Que quieres?")
            else:
                accion = AccionesPersonaje
                accion.caminar()
                del accion
        elif "Roca" in over.hitObject.name and cLeft.positive:
            #Accion de picar
            accion = AccionesPersonaje
            accion.picar()     
            del accion
        elif "drop" in over.hitObject.name and cLeft.positive:
            #Accion de Recoger
            accion = AccionesPersonaje
            accion.recoger()     
            del accion
else:
    #Esto indica el estado del boton Izq del mause
    print(cLeft.getButtonStatus(bge.events.LEFTMOUSE))
    for x in gd["inventario"]:
        print(x)