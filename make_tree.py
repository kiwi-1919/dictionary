import tree

if __name__ == '__main__':
    string = input('reset:1;show_node:2')
    if string == '1':
        tree.reset(root='*.txt')
    elif string == '2':
        tree.show_node(input('node_tag'))
    else:
        print('wait for a minute')
