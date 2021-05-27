import tree

if __name__ == '__main__':
    string = input('reset:1;show_node:2;add_node:3')
    if string == '1':
        tree.reset(root='*.txt')
    elif string == '2':
        tree.show_node(input('node_tag'))
    elif string == '3':
        tree.add_node(name=input('node_tag'), parent=input('parent_name'))
    else:
        print('wait for a minute')
