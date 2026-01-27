'''
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
'''
#Create a dictionary 
hotel = {
    "nombre": "Hotel Paraíso",
    "numero_de_estrellas": 5,
    "habitaciones": [
        {
            "numero": 101,
            "piso": 1,
            "precio_por_noche": 45000
        },
        {
            "numero": 202,
            "piso": 2,
            "precio_por_noche": 55000
        },
        {
            "numero": 303,
            "piso": 3,
            "precio_por_noche": 65000
        }
    ]
}