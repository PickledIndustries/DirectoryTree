"""
Author: Daniel Garnier
Date:   17th Dec 2018


Usage Example: 

rootPath = "C:/Users/daniel.garnier/Documents/Maya"
treeClass = tree.directoryTree(rootPath)

# get a dictionary of the full folder/file hierarchy 
Dict = treeClass.getDictOfRoot()

# print out the hierarchy  folder structure in a clean/pretty format
treeClass.printTree(printDirectory = False)
treeClass.printTree(printDirectory = True)

"""
import os



class node():
    """
        This is a class to break out each node as an instance for usability.
        
        Param: parent, instance of node(), or None if its the first node(root node)
        Param: name, string of the Folder name
        Param: files, list of string file names
        Param: children, list of node() instances(this gets appended to as new children
               nodes are created)
        Param: directory = The directory of the current nodes folder + node.name
    """
    def __init__(self, name, parent = None):
        self.parent = parent
        self.name = name
        self.files = None
        self.children = None

        

class directoryTree():
    """
        This class was built as a fast and intuitive version of what os.walk does, but 
        gives a dictionary. Also runs a lot faster!
        
        Param: rootPath, path you want to list everything for.
    """
    def __init__(tree, rootPath):
        tree.printDepth = 0
        tree.dictDepth = ""
        tree.root = node(rootPath, None)
        tree.root.directory = str(tree.root.name)
        
        tree.fillParent(tree.root)
        
    def fillParent(tree, parent):
        """
            Loops through all children folders of the directory tree 
            
            param: parent, instance of class node()
        """
        filsFolds = os.listdir(parent.directory)
        
        files = [f for f in filsFolds if os.path.isfile("/".join([parent.directory,f]))]
        folders = [f for f in filsFolds if os.path.isdir("/".join([parent.directory,f]))]
        
        parent.files = files
        parent.children = None
        
        thereIsChildren = True
        
        while thereIsChildren:
            if parent.children ==[]:
                thereIsChildren = False
            else:
                if parent.children == None:
                    parent.children = []
            
                for child in folders:
                    nChild = node(child, parent)
                    nChild.directory = "/".join([nChild.parent.directory, nChild.name])
                    parent.children.append(nChild)
                    if nChild.children == None:
                        tree.fillParent(nChild)
                thereIsChildren = False
        
        
        
    def printTree(tree, fromNode=None, printDirectory = False):
        """
            Used to print the entire tree from the root OR the given node
            
            param: fromNode, instance of class node()
            param: printDirectory, Bool, if True, it will print directories instead of folder names
        """
        if fromNode == None:
            fromNode = tree.root
        print fromNode.name
        tree.printChildrenOfNode(fromNode, printDirectory)
        
        
        
    def printChildrenOfNode(tree, node, printDirectory = False):
        """
            Used to print all children, from the root OR the given node
            
            param: fromNode, instance of class node()
            param: printDirectory, Bool, if True, it will print directories instead of folder names
        """
        if node.children:
            for child in node.children:
                tree.printDepth = tree.printDepth+1
                if printDirectory:
                    print ("|   "*tree.printDepth), child.directory
                else:
                    print ("|   "*tree.printDepth), child.name
                if child.children:
                    tree.printChildrenOfNode(child, printDirectory)
                else:
                    tree.printDepth = tree.printDepth-1
                
            tree.printDepth = tree.printDepth-1
    
    
    
    def getDictOfRoot(tree, fromNode=None):
        """
            Used to get a full dictionary of all folders within the root directory
            
            param: fromNode, instance of class node()
            
            returns a dictionary of: {
                "//path/to/root/directory/given/to/the/class": {
                    "__files__": [
                        "fileInTheRootDir.txt"
                    ],
                    "child1FolderName":{
                        "__files__": [
                            "fileInChild1Dir.txt"
                        ],
                        "child2FolderName":{
                            "__files__": [
                                "fileInChild2Dir.txt"
                            ],
                            
                        },
                        
                    },
                },
            }
        """
        if fromNode == None:
            fromNode = tree.root
        Dict = {fromNode.name:{"__files__":fromNode.files}}
        Dict = tree.getChildren(fromNode, Dict)
        return Dict
        
        
        
    def getChildren(tree, node, Dict):
        """
            Used to get all children nodes within the given node.
            
            param: node, instance of class node()
            param: Dict, A base dictionary that  == {tree.root.name:{}}
        """
        if node.children:
            for child in node.children:
                tree.dictDepth = tree.dictDepth+"$$"+child.name
                dictString = "Dict[tree.root.name]"
                for each in [e for e in tree.dictDepth.split("$$") if not e == ""]:
                    dictString+="['{}']".format(each)
                exec(dictString+"={'__files__':"+str(child.files)+"}")
                    
                if child.children:
                    tree.getChildren(child, Dict)
                else:
                    A, B = tree.dictDepth.rsplit("$$"+child.name,1)
                    tree.dictDepth = A+B
            try:
                A, B = tree.dictDepth.rsplit("$$"+node.name,1)
                tree.dictDepth = A+B
            except:
                pass
        return Dict
        
    
    
    
    
    
    