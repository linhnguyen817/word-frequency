class Tree_Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    # Inserts key as node into AVL tree
    # Returns new root of balanced tree with key inserted
    def insert(self, root, key):
        # 1. Locate correct subtree to insert key
        if not root:    # Key is first node in tree
            return Tree_Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height of tree root with new node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # 3. Re-balance tree if needed depending on 4 different cases
        #    Tree isn't balanced if height difference between left and right subtrees is not 0 nor 1
        balance_factor = self.get_balance(root)

        # If left side is heavier
        if balance_factor > 1:  
            # a. Left Left 
            if self.get_balance(root.left) >= 0:    
                return self.right_rotate(root)
            # b. Left Right
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # If right side is heavier
        elif balance_factor < -1:
            # c. Right Right
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            # d. Right Left
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        # Else tree is already balanced
        return root

    # Perform left rotation at node z and return new root
    def left_rotate(self, z):
        new_root = z.right
        temp = new_root.left
        new_root.left = z
        z.right = temp

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    # Perform right rotation at node z and return new root
    def right_rotate(self, z):
        new_root = z.left
        temp = new_root.right
        new_root.right = z
        z.left = temp

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    # Get height of node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor of node = left subtree height - right subtree height
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def print_in_order(self, root):
        if not root:
            return

        self.print_in_order(root.left)
        print("{0} ".format(root.key), end="")
        self.print_in_order(root.right)

if __name__ == '__main__':
    tree = AVL_Tree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    tree.print_in_order(root)
    print()