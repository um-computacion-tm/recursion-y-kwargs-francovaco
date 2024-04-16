#-------------FACTORIAL----------------
def factoriales (n):
    if n == 0:
        return 1
    factorial = n * factoriales(n - 1)
    return factorial


#-------------FIBONACCI----------------
def fibonacci (n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#-------------BUSCAR DATOS--------------
database = { "persona 1": {"primer_nombre": "Pablo", "segundo_nombre": "Diego", "primer_apellido": "Ruiz", "segundo_apellido": "Picasso"}, 
             "persona 2": {"primer_nombre": "Nahuel", "segundo_nombre": "Carlos", "primer_apellido": "Perez", "segundo_apellido": "Gonzalez"}, 
             "persona 3": {"primer_nombre": "Maria", "segundo_nombre": "Luisa", "primer_apellido": "Galera", "segundo_apellido": "Lopez"}, 
             "persona 4": {"primer_nombre": "Jose", "segundo_nombre": "Luis", "primer_apellido": "Garcia", "segundo_apellido": "Sanchez"}, 
             "persona 5": {"primer_nombre": "Franco", "segundo_nombre": "Tomas", "primer_apellido": "Yañes", "segundo_apellido": "Chuajer"}, 
             "persona 6": {"primer_nombre": "Juan", "segundo_nombre": "Matias", "primer_apellido": "Martin", "segundo_apellido": "Schajer"}, 
             "persona 7 ": {"primer_nombre": "Marta", "segundo_nombre": "Isidora", "primer_apellido": "Suarez", "segundo_apellido": "Macri"}, 
             "persona 8": {"primer_nombre": "Javier", "segundo_nombre": "Gerardo", "primer_apellido": "Milei", "segundo_apellido": "Conan"}, 
             "persona 9": {"primer_nombre": "Lionel", "segundo_nombre": "Andres", "primer_apellido": "Messi", "segundo_apellido": "Cuccitini"}, 
             "persona 10": {"primer_nombre": "Manuel", "segundo_nombre": "Jose", "primer_apellido": "Diez", "segundo_apellido": "Oñate"},}

def buscar_datos(persona, database):
    if "" in persona.values():
        print("Dato erróneo")
        return False
    for key, value in database.items():
        if persona == value:
            print(f"Dato encontrado, clave: {key}")
            return True   
    print("Dato no encontrado")
    return False

persona = {"primer_nombre": "Pablo", "segundo_nombre": "Diego", "primer_apellido": "Ruiz", "segundo_apellido": "Picasso"}
buscar_datos(persona, database)

persona = {"primer_nombre": "Diego", "segundo_nombre": "Alejandro", "primer_apellido": "Barroso", "segundo_apellido": "Miller"}
buscar_datos(persona, database)

persona = {"primer_nombre": "Maria", "segundo_nombre": "Luisa", "primer_apellido": "Galera", "segundo_apellido": "Suarez"}
buscar_datos(persona, database)

persona = {"primer_nombre": "Manuel", "segundo_nombre": "Jose", "primer_apellido": "Diez", "segundo_apellido": "Ramirez"}
buscar_datos(persona, database)

persona = {"primer_nombre": "Pablo", "segundo_nombre": "", "primer_apellido": "Ruiz", "segundo_apellido": "Picasso"}
buscar_datos(persona, database)

persona = {"segundo_nombre": "Diego", "primer_nombre": "Pablo", "segundo_apellido": "Picasso", "primer_apellido": "Ruiz"}
buscar_datos(persona, database)

persona = {"segundo_nombre": "Jose", "segundo_apellido": "Oñate", "primer_nombre": "Manuel", "primer_apellido": "Diez"}
buscar_datos(persona, database)

persona = {"segundo_apellido": "Chuajer", "primer_apellido": "Yañes", "segundo_nombre": "Tomas", "primer_nombre": "Franco"}
buscar_datos(persona, database)






