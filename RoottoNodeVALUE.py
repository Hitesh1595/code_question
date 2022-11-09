# path of root to distance in true and false


def disttonode(root,target,path):
    if root is None:
        return False
    
    path.append(root.data)
    
    if root.data == target:
        return True
    
        
    if disttonode(root.left,target,path) or disttonode(root.right,target,path):
        return True
        
    path.pop()
    
    return False

disttonode(root,4,[])