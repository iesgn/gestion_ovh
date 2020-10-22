import ovh
import json
client = ovh.Client()

id=input("Indica el código del contacto técnico:")
try:
    result = client.get('/me/task/contactChange', 
        toAccount=id, # Filter the value of toAccount property (like) (type: string)
    )
except:
    print("Usuario incorrecto.")
    result=[]



# Pretty print
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