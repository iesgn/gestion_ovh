import ovh
import json
client = ovh.Client()

vps=input("Indica el nombre de un vps:")
id=input("Indica el código del contacto técnico:")
dominio=input("Indica el nombre de dominio:")

print("VPS:%s" % vps)
try:
    result2 = client.post('/vps/%s/changeContact'%vps, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de vps o usuario incorrecto.")

print("Dominio:%s" % dominio)
try:
    result2 = client.post('/domain/%s/changeContact'%dominio, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de dominio o usuario incorrecto.")


print("Zona de dominio:%s" % dominio)
try:
    result2 = client.post('/domain/zone/%s/changeContact'%dominio, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de zona de dominio o usuario incorrecto.")

print("Correo del dominio:%s" % dominio)
try:
    result2 = client.post('/email/domain/%s/changeContact'%dominio, 
            contactAdmin=None, # The contact to set as admin contact (type: string)
            contactBilling=None, # The contact to set as billing contact (type: string)
            contactTech=id, # The contact to set as tech contact (type: string)
        )
except:
    print("Error. Nombre de correo de dominio o usuario incorrecto.")



try:
    result = client.get('/me/task/contactChange', 
        toAccount=id, # Filter the value of toAccount property (like) (type: string)
    )
except:
    print("Usuario incorrecto.")
    result=[]


for servicio in result:

    result2 = client.get('/me/task/contactChange/%s' % servicio)
    #print(json.dumps(result2, indent=4))
    print(result2.get("serviceDomain"),"(",result2.get("id"),")")
    token = input("Token:")
    try:
        result = client.post('/me/task/contactChange/%s/accept' % result2.get("id"), 
            token=token, # The token you received by email for this request (type: string)
        )
    except:
        print("Error al validar el token.")