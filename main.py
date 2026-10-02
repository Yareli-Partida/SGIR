from models.Insumo import Insumo

insumos = []

persona = Insumo(1,'nombre',20,'kg',50,50)
insumos.append(persona)

for persona in insumos:
    print(persona._id)



