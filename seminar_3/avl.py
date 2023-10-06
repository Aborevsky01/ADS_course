class AVLNode: 
    def __init__(self, value): 
        self.value = value 
        self.left_child  = None
        self.right_child = None
        self.height = 1
  


def insert(root, key): 
    # Step I. Perform basic BST insertion
    if not root: return AVLNode(key) 
    elif key < root.value : root.left_child  = insert(root.left_child, key) 
    elif key >= root.value: root.right_child = insert(root.right_child, key) 

    # Step II. Update the height & Calculate balance factor for the root
    root.height = 1 + max(getHeight(root.left_child), getHeight(root.right_child)) 
    balance = getBalance(root) 

    # Step III. Check for balance factor issues
    if balance > 1 and key < root.left_child.value: 
        return rightRotate(root) 

    if balance < -1 and key > root.right_child.value: 
        return leftRotate(root) 

    if balance > 1 and key > root.left_child.value: 
        root.left_child = leftRotate(root.left_child) 
        return rightRotate(root) 

    if balance < -1 and key < root.right_child.value: 
        root.right_child = rightRotate(root.right_child) 
        return leftRotate(root) 

    return root 

def leftRotate(z): 
    # Step I. Initialize nodes (son & grandson) 
    y = z.right_child 
    T2 = y.left_child 

    # Step II. Perform rotation 
    y.left_child = z 
    z.right_child = T2 

    # Step III. Update heights 
    z.height = 1 + max(getHeight(z.left_child), getHeight(z.right_child)) 
    y.height = 1 + max(getHeight(y.left_child), getHeight(y.right_child)) 

    return y 

def rightRotate(z):
    
    y = z.left_child 
    T3 = y.right_child

    y.right_child = z 
    z.left_child = T3 

    z.height = 1 + max(getHeight(z.left_child), getHeight(z.right_child)) 
    y.height = 1 + max(getHeight(y.left_child), getHeight(y.right_child)) 

    return y 

def getHeight(root): 
    if not root: return 0
    return root.height 

def getBalance(root): 
    if not root: return 0
    return getHeight(root.left_child) - getHeight(root.right_child) 
