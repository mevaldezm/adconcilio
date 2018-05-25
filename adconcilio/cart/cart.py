    
class Item:
    'Clase base del Shopping Cart'
    precio = 0.00
    descripcion = ''
    
    
    def __init__(self, descripcion, precio):
    
        self.descripcion = descripcion
        self.precio = precio

    def getDescripcion(self):
        return self.descripcion
    
    def getPrecio(self):
        return self.precio

    def AddItem(self, item):
        return
        
    def RemoveItem(self, item):
        return
        
    def getItems(self):
       return
    
    def __str__(self):
        return '{0},... {1:.2f}'.format(self.descripcion, self.getPrecio())
    

class Part(Item):

    'Entry unitario'
              
    def getItems(self):
        return [0]
   
   
class Bundle(Item):
    
    __items = []

    def __init__(self, descripcion):
    
        Item.descripcion = descripcion
        Item.precio = 0.0
        
    def AddItem(self, item):
        self.__items.append(item)

    def RemoveItem(self, item):
        self.__items.remove(item) 

    def getItems(self):
        return self.__items

    def getPrecio(self):
        total = 0.0
        for item in self.__items:
            total += item.precio
        return total
