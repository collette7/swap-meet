from swap_meet.item import Item
class Electronics(Item):
        
    def __init__(self, id=None, condition=0, type_="Unknown"):
        super().__init__(id=id, condition=condition)
        self.type = type_
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

