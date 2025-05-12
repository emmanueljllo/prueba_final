# prueba de desempeño - modulo 1

list = []

def main():
    menu()

#create a funtion 

def exit_():
    print("\n")

#validate consult
    validate = True
    while validate:
        print('-'*30)
        opcion = input("¿deseas continuar? (si/no): ")
        optionfinal = opcion.lower()
        if optionfinal == "si": 
            #option si

            menu()

        elif optionfinal == "no": 
            #option No 
        
    #exit program

            print("saliendo")        
            print("'-'*30")
            print()

        else:
            print("opcion no valida")
            exit_()

        break

# create funtion menu

def menu():
    print('-'*20)
    print("Gestion De Inventario")
    print('-'*20)
    print("opciones:")
    print('-'*20)
    print("1. Añadir Productos")
    print("2. Buscar Productos")
    print("3. Actualizar Productos")
    print("4. Eliminar Productos")
    print("5. Calcular El Valor Del Inventario")
    print("6. Mostrar Inventario")
    print("7. salir")
    print('-'*20)
    option = (input("Que Opcion Deseas: "))
    print('-'*20)
    validate = True
    while validate:
        match option:

            case "1": 
                add()# option 1 the funtion add

            case "2": 
                search() # optioon 2 the funtion search
            
            case "3": 
                update() # option 3 the funtion update

            case "4":
                delete() # option 4 the funcion delete

            case "5":
                total_value() # option 5 the funtion total_value

            case "6":
                show() # option 6 the funtion show

            case "7":
                print("¿Estas Seguro De Salir?")
                exit_() # option 7 the funtion exit

            case _:
                print('_'*20)
                print("opcion no valida")
                print('-'*20)
                main()
                break
        break
    print('-'*20)

def add(name:str='',price:float=0,quantity:int=0):
    validate = True
    while validate:
        print("REGISTRAR PRODUCTO")
        print('-'*20)
        name = input("ingresa el nombre del producto: ")
        if name == "":
            print("Nombre No Puede Estar Vacio")
            name = input("Ingresa El Nombre Del Producto: ")
        elif not name.isalpha():
            print("Nombre Solo Puede Tener Letras")
            name = input("ingrese el nombre del producto: ")
        elif len(name) <3:
            print("Nombre Debe Tener Al Menos 3 Caracteres")
            name =  input("Ingrese El Nombre Del Producto: ")
        elif len(name) >20:
            print("Nombre No Puede Tener Mas De 20 Caracteres")
            name = input("ingrese el nombre del producto: ")
        else: 
            validate = False
        break

    validate = True
    while validate:
        price = input("ingrese el precio del producto: ")
        if price == "":
            print("Precio No Puede Estar Vacio")
            price = input("ingrese el precio del producto: ")
        elif not price.isnumeric():
            print("Precio Solo Puede Contener Numeros#")
            price = input("Ingrese El Precio Del Producto: ")
        elif float(price) <0: #validate the price is not negative, if it is negative ask again
             print('Precio no puede ser negativo')
             price = input('Ingrese el precio del producto: ')
        else: #If the price is valid break the loop
            validate = False
        break

    validate = True
    while validate:
        quantity = input('Ingrese la cantidad del producto: ')
        if quantity == '': #validate the quantity is not empty, if it is empty ask again
            print('Cantidad no puede estar vacio')
            quantity = input('Ingrese la cantidad del producto: ')
        elif not quantity.isnumeric(): #validate the quantity is number, if it is not a number ask again
            print('Cantidad solo puede contener numeros')
            quantity = input('Ingrese la cantidad del producto: ')
        elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
            print('Cantidad no puede ser negativa')
            quantity = input('Ingrese la cantidad del producto: ')
        else: #If the quantity is valid break the loop
            validate = False 
        break

    tupla = (float(price), int(quantity)) #create a tuple with the price and quantity
    #create a dictionary with the name, price and quantity
    dict = {
        'name': name,
        'price':tupla[0],
        'quantity': tupla[1]
    }
    list.append(dict) #add the dictionary to the list
    print('-'*20)
    print(f"Producto agregado: {name}, Precio: {tupla[0]}, Cantidad: {tupla[1]}")
    
    exit_()

    return list

#Create a function that searches for a product in the list of products
def search():
    validate = True
    while validate:
        print('-'*20)
        print('BUSCAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a buscar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a buscar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name: 
            print(f"Producto encontrado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            exit_()
            break
    else: #If the product is not found in the list
        print('Producto no encontrado')
    exit_()
        
    return list

#Create a function that updates a product in the list of products
def update():
    validate = True
    while validate:
        print('-'*20)
        print('ACTUALIZAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a actualizar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a actualizar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name:
            print(f"Producto encontrado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            validate = True
            while validate:
                price = input('Ingrese el nuevo precio del producto: ')
                if price == '': #validate the price is not empty, if it is empty ask again
                    print('Precio no puede estar vacio')
                    price = input('Ingrese el nuevo precio del producto: ')
                elif not price.isnumeric(): #validate the price is number, if it is not a number ask again
                    print('Precio solo puede contener numeros')
                    price = input('Ingrese el nuevo precio del producto: ')
                elif float(price) < 0: #validate the price is not negative, if it is negative ask again
                    print('Precio no puede ser negativo')
                    price = input('Ingrese el nuevo precio del producto: ')
                else: #If the price is valid break the loop
                    price = float(price)
                    validate = False
                break

            validate = True
            while validate:
                quantity = input('Ingrese la nueva cantidad del producto: ')
                if quantity == '': #validate the quantity is not empty, if it is empty ask again
                    print('Cantidad no puede estar vacio')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                elif not quantity.isnumeric(): #validate the quantity is number, if it is not a number ask again
                    print('Cantidad solo puede contener numeros')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
                    print('Cantidad no puede ser negativa')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                else: #If the quantity is valid break the loop
                    quantity = int(quantity)
                    validate = False
                break

            print(f"Producto actualizado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            
            exit_()
            break

#create a function that deletes a product from the list of products
def delete():
    validate = True
    while validate:
        print('-'*20)
        print('ELIMINAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a eliminar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a eliminar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name:
            list.remove(i) #remove the product from the list
            print(f"Producto eliminado: {i['name']}")
            exit_()
            break
    else: #If the product is not found in the list
        print('Producto no encontrado')
    exit_()
        
    return list

#create a function that calculates the total value of the inventory
def total_value():
    total = 0
    for i in list: #calculate the total value of the inventory
        total += i['price'] * i['quantity'] #multiply the price by the quantity of each product
    print(f'El valor total del inventario es: {total}')
    exit_()
    return total

#create a function that shows the inventory
def show():
    if len(list) == 0: #validate the inventory is not empty, if it is empty show a message
        print('-'*20)
        print('Inventario vacio')
    else:
        print('-'*20)
        print('Inventario:')
        for i in list: #show the inventory
            print('-'*40)
            print(f"Nombre: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}\n")
    exit_()
    return list

#Call the main function
main()






