import re
import pandas as pd

REGEX_SEPARATOR = ",|;|\s+"

tokenList = []
symbolTable = {}
symbolTableFile = open("symbol_table.txt")
for line in symbolTableFile:
    key, value = line.split()
    symbolTable[key] = value

class Tokens: 
    def __init__(self, token, start, type, lineNumber): 
        self.lineNumber = lineNumber
        self.start = start
        self.token = token 
        self.type = type
        
def DisplayTokens():
    df = pd.DataFrame([t.__dict__ for t in tokenList])
    return df

def IsValidToken(token, REGEX_PATTERN):
    matched = re.match(REGEX_PATTERN, token)
    return bool(matched)

def CreateToken(token, start, lineNumber, type):
    obj = Tokens(token, start, type, lineNumber)
    return obj

def IdentifyToken(token):
    for x in symbolTable:
        if(IsValidToken(token, symbolTable[x]) == True):
            return x

def UpdateTokenLst(token, start, lineNumber, type):
    obj = CreateToken(token, start, lineNumber, type)
    tokenList.append(obj)  

def GetTokens(line, lineNumber):
    token = ""
    i = 0
    line += " "
    while i < len(line):
        if(IsValidToken(line[i], REGEX_SEPARATOR) == True):
            token = token.strip()
            x = i - len(token)
            oldItr = i
            oldToken = token
            while i > x:
                type = IdentifyToken(token)
                if(type != None):
                    UpdateTokenLst(token, i-len(token), lineNumber, type)
                    break
                token = token[:-1]
                i -= 1

            if(type == None):
                i = oldItr
                token = oldToken
                UpdateTokenLst(token, i-len(token), lineNumber, "Error")

            token = "" 
        token += line[i]
        i += 1

def ReadSourceFile(path):
    lines = []
    with open(path) as f:
        lines = f.readlines()
    return lines

def Tokenize(filename):
    tokenList.clear()
    lines = ReadSourceFile(filename)
    i = 1
    if lines:
        for line in lines:
            if not line.isspace() and len(line) > 0:
                GetTokens(line.strip(), i)
            i += 1
        return DisplayTokens()
    else:
        print('Source File is empty!') 
