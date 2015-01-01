import bge
g = bge.logic
gd = g.globalDict         
scene = g.getCurrentScene()
con = g.getCurrentController()

#Separo la logica de las animaciones del personaje en este archivo que en futuro supongo agregare tambien la logica de los  
#sonidos 
#

obj = con.owner

if obj["picando"] == 1:
    print("picando")
elif obj["caminando"] == 1:
    print("camina")
elif obj["atacando"] == 1:
    print("esto es esparta!!!!")
else:
    print("parado")