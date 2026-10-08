from lexer import convertToTokens
from parser import parse, Node
import argparse

def printTree(treeList, depth = 0):
    if not isinstance(treeList, list):
        printTree([treeList], depth)
        return
    for tree in treeList:
        if isinstance(tree, Node):
            print("    " * depth, tree.type)
            if tree.children != []:
                printTree(tree.children, depth+1)
        else:
            print("    " * depth + str(tree))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    print("inputfile:",args.input)
    
    with open(args.input, "r") as file:
        source = file.read()

    print("contents of file:\n", source)

    tokensList = convertToTokens(source)

    print("Tokens:")
    for token in tokensList:
        print(token)

    print("Tree:")
    
    statements = parse(tokensList)
    printTree(statements)