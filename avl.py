from node import Node
from exceptions import NoBinFoundException

def comp_1(val_1, val_2):
    if(val_1.id > val_2.id):
        return True
    else:
        return False
    
def comp_2(val_1, val_2):
    if(val_1.capacity > val_2.capacity):
        return True
    elif(val_1.capacity < val_2.capacity):
        return False
    else:
        return comp_1(val_1,val_2)
    
def comp_3(val_1,val_2):
    if(val_1.capacity > val_2.capacity):
        return True
    elif(val_1.capacity < val_2.capacity):
        return False
    else:
        return comp_1(val_2,val_1)

class AVLTree:
    def __init__(self, comparator=comp_1,comparator1=comp_2):
        self.comparator = comp_1
        self.comparator1 = comp_2
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif self.comparator(root.value, value):
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left)>=0:
            # print('a')
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right)<=0:
            # print('b')
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left)<0:
            # print('c')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right)>0:
            # print('d')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def insert_bin_search(self, root, value):
        if not root:
            return Node(value)
        elif self.comparator1(root.value, value):
            root.left = self.insert_bin_search(root.left, value)
        else:
            root.right = self.insert_bin_search(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left)>=0:
            # print('a')
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right)<=0:
            # print('b')
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left)<0:
            # print('c')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right)>0:
            # print('d')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root

        if self.comparator(root.value, value):
            root.left = self.delete(root.left, value)
        elif self.comparator(value, root.value):
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_search(self, root, value):
        if not root:
            return root

        if self.comparator1(root.value, value):
            root.left = self.delete_search(root.left, value)
        elif self.comparator1(value, root.value):
            root.right = self.delete_search(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete_search(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value.id == value:
            # print('root',root)
            return root
        if root.value.id < value:
            # print('root',root)
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def insert_value_search(self, value):
        self.root = self.insert_bin_search(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def delete_value_search(self, value):
        self.root = self.delete_search(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)

    # def delete_value(self, value):
    #     self.root = self.delete(self.root, value)

    # def search_value(self, value):
    #     return self.search(self.root, value)
    def compact_least(self, size):
        curr = self.root
        ans = None
        while curr is not None:
            if curr.value.capacity >= size:
                ans = curr
                curr = curr.left
            else:
                curr = curr.right
        # if not ans:
        #     raise NoBinFoundException
        return ans
        

    def compact_greatest(self, size):
        curr = self.root
        ans = self.compact_least(size)
        if ans is None:
            return None
        while curr is not None:
            if curr.value.capacity > ans.value.capacity:
                curr = curr.left
            elif curr.value.capacity < ans.value.capacity:
                curr = curr.right
            else:
                if curr.value.id > ans.value.id:
                    ans = curr
                curr = curr.right
        # if not ans:
        #     raise NoBinFoundException
        return ans


    def largest_least(self):
        curr=self.root
        ans=self.largest_greatest()
        max_size = ans.value.capacity
        # if not ans:
        #     raise NoBinFoundException
        while(curr):
            # print('hi')
            if(curr.value.capacity<max_size):
                curr=curr.right
            elif(curr.value.capacity==max_size):
                ans = curr
                curr=curr.left
        # if not ans:
        #     raise NoBinFoundException
        return ans
    
    def largest_greatest(self):
        root=self.root
        while(root.right):
            root=root.right
        # if not root:
        #     raise NoBinFoundException
        return root
    
    def inorder(self, node):
        if node is None:
            return []
        else:
            return self.inorder(node.left) + [node.value.capacity] + self.inorder(node.right)
        

    def inorder_bin(self, node):
        if node is None:
            return []
        else:
            return self.inorder_bin(node.left) + [node.value.id] + self.inorder_bin(node.right)
        

        