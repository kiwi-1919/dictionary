from treelib import *
import pickle
import os


class node:
    def __init__(self, parent, name, tree):
        self.tree = tree
        self.parent = parent
        self.name = name

    def add(self):
        try:
            self.tree.create_node(self.name, self.name, parent=self.parent)
        except:
            raise Exception('MakeNodeError')

    def show(self):
        self.tree.subtree(self.name).show()


def reset(root=None):
    try:
        os.remove('data.tree')
    except:
        pass
    tree = Tree()
    tree.create_node(root, root)
    while True:
        if input('continue:y/o').lower() == 'y':
            n = node(parent=input('parent'), name=input('name'), tree=tree)
            n.add()
        else:
            break
    tree.show()
    with open('data.tree', 'wb') as data:
        pickle.dump(tree, data)


def show_node(name):
    with open('data.tree', 'rb') as data:
        tree = pickle.load(data)
        n = node(parent=None, name=name, tree=tree)
        n.show()


def add_node(name, parent):
    with open('data.tree', 'rb') as rf:
        tree = pickle.load(rf)
        n = node(parent=parent, name=name, tree=tree)
        n.add()
    with open('data.tree', 'wb') as wf:
        pickle.dump(tree, wf)
