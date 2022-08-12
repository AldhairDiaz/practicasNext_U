import json



def actualizar_cantidad_cliente(cant):

    new_cant=cant
    BD_CLIENTE = {}  # Iniciando la Base de Datos en Json con 2 campos "cliente"y"admin" que son quienes van a interactuar
    BD_CLIENTE['user_cliente'] = []
    BD_CLIENTE['user_cliente'].append({
        'codigo': 'aldhair',

        'cant_total_cripto': new_cant,
        'cant_total_USD': 0

    })
    with open('BD_CLIENTE.json', 'w') as file:
        json.dump(BD_CLIENTE, file, indent=4)

def actualizar_cantidad_admin(cant):
    new_cant_admin = cant
    BD_ADMIN={}
    BD_ADMIN['user_admin'] = []
    BD_ADMIN['user_admin'].append({

        'can_total_cripto': new_cant_admin,
        'cant_total_USD': 0
    })


    with open('BD_ADMIN.json', 'w') as file:
        json.dump(BD_ADMIN, file, indent=4)









