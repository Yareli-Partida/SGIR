from models.Insumo import Insumo

insumos = []

persona = Insumo(10,20,30,40,50,50)
insumos.append(persona)

for persona in insumos:
    print(persona._id)



