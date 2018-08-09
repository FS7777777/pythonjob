# import os
# from tests import test_yang
# from yang import Create_app

# if __name__=='__main__':
#     # test_yang.pytest.main('-v -s')
#     Create_app().run()

tree_node={
    "_data":'root',
    '_left':{'_data':'left1','_left':{'_data':'left2'},'_right':{'_data':'right2',}},
    '_right':{'_data':'right1','_right':{'_data':'right3',}}
}

def deep_node(tree_node):
    if tree_node is not None:
        print(tree_node['_data'])
        if '_left' in tree_node.keys():
            deep_node(tree_node['_left'])
        if '_right' in tree_node.keys():
            deep_node(tree_node['_right'])

print(deep_node(tree_node))
        
    