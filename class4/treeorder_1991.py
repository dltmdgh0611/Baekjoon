class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(tree):
    print(tree.data, end='')
    if tree.left != '.' : preorder(tree.left)
    if tree.right != '.' : preorder(tree.right)

def inorder(tree):
    if tree.left != '.' : inorder(tree.left)
    print(tree.data, end='')
    if tree.right != '.' : inorder(tree.right)

def postorder(tree):
    if tree.left != '.' : postorder(tree.left)
    if tree.right != '.' : postorder(tree.right)
    print(tree.data, end='')
    
n = int(input())
treelist = []
for _ in range(n):
    node, left, right = list(input().split())
    t = tree(node)
    t.left = left
    t.right = right
    treelist.append(t)

for i in range(n):
    for j in range(n):
        if treelist[i].data == treelist[j].left: treelist[j].left = treelist[i]
        elif treelist[i].data == treelist[j].right: treelist[j].right = treelist[i]

preorder(treelist[0])
print()
inorder(treelist[0])
print()
postorder(treelist[0])
    

        