class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None: return Node(key)

    if key < root.key: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)

    return root

def minValueNode(node):
    current = node
    while(current.left is not None): current = current.left
    return current


def deleteNode(root, key):
    if root is None: return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if   root.left  is None: root = root.right
        elif root.right is None: root = root.left
        else:
            root = minValueNode(root.right)
            root.right = deleteNode(root.right, root.key)

    return root

def searchNode(root, key, func_type='recursive'):
    if func_type == 'recursive':
        if root is None or key == root.key: return root
        elif key < root.key: return searchNode(root.left, key)
        elif key > root.key: return searchNode(root.right, key)
    elif func_type == 'iterative':
        while not (root is None or key == root.key):
            if key < root.key: root = root.left
            if key > root.key: root = root.right
        return root
    
