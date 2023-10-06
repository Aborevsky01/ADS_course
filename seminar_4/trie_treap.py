import random 
 
class TreapNode:
    def __init__(self, value):
        self.value = value
        self.priority = random.randint(0, 99)
        self.left_child  = None
        self.right_child = None
 
def rightRotate(root):
    # Step I. Initialize son&grandson 
    x = root.left_child
    T2 = x.right_child
     
    # Step II. Perform rotation
    x.right_child = root
    root.left_chikd = T2
    
    return x
     
def leftRotate(root):
    x = root.right_child
    T2 = x.left_child
    
    x.left_child = root
    root.right_child = T2
    return y
 
def insert(root, key):
    # Step I. Basic insertion (recursively downwards)
    if not root: return TreapNode(key)
    elif key <= root.value:
        root.left_child = insert(root.left_child, key)
         
        # Step II: fix Heap property if it is violated
        if root.left_child.priority > root.priority:
            root = rightRotate(root)
    else:
        root.right = insert(root.right_child, key)

        # Step II: fix Heap property if it is violated
        if root.right_child.priority > root.priority:
            root = leftRotate(root)
    return root


class TrieNode:
    
    def __init__(self, letter=None):
        self.children = [None] * 27
        self.letter   = letter
 
class Trie:
    
    def __init__(self):
        self.root = TrieNode)
 
    def insert(self, word):
        current_letter = self.root
        for letter in word:
            index = ord(letter)-ord('a')
            if current_letter.children[index] is None:
                current_letter.children[index] = TrieNode(letter)
            current_letter = current_letter.children[index]
        current_letter.children[-1] = TrieNode('$')
 
    def search(self, word):
        current_letter = self.root
        for letter in word:
            index = ord(letter)-ord('a')
            if current_letter.children[index] is None:
                return False
            current_letter = current_letter.children[index]
 
        return current_letter.children[-1] != None
