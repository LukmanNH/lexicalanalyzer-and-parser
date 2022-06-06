class node():
    def __init__(self, id):
        self.id = id
        self.next = []
        self.edgeForNext = []
        self.finalStatus = False
    
    def addCon(self, newNext, newEdgeForNext):
        self.next.append(newNext)
        self.edgeForNext.append(newEdgeForNext)

    def setFinalStatus(self, newStatus):
        self.finalStatus = newStatus

    def isConExist(self, toBeSearched):
        i = 0
        while i != len(self.edgeForNext):
            if toBeSearched == self.edgeForNext[i]:
                return self.next[i]
            i = i + 1
        if i == len(self.edgeForNext):
            return -1
            

def createNodeList():
    nodes = []
    for i in range(56):
        newNode = node(i)
        nodes.append(newNode)
    return nodes

def setRelations(nodes):
    nodes[55].setFinalStatus(True)
    nodes[55].addCon(55, " ")

    nodes[0].addCon(0, " ")
    nodes[0].addCon(1, "t")
    nodes[1].addCon(2, "h")
    nodes[2].addCon(3, "e")
    nodes[3].addCon(4, "y")
    nodes[4].setFinalStatus(True)
    nodes[4].addCon(55, " ")
    nodes[55].addCon(1, "t")
    nodes[0].addCon(5, "s")
    nodes[5].addCon(6, "h")
    nodes[6].addCon(7, "e")
    nodes[7].setFinalStatus(True)
    nodes[7].addCon(55, " ")
    nodes[55].addCon(5, "s")

    nodes[0].addCon(8, "i")
    nodes[8].addCon(9, "s")
    nodes[9].setFinalStatus(True)
    nodes[9].addCon(55, " ")
    nodes[55].addCon(8, "i")
    nodes[0].addCon(10, "a")
    nodes[10].addCon(6, "r")
    nodes[55].addCon(10, "a")

    nodes[0].addCon(11, "e")
    nodes[11].addCon(12, "a")
    nodes[12].addCon(13, "t")
    nodes[13].addCon(14, "i")
    nodes[14].addCon(15, "n")
    nodes[15].addCon(16, "g")
    nodes[16].setFinalStatus(True)
    nodes[16].addCon(55, " ")
    nodes[55].addCon(11, "e")
    nodes[0].addCon(17, "h")
    nodes[17].addCon(18, "u")
    nodes[18].addCon(12, "n")
    nodes[55].addCon(17, "h")
    nodes[0].addCon(19, "b")
    nodes[19].addCon(20, "u")
    nodes[20].addCon(13, "y")
    nodes[55].addCon(19, "b")
    nodes[0].addCon(21, "p")
    nodes[21].addCon(22, "l")
    nodes[22].addCon(20, "a")
    nodes[55].addCon(21, "p")
    nodes[0].addCon(23, "l")
    nodes[23].addCon(24, "e")
    nodes[24].addCon(25, "a")
    nodes[25].addCon(26, "r")
    nodes[26].addCon(13, "n")
    nodes[17].addCon(27, "e")
    nodes[27].setFinalStatus(True)
    nodes[27].addCon(55, " ")
    nodes[55].addCon(17, "h")

    nodes[23].addCon(28, "u")
    nodes[28].addCon(29, "n")
    nodes[29].addCon(30, "c")
    nodes[30].addCon(31, "h")
    nodes[31].setFinalStatus(True)
    nodes[31].addCon(55, " ")
    nodes[55].addCon(23, "l")

    nodes[0].addCon(32, "g")
    nodes[32].addCon(33, "r")
    nodes[33].addCon(34, "a")
    nodes[34].addCon(35, "p")
    nodes[35].addCon(36, "e")
    nodes[36].addCon(37, "s")
    nodes[37].setFinalStatus(True)
    nodes[37].addCon(55, " ")
    nodes[55].addCon(32, "g")
    nodes[32].addCon(38, "a")
    nodes[38].addCon(35, "m")
    nodes[5].addCon(40, "e")
    nodes[40].addCon(41, "e")
    nodes[41].addCon(36, "d")
    nodes[5].addCon(42, "c")
    nodes[42].addCon(43, "i")
    nodes[43].addCon(44, "e")
    nodes[44].addCon(45, "n")
    nodes[45].addCon(46, "c")
    nodes[46].addCon(47, "e")
    nodes[47].setFinalStatus(True)
    nodes[47].addCon(55, " ")

    return nodes

def analizeLexicon(words, finAuto):
    ptr = 0
    for i in range(len(words)):
        if finAuto[ptr].isConExist(words[i]) != -1:
            ptr = finAuto[ptr].isConExist(words[i])
        else:
            print("Lexicon Error")
            return False
    if finAuto[ptr].finalStatus == True:
        print("Lexicon OK")
        return True