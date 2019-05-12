#! usr/bin/python
# -*- coding: utf-8 -*-
 
#Agenda con base de datos Sqlite3
 
#Modulos importados
import sqlite3
 
import os
global bord 
bord = "=" * 80
 
#Conexion con Base de Datos Sqlite3
con = sqlite3.connect("agenda.db")
cursor = con.cursor()
#Comprueba si la tabla existe, en caso de no existir la crea
cursor.execute("""CREATE TABLE IF NOT EXISTS datos (nombre TEXT, apellido TEXT, referencia TEXT, telefono TEXT, correo TEXT)""")
 
cursor.close()
 
#Declaracion de las funciones
 
def limpiar():
 
	"""Limpia la pantalla"""
 
	if os.name == "posix":
		os.system("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system("cls")
 
def agregar():
  
	"""Agrega un nuevo contacto a la Agenda"""
 
	print "Agregar contacto"
	print "----------------"
	print ""
 
	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()
 
	nombre = raw_input("Nombre: ")
	nombre = nombre.lower()
	apellido = raw_input("Apellido: ")
	apellido = apellido.lower()
	referencia = raw_input("Referencia: ")
	referencia = referencia.lower()
	telefono = raw_input("Telefono: ")
	correo = raw_input("Correo: ")
	correo = correo.lower()
 
	cursor.execute("insert into datos (nombre, apellido, referencia, telefono, correo) values ('%s','%s','%s','%s','%s')"%(nombre,apellido,referencia, telefono,correo))
 
	con.commit()
 
	print "Los datos fueron agregados correctamente."
 
	cursor.close()
	main()
 
def ver():
	
	"""Devuelve todos los contactos de la agenda"""
 
	print "Lista de contactos"
	print "------------------"
	print ""
 
	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()
 
	cursor.execute("SELECT * FROM datos")
	resultado = cursor.fetchall()
 
	for i in resultado:
		nomb = i[0]
		nomb = nomb.capitalize()
		apel = i[1]
		apel = apel.capitalize()
		refe = i[2]
		refe = refe.capitalize()
		#bord = "=" * 80
		print "%s %s" % ("[Nombre]" + nomb," [Apellido]" + apel)
		print "%s %s %s" % ("[Referencia]" + refe, "[telefono]" + i[3], "[Correo]" + i[4]) 
		print (bord)
	cursor.close()
 
	print ""
	raw_input("Presionar una tecla para continuar... ")
 
	main()
 
def buscar():
	global x 
	
	"""Busca un contacto en la agenda y lo lista"""
 
	print "Buscar contacto"
	print "---------------"
	print ""
	print "Criterios de busqueda:"
	print ""
	print "[0] = Nombre "
	print "[1] = Apellido "
	print "[2] = Referencia "
	print "[3] = Correo "
	print ""
	op_busq = raw_input("Elegir opción de busqueda: ")
	
 
	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()
 
	if op_busq != "0" and op_busq != "1" and op_busq != "2" and op_busq != "3":
		print "Opcion incorrecta "
		print "presionar una tecla para continuar..."
		limpiar()
		buscar()
	elif op_busq == "0":
		buscar = raw_input("Nombre a buscar: ")
		buscar = buscar.lower()
		##print buscar
		cursor.execute ("SELECT * FROM datos WHERE nombre LIKE '%"+buscar+"%'" )
		##cursor.execute ("SELECT * FROM datos WHERE nombre = '%s'" %(buscar))
		x = cursor.fetchall()
		mostrar_busqueda()
	elif op_busq == "1":
		buscar = raw_input("Apellido a buscar: ")
		buscar = buscar.lower()
		cursor.execute ("SELECT * FROM datos WHERE apellido LIKE '%"+buscar+"%'" )
		##cursor.execute ("SELECT * FROM datos where apellido = '%s'" %(buscar))
		x = cursor.fetchall()
		mostrar_busqueda()
	elif op_busq == "2":
		buscar = raw_input("Referencia a buscar: ")
		buscar = buscar.lower()
		cursor.execute ("SELECT * FROM datos WHERE referencia LIKE '%"+buscar+"%'" )
		##cursor.execute ("SELECT * FROM datos where referencia = '%s'" %(buscar))
		x = cursor.fetchall()
		mostrar_busqueda()
	elif op_busq == "3":
		buscar = raw_input("Correo a buscar: ")
		buscar = buscar.lower()
		cursor.execute ("SELECT * FROM datos WHERE correo LIKE '%"+buscar+"%'" )
		##cursor.execute ("SELECT * FROM datos where correo = '%s'" %(buscar))
		x = cursor.fetchall()
		##print x 
		mostrar_busqueda()			
	exit()	
		
		
def mostrar_busqueda():	
	
 
	print ""
	"""[x.upper() for x in ["a","b","c"]] """
	for i in x:
		el_nombre = i[0]
		el_nombre = el_nombre.capitalize()
		el_ape = i[1]
		el_ape = el_ape.capitalize()
		la_refe = i[2]
		la_refe = la_refe.capitalize()
		print "Nombre: ", el_nombre 
		print "Apellido:", el_ape 
		print "Referencia: ", la_refe
		print "Telefono:", i[3]
		print "Correo:", i[4]
		print (bord)
 
	cursor.close()
 
	##"if el_nombre != "":
	print ""
	
	raw_input("Presionar una tecla para continuar... ")
		
	##exit()
	main()
 
def eliminar():
  
	"""Elimina un contacto de la Agenda"""
 
	print "Eliminar contacto"
	print "-----------------"
	print ""
 
	con = sqlite3.connect("agenda.db")
	cursor = con.cursor()
 
	eliminar = raw_input ("Nombre de contacto a eliminar: ")
 
	cursor.execute("DELETE FROM datos WHERE nombre='%s'"%(eliminar))
 
	con.commit()
 
	cursor.close()
 
	print "Contacto eliminado correctamente..."
	print ""
	raw_input("Presionar una tecla para continuar... ")
	main()
 
def main():
 
	"""Funcion principal de la Agenda"""
 
	limpiar()
 
	print "-----------------------------------------"
	print "               Agenda                    "
	print "-----------------------------------------"
	print "                              Version 0.1"
	print """
	[1] Ingresar Contacto
	[2] Listar Contactos
	[3] Buscar Contacto
	[4] Eliminar Contacto
	[0] Salir
	"""
 
	opcion = raw_input("Ingresar una opción: ")
 
	if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
		print "Opcion incorrecta"
		raw_input()
		main()
	elif opcion == "1":
		limpiar()
		agregar()
	elif opcion == "2":
		limpiar()
		ver()
	elif opcion == "3":
		limpiar()
		buscar()
	elif opcion == "4":
		limpiar()
		eliminar()
	elif  opcion == "0":
		print ""
		print ""
		print ""
		limpiar()
	exit()
  
 
main()
