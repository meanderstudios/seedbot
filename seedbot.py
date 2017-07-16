def getsentences(theinput):
    sentences = []
    currentsentence = ""
    puncendings = [".","!","?"]
    for i in range(len(theinput)):
        try:
            x = puncendings.index(theinput[i])
            sentences.append(currentsentence)
            currentsentence = ""
        except:
            currentsentence += theinput[i]
    return sentences
def splitby(text,string):
    thelist = text.split()
    newlist = []
    for i in range(len(thelist)):
        if thelist[i]!=string:
            newlist.append(thelist[i])
    return newlist
def seedis():
    theinput = raw_input("Enter Article: ")
    thesentences = getsentences(theinput)
    for i in range(len(thesentences)):
        if "are" in thesentences[i]:
            print splitby(thesentences[i],"are");
        if "is" in thesentences[i]:
            print splitby(thesentences[i],"is");
