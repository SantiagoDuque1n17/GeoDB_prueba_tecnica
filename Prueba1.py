#!/usr/bin/env python
# coding: utf-8

# In[1]:


import base58
import datetime

import matplotlib.pyplot as plt
import numpy as np

from random import choice
from random import randint
from string import ascii_lowercase
from dateutil.parser import parse


# In[ ]:


# Código para la prueba técnica de GeoDB
# Santiago Duque Porras
# Diciembre 2020


# In[2]:


"""
Clase para representar los Tickets. 

Parámetros:

id_ticket (string en base58 de longitud 20)
id_evento (string en base58 de longitud 10)
numero_de_entrada (integer entre 1 y 1.000.000)
estado (string/char 'v' o 'u')

No tiene funciones propias, sólo sirve para representar los Tickets
"""
class Ticket:
    def __init__(self, id_ticket, id_evento, numero_de_entrada, estado):
        
        self.id_ticket = id_ticket
        self.id_evento = id_evento
        self.numero_de_entrada = numero_de_entrada
        self.estado = estado
        
        
        #id_ticket type check
        try:
            base58.b58decode(id_ticket)
            self.id_ticket = id_ticket
            if (len(id_ticket) != 20 or isinstance(id_ticket, str) == False):
                print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
                self.id_ticket = "invalid"
        except:
            print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
            self.id_ticket = "invalid"
            
            
        #id_evento type check
        try:
            base58.b58decode(id_evento)
            self.id_evento = id_evento
            if (len(id_evento) != 10 or isinstance(id_evento, str) == False):
                print("Error - 'id_evento' debe ser un texto en Base58 de longitud 10")
                self.id_evento = "invalid"
        except:
            print("Error - 'id_evento' debe ser un texto en Base58 de longitud 10")
            self.id_evento = "invalid"
            
                   
        #numero_de_entrada type check
        if (numero_de_entrada < 1 or numero_de_entrada > 1000000 or isinstance(numero_de_entrada, int) == False):
            print("Error - 'numero_de_entrada' debe ser un integral entre 1 y 1.000.000")
            self.numero_de_entrada = "invalid"
            
        #estado type check
        if ((estado != 'v' and estado != 'u') or isinstance(estado, str) == False):
            print("Error - 'estado' debe ser 'v' o 'u' ")
            self.estado = "invalid"
            
    


# In[3]:


#Código de testeo para la clase Ticket

ticket1 = Ticket("1111111111aaaaaaaaaa", "1111111111", 100, 'v')
print(ticket1.id_ticket)
print(ticket1.id_evento)
print(ticket1.numero_de_entrada)
print(ticket1.estado)


# In[4]:


"""
Clase para representar los Eventos. 

Parámetros:

id_evento (string en base58 de longitud 10)
id_recinto (string en base58 de longitud 5)
descripcion (string)
fecha (formato 'date')

No tiene funciones propias, sólo sirve para representar los Eventos
"""
class Evento:
    def __init__(self, id_evento, id_recinto, descripcion, fecha):
            
        #id_evento type check
        try:
            base58.b58decode(id_evento)
            self.id_evento = id_evento
            if (len(id_evento) != 10 or isinstance(id_evento, str) == False):
                print("Error - 'id_evento' debe ser un texto en Base58 de longitud 10")
                self.id_evento = "invalid"
        except:
            print("Error - 'id_evento' debe ser un texto en Base58 de longitud 10")
            self.id_evento = "invalid"
            
        #id_recinto type check
        try:
            base58.b58decode(id_recinto)
            self.id_recinto = id_recinto
            if (len(id_recinto) != 5 or isinstance(id_recinto, str) == False):
                print("Error - 'id_recinto' debe ser un texto en Base58 de longitud 5")
                self.id_recinto = "invalid"
        except:
            print("Error - 'id_recinto' debe ser un texto en Base58 de longitud 5")
            self.id_recinto = "invalid"
            
                   
        #descripcion type check
        self.descripcion = descripcion
        if (len(descripcion) > 1000 or isinstance(descripcion, str) == False):
            print("Error - La descripción debe ser un texto que no supere los 1000 caracteres")
            self.descripcion = "invalid"
            
        #fecha type check  
        self.fecha = fecha


# In[5]:


#Código de Testeo para la clase Evento

evento1 = Evento("1111111111", "aaaaa", "hola hola hola", datetime.date.today())
print()
print(evento1.id_evento)
print(evento1.id_recinto)
print(evento1.descripcion)
print(evento1.fecha)


# In[6]:


"""
Clase para representar los Recintos. 

Parámetros:

id_recinto (string en base58 de longitud 5)
latitud (float)
longitud (float)

No tiene funciones propias, sólo sirve para representar los Recintos

"""

class Recinto:
    def __init__(self, id_recinto, latitud, longitud):
        #id_recinto type check
        try:
            base58.b58decode(id_recinto)
            self.id_recinto = id_recinto
            if (len(id_recinto) != 5 or isinstance(id_recinto, str) == False):
                print("Error - 'id_recinto' debe ser un texto en Base58 de longitud 5")
                self.id_recinto = "invalid"
        except:
            print("Error - 'id_recinto' debe ser un texto en Base58 de longitud 5")
            self.id_recinto = "invalid"
            
         
        self.latitud = latitud
        #latitud type check
        if (isinstance(latitud, float) == False):
            print("Error - Formato incorrecto de latitud")
            self.latitud = "invalid"
           
        
        #longitud type check
        self.longitud = longitud
        if (isinstance(longitud, float) == False):
            print("Error - Formato incorrecto de latitud")
            self.longitud = "invalid"
            
        


# In[7]:


#Código de testeo para los Recintos

recinto1 = Recinto('11111', 58.123123, 78.97328273)

print(recinto1.id_recinto)
print(recinto1.latitud)
print(recinto1.longitud)


# In[20]:


#RETO 1

"""
Función para generar n número de tickets en función de los eventos disponibles.

"""
def generar_tickets(n_tickets, lista_eventos):
    lista_tickets = []
    
    #Generar una lista con todas las IDs de los eventos
    lista_id_eventos = []
    for evento in lista_eventos:
        lista_id_eventos.append(evento.id_evento)
        
    #Contador del número de entradda
    numero_actual = 1
    
    #Ticket: id_ticket, id_evento, numero_de_entrada, estado
    for n in range (n_tickets):
        
        id_ticket = generar_id_ticket_aleatoria()
        
        #El número del evento es n módulo el número total de eventos que hay
        #Es decir, se asignarán tickets secuencialmente a los eventos y, cuando llegue al final
        #de la lista de eventos, empezará por el principio.
        n_evento = n%len(lista_id_eventos)
        id_evento = lista_id_eventos[n_evento]
        
        numero_de_entrada = numero_actual
        numero_actual = numero_actual+1
        
        #Lo mismo con el estado de los tickets. Van alterando entre válido y usado. 
        #Se podrían generar de otras maneras, quizás con una probabilidad.
        lista_estados = ['v', 'u']
        estado = lista_estados[n%2]
        
        lista_tickets.append(Ticket(id_ticket, id_evento, numero_de_entrada, estado))
        
    for n in range(len(lista_tickets)):
        print("______________________________________")
        print("Ticket número ", n+1)
        print("********************")
        print("Id del ticket : ", lista_tickets[n].id_ticket)
        print("Id del evento : ", lista_tickets[n].id_evento)
        print("Número de entrada: ", lista_tickets[n].numero_de_entrada)
        print("Estado del ticket: ", lista_tickets[n].estado)
        
    return lista_tickets
        
#Generación de IDs a partir del módulo ASCII. La manera de hacerlo compatible con base58 es generándolas en 
#minúsculas para que no haya 'O's mayúsculas y cambiando la 'L' minúscula por una mayúscula.
def generar_id_ticket_aleatoria():
    id = ''.join(choice(ascii_lowercase) for i in range(20))
    id = id.replace('l', 'L')
    return id
    
    
"""
Función para generar n número de eventos en función de los recintos disponibles.

"""
def generar_eventos(n_eventos, lista_recintos):
    lista_eventos = []
    
    lista_tipo_eventos = ['Concierto', 'Obra de teatro', 'Monólogo', 'Performance', 'Concurso']
    
    #Agrupando las ids de todos los recintos 
    lista_id_recinto = []
    for recinto in lista_recintos:
        lista_id_recinto.append(recinto.id_recinto)
        
    for n in range (n_eventos):
        id_evento = str(1111111111+n)
        
        n_recinto = n%len(lista_id_recinto)
        id_recinto = lista_id_recinto[n_recinto]
        
        tipo_evento = n%len(lista_tipo_eventos)
        descripcion = lista_tipo_eventos[tipo_evento]
        
        lista_eventos.append(Evento(id_evento, id_recinto, descripcion, datetime.date.today()))

    return lista_eventos
        
    
"""
Función para generar recintos. Se podría parameterizar, pero por brevedad he generado manualmente dos recintos específicos.

"""
def generar_recintos():
    #las coordenadas son de Madrid y Berlín, respectivamente (ciudades conocidas por su gran ambiente nocturno :D)
    lista_recintos = [Recinto('MADRD', 40.416729, -3.703339), Recinto('BERLN', 52.520008, 13.404954)]
    return lista_recintos


# In[21]:


#Código de testeo para generar los recintos, eventos y tickets

recintos = generar_recintos()
eventos = generar_eventos(7, recintos)
tickets = generar_tickets(100, eventos)


# In[22]:


"""
Clase que recopila información sobre un lote específico de recintos, eventos y tickets.

"""

class InformacionEvento:
        
    def __init__(self, lista_tickets, lista_eventos, lista_recintos):
        self.lista_tickets = lista_tickets
        self.lista_eventos = lista_eventos
        self.lista_recintos = lista_recintos
       
    #RETO 2
    """
    Función para extraer el porcentaje de asistencia de un evento específico
    
    """
    def extraer_asistencia_por_evento(self, id_del_evento):
        evento_elegido = None
        
        for e in self.lista_eventos:
            if (e.id_evento == id_del_evento): #Seleccionando el evento específico en base a su id
                evento_elegido = e
         
        lista_tickets_evento = []
        
        for t in self.lista_tickets:
            if (t.id_evento == evento_elegido.id_evento): #Llenando una lista con los estados de todos 
                lista_tickets_evento.append(t.estado)     #los tickets de ese evento
        
        n_valido = 0
        n_usado = 0
        for e in lista_tickets_evento:
            if (e=='v'):
                n_valido = n_valido+1   #Contando el número de tickets válidos y usados, respectivamente
            elif (e=='u'):
                n_usado = n_usado+1
                
        print ("Información de tickets para el evento %s en el recinto %s :" 
               % (evento_elegido.descripcion, evento_elegido.id_recinto))
        print ("Número de tickets válidos: ", n_valido)
        print ("Número de tickets usados: ", n_usado)
            
        return n_valido, n_usado
    
    #RETO 3
    """
    Función para extraer el nivel de asistencia en cada evento y recinto
    
    """
    def extraer_asistencia_total(self, lista_eventos):
        lista_validos = []
        lista_usados = []
        
        for evento in lista_eventos:
            valido, usado = self.extraer_asistencia_por_evento(evento.id_evento)
            lista_validos.append(valido)
            lista_usados.append(usado)
        
        return lista_validos, lista_usados
        


# In[23]:


#Código de testeo para la extracción de datos específica

info_eventos = InformacionEvento(tickets, eventos, recintos)
n_validos, n_usados = info_eventos.extraer_asistencia_por_recinto('1111111111')


# In[24]:


#Código de testeo para la extracción de datos general

validos, usados = info_eventos.extraer_asistencia_total(eventos)


# In[50]:


#Visualización de datos para el Reto 3

data = [validos, usados]
X = np.arange(len(eventos))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.3)
ax.bar(X + 0.25, data[1], color = 'r', width = 0.3, align='center')

lista_descripcion = []
for e in eventos:
    nombre = e.descripcion + "\n en recinto \n" + e.id_recinto
    lista_descripcion.append(nombre)
        
x = lista_descripcion
xi = list(range(len(x)))
plt.xticks(xi, x)
plt.setp(ax.get_xticklabels(), fontsize=10, rotation=45) # Etiquetas del eje x

ax.legend(labels=['Tickets válidos', 'Tickets usados']) # Leyenda

