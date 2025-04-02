import uuid

class Item:
    # generate random id's
    def __init__(self, id=None):
        if id is None:
            self.id = uuid.uuid4().int
            # random_num = ""
            # for i in range(32):
            #     random_num += str(random.randint(0, 9))
            # self.id = int(random_num)
        else:
            self.id = id
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."