import re
import pandas as pd

# Character that separates token from each other
REGEX_SEPARATOR = ",|;|\s+"

tokenList = []   # contains tokens of the entire source code
symbolTable = {} # contains symbol table

# reads the symbols file
symbolTableFile = open("tables\symbol_table.txt")
# creates keyvalue pair to store regex pattern and
# its equivalent token name
for line in symbolTableFile:
    key, value = line.split()  # splits line into kvp
    symbolTable[key] = value   # stores kvp on the symbolTable list

# Token class which holds information 
# related to token's line number, type and column number
class Tokens: 
    def __init__(self, token, start, type, lineNumber): 
        self.lineNumber = lineNumber
        self.start = start
        self.token = token 
        self.type = type

# Function Name: IsValidToken
# Purpose: displays all retrieved tokens in dataframe format
def DisplayTokens():
    df = pd.DataFrame([t.__dict__ for t in tokenList])
    return df

# Function Name: IsValidToken
# Purpose: Checks if token is valid
# Parameters:
#    token - retrieved lexeme
#    REGEX_PATTERN - regex pattern in the symbol table
# Return Value:
#   TRUE : Valid token
#   FALSE : Invalid token
def IsValidToken(token, REGEX_PATTERN):
    matched = re.match(REGEX_PATTERN, token)  # Checks if a token match the pattern
    return bool(matched)    # results match result

# Function Name: IdentifyToken
# Purpose: Identify retrieved lexeme's type
# Parameters:
#    token - lexeme
# Return Value:
#    type - lexeme's token type
def IdentifyToken(token):
    # loop on each symbol in symbol table
    for type in symbolTable:
        # check if the lexeme matches any token type's pattern
        if(IsValidToken(token, symbolTable[type]) == True):
            return type  # return type

# Function Name: UpdateTokenLst
# Purpose: Updates Token List of the source code
# Parameters:
#    token - lexeme
#    start - lexeme's column number
#    lineNumber - lexeme's code line number
#    type - lexeme's token type
def UpdateTokenLst(token, start, lineNumber, type):
    obj = Tokens(token, start, type, lineNumber) # create token instance
    tokenList.append(obj)  

# Function Name: GetTokens
# Purpose: Get tokens in a code line
# Parameters:
#    line - code line in a source code
#    lineNumber - code line's row number
def GetTokens(line, lineNumber):
    token = ""      # initialize token
    i = 0           # initialize iterator i which will be used to traverse codeline
    line += " "     # add an extra space at the end of the code line
    while i < len(line):  # loop on each character of the code line
        # check if the current character matches a separator
        if(IsValidToken(line[i], REGEX_SEPARATOR) == True):
            token = token.strip()   # trim the token to remove extra spaces
            x = i - len(token)      # store token's starting point
            oldItr = i              # store current iterator's value
            oldToken = token        # store current token's value
            # loop until you come back to the starting point x of the current token
            while i > x:       
                # Check if token matches a type
                type = IdentifyToken(token)
                if(type != None):
                    # Save token to token list
                    UpdateTokenLst(token, i-len(token), lineNumber, type)
                    break    # break free from the loop
                # remove last character in the token
                token = token[:-1]
                # decrement i
                i -= 1

            # if the type remains to be None,
            # then, the token did not match any token type 
            # in the above while loop operation
            if(type == None):
                i = oldItr          # set i back to future mode
                token = oldToken    # set token back to previous value
                UpdateTokenLst(token, i-len(token), lineNumber, "Error")   # update token list

            # reset token to empty value
            token = "" 
        
        token += line[i]    # add one character to token
        i += 1  # increment i to get next character

# Function Name: ReadSourceFile
# Purpose: Get source code from the input source file
# Parameters:
#    path - path of the target source code
# Return Value:
#    lines - list of code lines in the source file
def ReadSourceFile(path):
    lines = []       # code line list
    with open(path) as f:       # open source file
        lines = f.readlines()   # read all lines in the source file
    return lines     # return the list of code lines

# Function Name: Tokenize
# Purpose: Interface function, tokenizes the source file
# Parameters:
#    filepath - path of the target source code, filename included
# Return Value:
#    - Return dataframe of tokens or error when source file is empty
def Tokenize(filepath):
    tokenList.clear()
    lines = ReadSourceFile(filepath)
    i = 1
    if lines:
        for line in lines:
            if not line.isspace() and len(line) > 0:
                GetTokens(line.strip(), i)
            i += 1

        for t in tokenList:
            if(t.type == "Error"):
                print("line {}:{} Invalid token '{}'".format(t.lineNumber, t.start, t.token))
                
        return DisplayTokens()
    else:
        print('[ERROR] Source File is empty!') 

def GetErrorCount():
    errCount = 0
    for t in tokenList:
        if(t.type == "Error"):
            print("line {}:{} Invalid token '{}'".format(t.lineNumber, t.start, t.token))
            errCount += 1
    return errCount   