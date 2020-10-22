import ovh
import json
client = ovh.Client()

vps=input("Indica el nombre de un vps:")
id=input("Indica el código del contacto técnico:")
dominio=input("Indica el nombre de dominio:")

try:
    result2 = client.post('/vps/%s/changeContact'%vps, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de vps o usuario incorrecto.")

try:
    result2 = client.post('/vps/%s/changeContact'%vps, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de vps o usuario incorrecto.")
