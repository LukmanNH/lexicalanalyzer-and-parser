from lexical_analizer import*
from parser import*


Z = ["they", "he", "she"]
H = ["is", "are"]
V = ["eating", "playing", "buying", "hunting", "learning"]
O = ["grapes", "games", "seeds", "lunch", "science"]
S = [Z,H,V,O]

sentence = input()
nodeList = createNodeList()
nodeList = setRelations(nodeList)

if analizeLexicon(sentence, nodeList) == True:
    arrayifiedWord = arrayify(sentence)
    parse(arrayifiedWord, S)