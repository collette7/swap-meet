class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory
        
    # Adds an item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # Removes an item from the vendors inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        if item in self.inventory:
            self.inventory.remove(item)
        return item
    
    # Searche through the vendor's inventory for an item with a matching id
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
