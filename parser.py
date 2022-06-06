def arrayify(sentence):
    toBeReturned = []
    ptr = 0
    i = 0
    while i < len(sentence):
        if sentence[i] != " ":
            ptr = i
            toBeAppended = ""
            for j in range(ptr, len(sentence)):
                if sentence[j] != " " and j != len(sentence) - 1:
                    toBeAppended = toBeAppended + sentence[j]
                else:
                    i = j
                    break
            toBeReturned.append(toBeAppended)
        i = i + 1
    toBeReturned[len(toBeReturned) - 1] = toBeReturned[len(toBeReturned) - 1] + sentence[len(sentence) - 1]
    return toBeReturned

def isItIn(checkThis, theList):
    for i in range(len(theList)):
        if checkThis == theList[i]:
            return True
    return False

def parse(toBeParsed, grammar):
    i = 0
    while i < len(grammar):
        if isItIn(toBeParsed[i], grammar[i]) == False:
            # print("Parser Error")
            return False
            break
        i = i + 1
    if i == len(grammar):
        # print("Parser OK")
        return True
    return

def parse2(toBeParsed, S, Z, H, V, O):
    S.append(O)
    S.append(V)
    S.append(H)
    S.append(S)
    staccc = []
    staccc.append("#")
    ptr = 0
    print(staccc)
    staccc.append(O)
    staccc.append(V)
    staccc.append(H)
    staccc.append(S)

    print(staccc)
    print(O)
#    while len(staccc) != 0:
#        if staccc[len(staccc) - 1] == "#":
#            if ptr == 0:
#                staccc.append(O)
#                staccc.append(V)
#                staccc.append(H)
#                staccc.append(S)
#            else:
#                staccc.pop()
#        elif staccc[len(staccc) - 1] == S:
#            print(toBeParsed[ptr], staccc[len(staccc) - 1])
#            if isItIn(toBeParsed[ptr], staccc[len(staccc) - 1]) == True:
#                staccc.pop()
#                ptr = ptr + 1
#            else:
#                print("Parser Error S")
#                break
#        elif staccc[len(staccc) - 1] == H:
#            if isItIn(toBeParsed[ptr], staccc[len(staccc) - 1]) == True:
#                staccc.pop()
#                ptr = ptr + 1
#            else:
#                print("Parser Error H")
#                break
#        elif staccc[len(staccc) - 1] == V:
#            if isItIn(toBeParsed[ptr], staccc[len(staccc) - 1]) == True:
#                staccc.pop()
#                ptr = ptr + 1
#            else:
#                print("Parser Error V")
#                break
#        elif staccc[len(staccc) - 1] == O:
#            if isItIn(toBeParsed[ptr], staccc[len(staccc) - 1]) == True:
#                staccc.pop()
#                ptr = ptr + 1
#            else:
#                print("Parser Error O")
#                break
#    return