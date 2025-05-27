class Vendor:
    # Set up inventory
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
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
    
    # Search through the vendor's inventory for an item with a matching id
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
    #Check both inventories for items, swap items
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # start swaping
        self.remove(my_item)
        other_vendor.add(my_item)

        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    # Check both inventories, grab first items & swap
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(
            other_vendor, my_first_item, their_first_item
        )
    # Get items by category 
    def get_by_category(self, category):
        matching_items = []
        for item in self.inventory:
            if item.get_category() == category:
                matching_items.append(item)
        return matching_items
    
    # Get the item with the best condition in a specific category 
    def get_best_by_category(self, category):
        matching_items = self.get_by_category(category)
        if not matching_items:
            return None
            
        best_item = matching_items[0]
        for item in matching_items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    # Swap best items by category
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return False
            
        their_best = other_vendor.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        
        if not their_best or not my_best:
            return False
        
        return self.swap_items(other_vendor, my_best, their_best)