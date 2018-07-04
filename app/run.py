# from yang import Create_app

# app = Create_app()
# if __name__ == '__main__':
#     app.run()

nodes = []

root = dict(pid=-1, id=0, name='root',child=[])

nodes.append(root)

for i in range(1,5):
    node = dict(pid=0, id=i, name='第一级{0}'.format(i),child=[])
    nodes.append(node)


for i in range(6,9):
    node = dict(pid=i-4, id=i, name='第二级{0}'.format(i),child=[])
    nodes.append(node)

for i in range(9,10):
    node = dict(pid=i-3, id=i, name='第三级{0}'.format(i),child=[])
    nodes.append(node)

# print (nodes)

def get_tree(id,nodes):
    if(len(nodes)==0):
        return []
    child_node = []
    for node in nodes:
        if(node['pid'] == id):
            child_node.append(node)
            node['child'].extend(get_tree(node['id'],nodes))
            # nodes.remove(node)
        
    if(len(child_node)==0):
        return []
    return child_node

def get_root(nodes):
    return filter(lambda x:x['pid']==-1,nodes)
li = get_root(nodes)
print(list(li))
# tree = get_tree(-1,nodes)

# print(tree)
# import json
# print(json.dumps(tree))

