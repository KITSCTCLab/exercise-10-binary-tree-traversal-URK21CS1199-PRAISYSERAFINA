class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    if root not None:
        if new_value>root.data:
            if root.right_child is None:
                root.right_child=Node(new_value)
            else:
                root.right_child=insert(root.right_child,new_value)
        else:
            if root.left_child is None:
            root.left_child=Node(new_value)
            else:
            root.left_child=insert(root.left_child,new_value)
    else:
        root=Node(new_value)
    
                             


def inorder(root) -> None:
    # Write your code here
    inorder(root.left_child)
    print(root.data)
    inorder(root.right_child)


def preorder(root) -> None:
    # Write your code here
    print(root.data)
    preorder(root.left_child)
    preorder(root.right_child)


def postorder(root) -> None:
    # Write your code here
     postorder(root.left_child)
     postoder(root.right_child)
     print(root.data)


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
