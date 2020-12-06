#!/usr/bin/env python
# coding: utf-8

# In[59]:


import base58


# In[62]:


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
            if (len(id_ticket) != 20):
                print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
                self.id_ticket = "invalid"
        except:
            print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
            self.id_ticket = "invalid"
            
            
        #id_evento type check
        try:
            base58.b58decode(id_evento)
            self.id_evento = id_evento
            if (len(id_evento) != 10):
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
        if (estado != 'v' and estado != 'u'):
            print("Error - 'estado' debe ser 'v' o 'u' ")
            self.estado = "invalid"
            
    


# In[64]:


ticket1 = Ticket("1111111111aaaaaaaaaa", "1111111111", 100, 'v')
print(ticket1.id_ticket)
print(ticket1.id_evento)
print(ticket1.numero_de_entrada)
print(ticket1.estado)


# In[ ]:


class Evento:
    def __init__(self, id_evento, id_recinto, descripcion, fecha):
        self.id_evento = id_evento
        self.id_recinto = id_recinto
        self.descripcion = descripcion
        self.fecha = fecha
        
        
        #id_ticket type check
        try:
            base58.b58decode(id_ticket)
            self.id_ticket = id_ticket
            if (len(id_ticket) != 20):
                print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
                self.id_ticket = "invalid"
        except:
            print("Error - 'id_ticket' debe ser un texto en Base58 de longitud 20")
            self.id_ticket = "invalid"
            
            
        #id_evento type check
        try:
            base58.b58decode(id_evento)
            self.id_evento = id_evento
            if (len(id_evento) != 10):
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
        if (estado != 'v' and estado != 'u'):
            print("Error - 'estado' debe ser 'v' o 'u' ")
            self.estado = "invalid"


# In[ ]:




