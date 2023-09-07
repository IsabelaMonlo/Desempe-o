diccionarioPersonas={}   


while True:
    print("Bienvenido al programa de diccionario")
    print("Por favor selecione la acción que desa realizar:")
    print("1)si desea agregar")
    print("2)si desea actualizar")
    print("3)si desea consultar")
    print("4)si desea eliminar")
    print("5)mostrar todos los elementos del diccionario")
    print("6)si desea salir del programa")
    action = input()
    
    if action == '1':
        nom=input("Ingrese la nombre a agregar:")
        tele=input('ingrese un telefono: ')
        diccionarioPersonas[nom]=tele
    elif action == '2':
        actilizarvalor=input("Persona a actualizar: ")
        cel = input("ingrese nuevo telefono a actualizar:")
        diccionarioPersonas[actilizarvalor]=cel
        print("Diccionario actualizado: ",diccionarioPersonas)
    elif action == '3':
       print("Diccionario: ", diccionarioPersonas)
       nombreid=(input("Persona a consultar"))
       if nombreid in diccionarioPersonas:
        nombre=diccionarioPersonas[nombreid]
       ("el nombre consultado es: ",nombre)
    elif action =='4':
        print("Diccionario: ", diccionarioPersonas)
        nombreElminiar=input("el elemento ha sido eliminado. ")
        if nombreElminiar in diccionarioPersonas:
            diccionarioPersonas.pop(nombreElminiar)
    elif action =='5':
        print("Todos los elementos de la lista son: ",diccionarioPersonas)  
    elif action =='6':
        print("Has salido del programa.")
        break
    else:
        ("Intente nuevamente")    
    
