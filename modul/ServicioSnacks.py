
import os.path
from modul.snack import Snack


class ServicioSnacks:
	NOMBRE_ARCHIVO = 'snacks.txt'


	def __init__(self):
		self.snacks = []
		# revisar si ya existe el archivo snacks
		# si ya existe, obtenemos los snacks del archivo
		if os.path.isfile(self.NOMBRE_ARCHIVO):
			self.snacks = self.obtener_snacks()
		# si no, cargamos algunos snacks iniciales
		else:
			self.cargar_snacks_iniciales()


	def cargar_snacks_iniciales(self):
		snacks_iniciales = [
			Snack('papas', 70),
			Snack('refresco', 50),
			Snack('sandwich', 120)
		]
		self.snacks.extend(snacks_iniciales)
		self.guardar_snacks_archivo(snacks_iniciales)


	def guardar_snacks_archivo(self, snacks):
		try:
			with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
				for snack in snacks:
					archivo.write(f'{snack.escribir_snack()}\n')
		except Exception as e:
			print(f'error al guardar {e}')


	def obtener_snacks(self):
		snacks = []
		try:
			with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
				for linea in archivo:
					id_snack, nombre, precio = linea.strip().split(',')
					snack = Snack(nombre, float(precio))
					snacks.append(snack)
		except Exception as e:
			print(f'error al leer{e}')
		return snacks


	# representa añadir snack a la lista
	def agregar_snack(self, snack):
		self.snacks.append(snack)
		self.guardar_snacks_archivo([snack])


	# representa mostrar la lista de snacks
	def mostrar_snacks(self):
		print('--- Snacks en el inventario ---')
		for snack in self.snacks:
			print(snack)


	# representa comprar snack
	def get_snacks(self):
		return self.snacks