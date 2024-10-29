from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.avl_bin=AVLTree()
        self.avl_object=AVLTree()
        self.avl_search=AVLTree() 

    def add_bin(self, bin_id, capacity):
        bin_instance=Bin(bin_id,capacity)
        bin_instance_1=Bin(bin_id,capacity)
        self.avl_bin.insert_value(bin_instance)
        self.avl_search.insert_value_search(bin_instance_1)
        # print(self.avl_search.root.value.capacity)
        # print(self.avl_search.inorder(self.avl_search.root))

    def add_object(self, object_id, size, color):
        # self.avl_object.insert_value(object_instance)

        if(color==Color.BLUE):
            node=self.avl_search.compact_least(size)
        elif(color==Color.YELLOW):
            node=self.avl_search.compact_greatest(size)
        elif(color==Color.RED):
            node=self.avl_search.largest_least()
        else:
            node=self.avl_search.largest_greatest()
        
        #Some variables
        if not node:
            raise NoBinFoundException
        elif node.value.capacity<size:
            raise NoBinFoundException
        else:
            # if node.value.id == 850:
            #     print(node.value.capacity, size)
            # if object_id == 8586:
            #     print("gay", node.value.id)
            #     print(node.value.capacity)
            #     print(size)
            object_instance=Object(object_id,size,color)
            self.avl_object.insert_value(object_instance)
            old_capacity=node.value.capacity
            bin_id=node.value.id
            object_instance.bin_id_appended=bin_id

            bin_blabla=Bin(bin_id,old_capacity)
            #Updating avl_search
            self.avl_search.delete_value_search(bin_blabla)
            new_bin_instance=Bin(bin_id, old_capacity-size)
            self.avl_search.insert_value_search(new_bin_instance)

            #Finding and updating bin
            #degug
            # print(self.avl_bin.inorder_bin(self.avl_bin.root))
            # print(self.avl_search.inorder(self.avl_search.root))
            # print(bin_id)
            #/debug
            node_bin=self.avl_bin.search(self.avl_bin.root,bin_id)
            node_bin.value.capacity=node_bin.value.capacity-size
            node_bin.value.add_object(object_instance)
            # if object_id == 8586:
            #     print(self.avl_bin.search_value(node.value.id).value.avl_inside_bin.inorder_bin(self.avl_bin.search_value(node.value.id).value.avl_inside_bin.root))
        return
        # raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        node=self.avl_object.search(self.avl_object.root,object_id)
        if(node==None):
            return
        # print(self.avl_object.inorder_bin(self.avl_object.root))
        # if object_id == 9813:
        #     print("gay")
        # if not node:
        #     print(object_id)
        bin_id=node.value.bin_id_appended
        object_size=node.value.size
        object_instance=Object(object_id)
        self.avl_object.delete_value(object_instance)

        #Find the bin and remove object
        node_bin=self.avl_bin.search(self.avl_bin.root,bin_id)
        old_capacity=node_bin.value.capacity
        node_bin.value.capacity=node_bin.value.capacity+object_size
        node_bin.value.remove_object(object_id)


        bin_blabla=Bin(bin_id,old_capacity)
        #Update avl_search
        self.avl_search.delete_value_search(bin_blabla)
        new_bin_instance=Bin(bin_id, old_capacity+object_size)
        self.avl_search.insert_value_search(new_bin_instance)

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        # bin_blabla=Bin(bin_id,0)
        node=self.avl_bin.search(self.avl_bin.root,bin_id)
        '''idhar kya karu?'''
        return (node.value.capacity, node.value.avl_inside_bin.inorder_bin(node.value.avl_inside_bin.root))

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        node=self.avl_object.search(self.avl_object.root,object_id)
        if not node:
            return None
        return node.value.bin_id_appended
    
    