from avl import AVLTree
from object import Object
class Bin:
    def __init__(self, bin_id, capacity):
        self.id=bin_id
        self.capacity=capacity
        self.avl_inside_bin= AVLTree()

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.avl_inside_bin.insert_value(object)

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        object_instance=Object(object_id,0,0)
        self.avl_inside_bin.delete_value(object_instance)

