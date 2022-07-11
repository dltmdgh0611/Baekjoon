from select import select
from tkinter.tix import Select


class tree:
    def __init__(self, data):
        self.data = data
        self.sons = []
        self.distance = None

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

N = int(input())
trees = []
for i in range(N):
    head, con, dis = list(map(int, input().split()))
    for j in trees:
        if head == j.head:
            j.sons.append(con)
            j.dista

    node = tree(head)
    node.sons.append(con)
    node.distance = dis
    trees.append(node)
pass
