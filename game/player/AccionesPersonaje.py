import bge
g = bge.logic
gd = g.globalDict
scene = g.getCurrentScene()
con = g.getCurrentController()
#Este archivo con la clase AccionesPersonaje permite crear un objeto que tiene metodos que representan las acciones del
#personaje de esta forma si se le agrega una nueva accion al personaje el trabajo es mas facil, por conviccin mia elimino cada 
#objeto creado de esta clase luego de ejecutar la accion tambien cuanta con el metodo sumar_al_inventario para la accion recoger
class AccionesPersonaje:            
    
    def picar():
        over = con.sensors["over"]
        cLeft = con.sensors["cLeft"]
        targetPlayer = scene.objects["targetPlayer"]
        targetPlayer.position = [over.hitPosition[0]-0.5, over.hitPosition[1], over.hitPosition[2]]
        targetPlayer.visible = 0
        obj = over.hitObject
        obj["picando"] = 1 
        del obj
        
    def caminar():
        targetPlayer = scene.objects["targetPlayer"]
        over = con.sensors["over"]
        targetPlayer.position = over.hitPosition
        targetPlayer.visible = 1 
        targetPlayer["target"] = 1
        player = scene.objects["ActorPlayer"] 
        player["caminando"] = 1
        del player
        
    def recoger():
        over = con.sensors["over"]
        cLeft = con.sensors["cLeft"]
        targetPlayer = scene.objects["targetPlayer"]
        targetPlayer.position = [over.hitPosition[0]-0.5, over.hitPosition[1], over.hitPosition[2]]
        obj = over.hitObject
        if obj["meRecoge"] != 1:
            obj["meRecoge"] = 1
            sumar_al_inventario(obj.name)
            del obj      
    
def sumar_al_inventario(material):
    if "Hierro" in material:
        gd["inventario"].append("Hierro")
    if "Carbon" in material:
        gd["inventario"].append("Carbon")
    if "Diamante" in material:
        gd["inventario"].append("Diamante")
    

    
    
