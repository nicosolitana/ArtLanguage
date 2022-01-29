class SemanticAnalyzer:
    def __init__(self, tokendf):
        self.tokens = tokendf.to_dict(orient='records')
        self.errorLst = []
        self.parenStack = []
        self.varDecStack = []
        self.funcDecStack = []
        self.dataTypes = ['RECTANGLE', 'CIRCLE', 'SQUARE', 'DOT', 'STRAIGHT','ARC','PIXEL']
        self.funcTypes = ['OUTLINE', 'FILL', 'DRAW', 'SIZE']
        self.varDec = {}
        self.funcDec = {}
        self.semanticsTable = self.ReadSemanticsTable()
    
    def ReadSemanticsTable(self):
        semanticsTable = [] # contains symbol table

		# reads the symbols file
        semanticsTableFile = open("semantics_table.txt")
		
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
        res = len(list(filter(lambda item: item['Identifier'] == self.tokens[i]['token'], self.varDecStack)))
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
				
    def SemanticAnalysis(self):
        isVarDec = False
        i = 0
        while i < len(self.tokens):
            if(self.tokens[i]['type'] == 'DEF'):
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
                        varInfo = list(filter(lambda item: item['Identifier'] == self.tokens[i]['token'], self.varDecStack))
                        if(self.tokens[i+1]['type'] == 'DOT_NOTATION'):
                            if(len(varInfo) > 0):
                                i += 2
                                i = self.ValidateFuncCall(i, varInfo)
                            else:
                                str = 'line {}:{} Identifier ''{}'' is not declared'.format(self.tokens[i]['lineNumber'], self.tokens[i]['lineNumber'], self.tokens[i]['token'])
                                self.errorLst.append(str)
                        
                        if(self.tokens[i+1]['type'] == 'ASSIGN_OP'):
                            if(len(varInfo) == 0):
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
            i += 1
        
        res = list(filter(lambda item: item['type'] == 'CANVAS', self.tokens))
        if(res == []):
            str = 'line -:- There is no canvas defined.'
            self.errorLst.append(str)
        
        res = list(filter(lambda item: item['token'] == 'main', self.tokens))
        if(res == []):
            str = 'line -:- There is no main function defined.'
            self.errorLst.append(str)
        

