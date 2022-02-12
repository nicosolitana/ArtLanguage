class SemanticAnalyzer:
    def __init__(self, tokendf):
        self.tokens = tokendf.to_dict(orient='records')
        self.errorLst = []
        self.parenStack = []
        self.varDecStack = []
        self.funcDecStack = []
        self.constStack = []
        self.globalStack = []
        self.funcParamLst = []
        self.dataTypes = ['RECTANGLE', 'CIRCLE', 'SQUARE', 'DOT', 'STRAIGHT','ARC','PIXEL', 'BOOL']
        self.funcTypes = ['OUTLINE', 'FILL', 'DRAW', 'SIZE']
        self.varDec = {}
        self.funcDec = {}
        self.semanticsTable = self.ReadSemanticsTable()
    
    def ReadSemanticsTable(self):
        semanticsTable = [] # contains symbol table
        semanticsTableFile = open("resources\\tables\semantics_table.txt") # reads the symbols file
		
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
        
    def CheckVarTypeParam(self, i, varType):
        if (self.tokens[i]['type'] == 'IDENTIFIER'):
            info = self.CheckVarExistence(i, varType)
            if len(info) > 0 and info[0]['DataType'] != "PIXEL":
                str = 'line {}:{} Type of passed parameter is invalid. Should be Pixel type.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
                self.errorLst.append(str)
            

    def CheckVarParam(self, i):
        self.CheckVarTypeParam(i, 'VARIABLE')

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
                    self.CheckVarParam(i)
                i += 1
            
            if(j != int(res[0]['paramcount'])):
                str = 'line {}:{} Parameter count for function {} of identifier {} is not correct'.format(lNum, cNum, res[0]['function'], varInfo[0]['Identifier'])
                self.errorLst.append(str)
            
        elif(self.tokens[i]['type'] == 'FILL') or (self.tokens[i]['type'] == 'OUTLINE'):
            j = 0
            oi = 0
            type = self.tokens[i]['type']
            while self.tokens[i]['type'] != 'PAREN_END':
                if (self.tokens[i]['type'] == 'PAREN_START'):
                    if(type == 'OUTLINE'):
                        if (self.tokens[i+1]['type'] == 'IDENTIFIER') or (self.tokens[i+1]['type'] == 'INTEGER'):
                            oi += 1
                            i += 2
                            self.CheckVarParam(i)
                        else:
                            str = 'line {}:{} Incorrect first parameter on function '"{}"'. Should be RGB'.format(lNum, cNum, type)
                            self.errorLst.append(str)
                    
                    if(self.tokens[i+1]['type'] != 'RGB'):
                        if(type == 'FILL'):
                            str = 'line {}:{} Incorrect parameter on function '"{}"'. Should be RGB'.format(lNum, cNum, type)
                            self.errorLst.append(str)
                    else:
                        IsRGBOK = True
                        while self.tokens[i]['type'] != 'PAREN_END':
                            if (self.tokens[i]['type'] == 'IDENTIFIER') or (self.tokens[i]['type'] == 'INTEGER'):
                                j += 1
                                if (self.tokens[i]['type'] == 'INTEGER') and(int(self.tokens[i]['token']) > 255):
                                    str = 'line {}:{} Color RGB parameter should not exceed 255'.format(lNum, cNum)
                                    self.errorLst.append(str)
                                    IsRGBOK = False
                                self.CheckVarParam(i)
                                
                            i += 1
                        if(j != 3):     
                            str = 'line {}:{} Incorrect RGB Parameter count'.format(lNum, cNum)
                            self.errorLst.append(str)
                        j = 1
                if (self.tokens[i]['type'] == 'IDENTIFIER') or (self.tokens[i]['type'] == 'INTEGER'):
                    j += 1
                    self.CheckVarParam(i)
                i += 1

            j += oi
            if (type == "FILL"):
                if(j != 2):
                    str = 'line {}:{} Parameter count for function '"{}"' is not correct'.format(lNum, cNum, type)
                    self.errorLst.append(str)
            if (type == "OUTLINE"):
                if(j != 3):
                    str = 'line {}:{} Parameter count for function '"{}"' is not correct'.format(lNum, cNum, type)
                    self.errorLst.append(str)
            pass
        return i

    def Functions(self, i):
        i += 1
        self.funcDec['Identifier'] = self.tokens[i]['token']
        count = 0
        while self.tokens[i]['type'] != 'PAREN_END':
            if(self.tokens[i]['type'] == 'IDENTIFIER'):
                self.funcParamLst.append(self.tokens[i]['token'])
                count += 1
            i += 1
        self.funcDec['paramcount'] = count
        self.funcDecStack.append(self.funcDec)
        self.funcDec = {}		
        return i

    def IsFuncParam(self, param):
        if param in self.funcParamLst:
            return True
        else:
            return False

    def Identifiers(self, i):
        varInfo = self.CheckVarExistence(i, 'VARIABLE')
        if(self.tokens[i+1]['type'] == 'DOT_NOTATION'):
            if(len(varInfo) > 0):
                i += 2
                i = self.ValidateFuncCall(i, varInfo)
            else:
                str = 'line {}:{} Identifier ''{}'' is not declared'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                self.errorLst.append(str)
        
        if (self.tokens[i+1]['type'] == 'ASSIGN_OP') and ((self.tokens[i+2]['type'] == 'FALSE') or (self.tokens[i+2]['type'] == 'TRUE')):
            if(len(varInfo) > 0):
                if(varInfo[0]['DataType'] != "BOOL"):
                    str = 'line {}:{} Cannot assign bool to a Pixel type.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
                    self.errorLst.append(str)
        
        if (self.tokens[i+1]['type'] == 'ASSIGN_OP') and (self.tokens[i+2]['type'] == 'IDENTIFIER'):
            v2Info = self.CheckVarExistence(i+2, 'VARIABLE')
            if(len(varInfo) > 0):
                v2Info = self.CheckVarExistence(i+2, 'VARIABLE')
            if (len(varInfo) > 0):
                vType = varInfo[0]['DataType']
            else:
                vType = "PIXEL"
            if(len(v2Info) > 0):
                v2Type = v2Info[0]['DataType']
            else:
                v2Type = "PIXEL"
            
            if(vType != v2Type):
                str = 'line {}:{} Variable assignment with different data types is prohibited.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
                self.errorLst.append(str)

        if(self.tokens[i+1]['type'] == 'ASSIGN_OP') or (self.tokens[i+1]['type'] == 'INCDEC_OP') or (self.tokens[i+1]['type'] == 'MATH_OP'):
            constInfo = self.CheckVarExistence(i, 'CONSTANT')
            globInfo = self.CheckVarExistence(i, 'GLOBAL')
            if((len(varInfo) == 0) and (len(constInfo) == 0) and (len(globInfo) == 0) and (self.IsFuncParam(self.tokens[i]['token']) == False)):
                str = 'line {}:{} Identifier ''{}'' is not declared'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                self.errorLst.append(str)
            if(len(constInfo)):
                str = 'line {}:{} Modifying constant value is prohibited.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
                self.errorLst.append(str)
            
            if(self.tokens[i+1]['type'] == 'MATH_OP'):
                v2Info = self.CheckVarExistence(i+2, 'VARIABLE')
                if (len(varInfo) > 0):
                    vType = varInfo[0]['DataType']
                else:
                    vType = "PIXEL"
                if(len(v2Info) > 0):
                    v2Type = v2Info[0]['DataType']
                else:
                    v2Type = "PIXEL"
                
                if(vType != v2Type):
                    str = 'line {}:{} Invalid variable type for arithmetic operation.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
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
                        self.CheckVarParam(i)
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
        i += 2
        if(self.tokens[i]['type'] == 'IDENTIFIER'):
            constInfo = self.CheckVarExistence(i, 'CONSTANT')
            if(len(constInfo) > 0):
                str = 'line {}:{} Constant ''{}'' is already defined.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'], self.tokens[i]['token'])
                self.errorLst.append(str)   
            constDec['Identifier'] = self.tokens[i]['token']
        i += 2
        constDec['value'] = self.tokens[i]['token']
        self.constStack.append(constDec)
        if(self.tokens[i]['token'].upper() == "TRUE") or (self.tokens[i]['token'].upper() == "FALSE"):
            str = 'line {}:{} Constant value should be pixel only.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
            self.errorLst.append(str)   
        i += 1
        return i
        
    def Globals(self, i):
        globalDec = {}
        IsAssignOp = False
        if(self.tokens[i+1]['type'] != 'PIXEL'):
            str = 'line {}:{} Global variable is restricted to Pixel only'.format(self.tokens[i+1]['lineNumber'], self.tokens[i+1]['start'])
            self.errorLst.append(str)  

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
    
    def Canvas(self, i):
        count = 0
        while self.tokens[i]['type'] != 'PAREN_END':
            if((self.tokens[i]['type'] == 'IDENTIFIER') or (self.tokens[i]['type'] == 'INTEGER')):
                count += 1
            i += 1
        if(count != 2):
            str = 'line {}:{} Function parameter count of CANVAS is incorrect.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
            self.errorLst.append(str)
        return i

    def CheckBools(self, i):
        if(self.tokens[i+1]['type'] == 'MATH_OP') or (self.tokens[i-1]['type'] == 'MATH_OP'):
            str = 'line {}:{} Bools cannot be used in arithmetic operation..'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
            self.errorLst.append(str)

    def CheckInt(self, i):
        if(self.tokens[i-2]['type'] == 'IDENTIFIER'):
            varInfo = self.CheckVarExistence(i-2, 'VARIABLE')
            if(len(varInfo) > 0):
                if(varInfo[0]['DataType'] != "PIXEL"):
                    str = 'line {}:{} Cannot assign pixel values on booleans.'.format(self.tokens[i]['lineNumber'], self.tokens[i]['start'])
                    self.errorLst.append(str)

    def SemanticAnalysis(self):
        isVarDec = False
        i = 0
        while i < len(self.tokens):
            if((self.tokens[i]['type'] == 'TRUE') or (self.tokens[i]['type'] == 'FALSE')):
                self.CheckBools(i)
            
            if(self.tokens[i]['type'] == 'INTEGER') and (self.tokens[i-1]['type'] == 'ASSIGN_OP'):
                self.CheckInt(i)

            if(self.tokens[i]['type'] == 'CANVAS'):
                i = self.Canvas(i)

            if(self.tokens[i]['type'] == 'CONSTANT'):
                i = self.Constants(i)
            
            if(self.tokens[i]['type'] == 'GLOBAL'):
                i = self.Globals(i)

            if(self.tokens[i]['type'] == 'DEF'):
                self.funcParamLst = []
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