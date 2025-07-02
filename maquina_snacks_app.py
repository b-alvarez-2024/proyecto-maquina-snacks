from modul.ServicioSnacks import ServicioSnacks
from modul.snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []


    def maquina_snacks(self):
        salir = False
        print('*** maquina de snacks ***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'ocurrio un error {e}')


    def mostrar_menu(self):
        print(f'''menu:
        1. comprar snack
        2. mostrar ticket
        3. agregar nuevo snack al inventario
        4. mostrar inventario snacks
        5. salir''')
        return int(input('elige una opcion: '))


    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa pronto!')
            return True
        else:
            print(f'Opcion invalida: {opcion}')
        return False


    def comprar_snack(self):
        id_snack = int(input('que snack quieres comprar (id)?'))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'snack encontrado: {snack}')
        else:
            print(f'id snack no encontrado {id_snack}')


    def mostrar_ticket(self):
        if not self.productos:
            print('no hay snacks en el ticket') 
            return
        total = sum(snack.precio for snack in self.productos)
        print('---ticket de venta---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')


    # utiliza agregar_snacks de ServicioSnacks
    def agregar_snack(self):
        nombre = input('nombre del snack: ')
        precio = float(input('precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado correctamente.')


# ejecucion programa principal
if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
