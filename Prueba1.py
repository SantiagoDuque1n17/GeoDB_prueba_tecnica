#!/usr/bin/env python
# coding: utf-8

# In[76]:


import base58
import datetime
from random import choice
from random import randint
from string import ascii_lowercase
from dateutil.parser import parse


# In[77]:


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
            
    


# In[78]:


ticket1 = Ticket("1111111111aaaaaaaaaa", "1111111111", 100, 'v')
print(ticket1.id_ticket)
print(ticket1.id_evento)
print(ticket1.numero_de_entrada)
print(ticket1.estado)


# In[79]:


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


# In[80]:


evento1 = Evento("1111111111", "aaaaa", "hola hola hola", datetime.date.today())
print()
print(evento1.id_evento)
print(evento1.id_recinto)
print(evento1.descripcion)
print(evento1.fecha)


# In[81]:


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
            
        


# In[82]:


recinto1 = Recinto('11111', 58.123123, 78.97328273)

print(recinto1.id_recinto)
print(recinto1.latitud)
print(recinto1.longitud)


# In[93]:


#RETO 1

def generar_tickets(n_tickets, lista_eventos):
    lista_tickets = []
    
    lista_id_eventos = []
    for evento in lista_eventos:
        lista_id_eventos.append(evento.id_evento)
        
    numero_actual = 1
    
    #Ticket: id_ticket, id_evento, numero_de_entrada, estado
    for n in range (n_tickets):
        
        id_ticket = generar_id_ticket_aleatoria()
        
        n_evento = n%len(lista_id_eventos)
        id_evento = lista_id_eventos[n_evento]
        
        #Para el número de entrada entiendo que es un número único para cada evento 
        #e.g.: puede (debe) haber varios tickets con el mismo número, porque es secuencial en función del evento
        #De momento voy a implementarlo para que sea en función del ticket y no del evento, igual lo cambio más tarde
        numero_de_entrada = numero_actual
        numero_actual = numero_actual+1
        
        lista_estados = ['v', 'u']
        estado = lista_estados[n%2]
        
        lista_tickets.append(Ticket(id_ticket, id_evento, numero_de_entrada, estado))
        
    for n in range(len(lista_tickets)):
        print("______________________________________")
        print("Ticket número ", n)
        print("********************")
        print("Id del ticket : ", lista_tickets[n].id_ticket)
        print("Id del evento : ", lista_tickets[n].id_evento)
        print("Número de entrada: ", lista_tickets[n].numero_de_entrada)
        print("Estado del ticket: ", lista_tickets[n].estado)
        
#Generación de IDs a partir del módulo ASCII. La manera de hacerlo compatible con base58 es generándolas en 
#minúsculas para que no haya 'O's mayúsculas y cambiando la 'L' minúscula por una mayúscula, no sé si es un poco stinky.
def generar_id_ticket_aleatoria():
    id = ''.join(choice(ascii_lowercase) for i in range(20))
    id = id.replace('l', 'L')
    return id
    
    
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
        
    
def generar_recintos():
    #las coordenadas son de Madrid y Berlín, respectivamente (ciudades conocidas por su gran ambiente nocturno :D)
    lista_recintos = [Recinto('MMMMM', 40.416729, -3.703339), Recinto('BBBBB', 52.520008, 13.404954)]
    return lista_recintos


# In[94]:


generar_tickets(10, generar_eventos(7, generar_recintos()))


# In[ ]:




