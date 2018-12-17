# DirectoryTree
#Author: Daniel Garnier
#Date:   17th Dec 2018
#
#Used as an API for any and all folder structure searching, gets hierarchy as Dict
#
#Usage Example: 

rootPath = "C:/Users/daniel.garnier/Documents/Maya"
treeClass = tree.directoryTree(rootPath)

# get a dictionary of the full folder/file hierarchy 
Dict = treeClass.getDictOfRoot()

# print out the hierarchy  folder structure in a clean/pretty format
treeClass.printTree(printDirectory = False)
treeClass.printTree(printDirectory = True)

