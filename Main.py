from pptree import *

def TopDownParsing(nonTerminal,terminal,initialState,productions,queue,string,depth,Tree):
    print("TopDownParsing Method")
    dicDepth = {}
    queue.append(initialState)
    dicDepth[initialState] = 0
    devide = []
    found = False
    uwv = ""
    while queue and not found:
        q = queue.pop(0)
        if dicDepth[q] + 1 > depth:
            break
        i=0
        done = False
        for x in range(len(q)):
            if q[x].isupper():
                q = q.partition(q[x])
                break      
        while not done and not found:
            for j in productions[q[1]]:
                devide.clear()
                w = j
                checkIfmatches = q[0]
                devide.append(q[0])
                devide.append(w)
                devide.append(q[2])
                uwv = listToString(devide)
                allTerminal = 0
                for minus in range(len(uwv)):
                    if uwv[minus] in terminal:
                        allTerminal = allTerminal + 1
                matches = True
                for x in range(len(checkIfmatches)):
                    if len(checkIfmatches) > len(string):
                        matches = False
                        break
                    elif checkIfmatches[x] != string[x]:
                        matches = False
                        break        
                if allTerminal < len(uwv) and matches:
                    queue.append(uwv)
                    append_value(Tree,listToString(q),uwv)
                    dicDepth[uwv] = dicDepth[listToString(q)] + 1
                    if uwv == string:
                        found = True

                elif matches:
                    append_value(Tree,listToString(q),uwv)
                    if uwv == string:
                        found = True          
            done = True  
                   
    if found:
        print("------------------String accepted------------------")
    else:
        print("----------------String NOT accepted----------------")   
    #print nice tree (missing)
    tempRoot = Node(initialState)
    print_tree_method_recursive(Tree,initialState,tempRoot)
    print_tree(tempRoot,horizontal=True)
    


def listToString(devide):  
    str1 = ""    
    for x in devide:  
        str1 += x    
    return str1

def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]

def print_tree_method_recursive(Tree,key,parent):
    for x in Tree:
        for j in Tree[x]:
            if x == key:
                nod = Node(j,parent)
                print_tree_method_recursive(Tree,j,nod)

print("Select the text file (e.g. test1, test2,test3,test4)")
txtVal = input()
print("String to evaluate")
string = input()
print("indicate the maximun depth")
depth = int(input())

productions = {}
queue = []
Tree = {}

with open(txtVal + ".txt") as f:
    nonTerminal = f.readline().split(",")
    nonTerminal[len(nonTerminal)-1] = nonTerminal[len(nonTerminal)-1].strip()
    terminal = f.readline().split(",")
    terminal[len(terminal)-1] = terminal[len(terminal)-1].strip()
    initialState = f.readline().strip() 
    for i in range(len(nonTerminal)*3):
            ste = f.readline()
            if not ste:
                break
            ste = ste.split("->")
            ste[len(ste)-1] = ste[len(ste)-1].strip()
            if ste[0].isupper():
                append_value(productions,ste[0],ste[1])
            ste.clear()

TopDownParsing(nonTerminal,terminal,initialState,productions,queue,string,depth,Tree)

