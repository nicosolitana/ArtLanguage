class SemanticAnalyzer:
    def __init__(self, tokendf):
        self.tokens = tokendf.to_dict(orient='records')
        self.errorLst = []
        self.parenStack = []
        self.varDecStack = []
        self.funcDecStack = []
        self.constStack = []
        self.globalStack = []
        self.dataTypes = ['RECTANGLE', 'CIRCLE', 'SQUARE', 'DOT', 'STRAIGHT','ARC','PIXEL']
        self.funcTypes = ['OUTLINE', 'FILL', 'DRAW', 'SIZE']
        self.varDec = {}
        self.funcDec = {}
        self.semanticsTable = self.ReadSemanticsTable()
    
    def ReadSemanticsTable(self):
        semanticsTable = [] # contains symbol table
        semanticsTableFile = open("tables\semantics_table.txt") # reads the symbols file
		
		# creates keyvalue pair to store regex pattern and
		# its equivalent token name
        for line in semanticsTableFile:
            key, value = line.split()  # splits line into kvp
            func, params = value.split(',')
            semantics = {}
            semantics['shape'] = key
            semantics['function'] = func
            semantics['paramcount'] = params
            semanticsTable.append(semantics)  # stores kvp on the symbolTable list
        return semanticsTable
        
    def CompleteVarDec(self, i):
        res = len(self.CheckVarExistence(i, 'VARIABLE'))
        gRes = len(self.CheckVarExistence(i, 'GLOBAL'))
        cRes = len(self.CheckVarExistence(i, 'CONSTANT'))
        
        if(cRes != 0):
            str = 'line {}:{} Variable ''{}'' is already declared as constant.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
            self.errorLst.append(str)

        if(gRes != 0):
            str = 'line {}:{} Variable ''{}'' is already declared as global variable.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
            self.errorLst.append(str)

        if(res != 0):
            str = 'line {}:{} Variable ''{}'' is already declared.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
            self.errorLst.append(str)
        else:
            self.varDec['Identifier'] = self.tokens[i]['token']
            self.varDecStack.append(self.varDec)
        self.varDec = {}
        
    def ValidateFuncCall(self, i, varInfo):
        shapeType = ''
        lNum = self.tokens[i]['lineNumber'] 
        cNum = self.tokens[i]['start'] 
        shapeType = varInfo[0]['DataType']
        if(self.tokens[i]['type'] == 'SIZE') or (self.tokens[i]['type'] == 'DRAW'):
            res = list(filter(lambda item: item['shape'] == shapeType and item['function'] == self.tokens[i]['type'], self.semanticsTable))
            j = 0
            while self.tokens[i]['type'] != 'PAREN_END':
                if (self.tokens[i]['type'] == 'IDENTIFIER') or (self.tokens[i]['type'] == 'INTEGER'):
                    j += 1
                i += 1
            if(j != int(res[0]['paramcount'])):
                str = 'line {}:{} Parameter count for function {} of identifier {} is not correct'.format(lNum, cNum, res[0]['function'], varInfo[0]['Identifier'])
                self.errorLst.append(str)
        return i

    def Functions(self, i):
        i += 1
        self.funcDec['Identifier'] = self.tokens[i]['token']
        count = 0
        while self.tokens[i]['type'] != 'PAREN_END':
            if(self.tokens[i]['type'] == 'IDENTIFIER'):
                count += 1
            i += 1
        self.funcDec['paramcount'] = count
        self.funcDecStack.append(self.funcDec)
        self.funcDec = {}		
        return i

    def Identifiers(self, i):
        varInfo = self.CheckVarExistence(i, 'VARIABLE')
        if(self.tokens[i+1]['type'] == 'DOT_NOTATION'):
            if(len(varInfo) > 0):
                i += 2
                i = self.ValidateFuncCall(i, varInfo)
            else:
                str = 'line {}:{} Identifier ''{}'' is not declared'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
                self.errorLst.append(str)
        
        if(self.tokens[i+1]['type'] == 'ASSIGN_OP') or (self.tokens[i+1]['type'] == 'INCDEC_OP'):
            constInfo = self.CheckVarExistence(i, 'CONSTANT')
            globInfo = self.CheckVarExistence(i, 'GLOBAL')
            if((len(varInfo) == 0) and (len(constInfo) == 0) and (len(globInfo) == 0)):
                str = 'line {}:{} Identifier ''{}'' is not declared'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
                self.errorLst.append(str)
        
        if(self.tokens[i+1]['type'] == 'PAREN_START'):
            funcInfo = list(filter(lambda item: item['Identifier'] == self.tokens[i]['token'], self.funcDecStack))
            count = 0
            lNum = self.tokens[i]['lineNumber']
            cNum = self.tokens[i]['start']
            if(len(funcInfo) == 0):
                if (self.tokens[i]['type'] not in self.funcTypes):
                    str = 'line {}:{} Function ''{}'' is not declared'.format(lNum, cNum, self.tokens[i]['token'])
                    self.errorLst.append(str)
            else:
                while self.tokens[i]['type'] != 'PAREN_END':
                    if((self.tokens[i]['type'] == 'IDENTIFIER') or (self.tokens[i]['type'] == 'INTEGER')):
                        count += 1
                    i += 1
                if(int(funcInfo[0]['paramcount']) != count):
                    str = 'line {}:{} Function parameter ''{}'' is not correct'.format(lNum, cNum, funcInfo[0]['Identifier'])
                    self.errorLst.append(str)
        return i

    def CheckCanvasMain(self, itr, value):
        res = list(filter(lambda item: item[itr] == value, self.tokens))
        if(res == []):
            str = 'line -:- There is no {} defined.'.format(value)
            self.errorLst.append(str)

    def CheckVarExistence(self, i, type):
        stackVal = []
        if(type == 'CONSTANT'):
            stackVal = self.constStack
        if(type == 'GLOBAL'):
            stackVal = self.globalStack
        if(type == 'VARIABLE'):
            stackVal = self.varDecStack
        return list(filter(lambda item: item['Identifier'] == self.tokens[i]['token'], stackVal))
                
    def Constants(self, i):
        constDec = {}
        IsAssignOp = False
        while self.tokens[i]['type'] != 'INTEGER':
            if(self.tokens[i]['type'] == 'IDENTIFIER'):
                constInfo = self.CheckVarExistence(i, 'CONSTANT')
                if(len(constInfo) > 0):
                    str = 'line {}:{} Constant ''{}'' is already defined.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                    self.errorLst.append(str)   
                constDec['Identifier'] = self.tokens[i]['token']

            if(self.tokens[i]['type'] == 'ASSIGN_OP'):
                IsAssignOp = True 
            i += 1
        if(self.tokens[i]['type'] == 'INTEGER') and IsAssignOp:
            constDec['value'] = self.tokens[i]['token']
            self.constStack.append(constDec)
        return i
        
    def Globals(self, i):
        globalDec = {}
        IsAssignOp = False
        while self.tokens[i]['type'] != 'INTEGER':
            if(self.tokens[i]['type'] == 'IDENTIFIER'):
                constInfo = self.CheckVarExistence(i, 'CONSTANT')
                globalInfo = self.CheckVarExistence(i, 'GLOBAL')
                if(len(constInfo) > 0):
                    str = 'line {}:{} Global variable ''{}'' is already defined as constant.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                    self.errorLst.append(str)   
                else:
                    if(len(globalInfo) > 0):
                        str = 'line {}:{} Global variable ''{}'' is already defined.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                        self.errorLst.append(str)   
                
                globalDec['Identifier'] = self.tokens[i]['token']
            i += 1

            if(self.tokens[i]['type'] == 'ASSIGN_OP'):
                IsAssignOp = True 
        if(self.tokens[i]['type'] == 'INTEGER') and IsAssignOp:
            globalDec['value'] = self.tokens[i]['token']
            self.globalStack.append(globalDec)
        return i
        
    def SemanticAnalysis(self):
        isVarDec = False
        i = 0
        while i < len(self.tokens):
            if(self.tokens[i]['type'] == 'CONSTANT'):
                i = self.Constants(i)
            
            if(self.tokens[i]['type'] == 'GLOBAL'):
                i = self.Globals(i)

            if(self.tokens[i]['type'] == 'DEF'):
                i = self.Functions(i)
            if(self.tokens[i]['type'] == 'CURLY_START'):
                self.parenStack.append('CURLY_START')
            if(self.tokens[i]['type'] == 'CURLY_END'):
                if(len(self.parenStack) == 1):
                    self.varDecStack = []
                if(len(self.parenStack) > 0):
                    self.parenStack.pop()
            if(self.tokens[i]['type'] in self.dataTypes):
                self.varDec['DataType'] = self.tokens[i]['type']
                isVarDec = True
            if(self.tokens[i]['type'] == 'IDENTIFIER'):
                if isVarDec:
                    self.CompleteVarDec(i)
                    isVarDec = False
                else:
                    if(i < len(self.tokens)):
                        i = self.Identifiers(i)
            i += 1
        
        self.CheckCanvasMain('type', 'CANVAS')
        self.CheckCanvasMain('token', 'main')