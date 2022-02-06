# Trial Execution of Python Code after ART code conversion to python
# Art Code is
# def main(){
#    print('This is a demo')
# }
# Converted Python Code is:
# def main():
#   print('This is a demo')
# main()
#str = 'def main(): ' + '\n\tprint(\'This is a demo\')' + '\n\nmain()'
#exec(str)

import os
import shutil

from inspect import iscode

class Interpreter:
    def __init__(self, tokendf):
        self.tokens = tokendf.to_dict(orient='records')
        self.tabs = ""
        self.code = ""
    
    def GetLogicalSym(self, symbol):
        if(symbol == "||"):
            return "or"
        else:
            return "and"

    def Conditions(self, i):
        logicalSymbols = ['||', '&&']
        self.code += self.tabs
        while self.tokens[i]['type'] != 'CURLY_START':
            if(self.tokens[i]['token'] in logicalSymbols):
                self.code += (" " + self.GetLogicalSym(self.tokens[i]['token']) + " " )
            else:
                self.code += (self.tokens[i]['token'])
            i += 1
        self.tabs += "\t"
        self.code += (":\n")

        # TO BE REMOVED ONCE CODELINES ARE INTERPRETED
        self.code += self.tabs + "pass\n"
        return i

    # For correction, return values are placeholders only
    def GetCondSym(self, symbol):
        if(symbol == '<') or (symbol == '>'):
            return "0+"
        elif(symbol == '<='):
            return "1+"
        else:   # symbol == ">="
            return "1-"

    def Loops(self, i):
        self.code += self.tabs
        isParenStart = False
        isSepCount = 0
        initVariable = ''
        start = ''
        stop = ''
        step = ''
        while self.tokens[i]['type'] != 'CURLY_START':
            if(isSepCount == 0) and (isParenStart == True):
                initVariable = self.tokens[i]['token']
                i += 2    
                while self.tokens[i]['type'] != 'SEMICOL_SEP':
                    start += self.tokens[i]['token'] 
                    i += 1
                i += 1
                isSepCount += 1
            
            if(isSepCount == 1) and (isParenStart == True):
                IsCond = False
                while self.tokens[i]['type'] != 'SEMICOL_SEP':
                    if(IsCond):
                        stop += self.tokens[i]['token']
                    if(self.tokens[i]['type'] == 'COND_OP'):
                        stop += self.GetCondSym(self.tokens[i]['token'])
                        IsCond = True
                    i += 1
                i += 1
                isSepCount += 1

            if(isSepCount == 2) and (isParenStart == True):
                step = self.tokens[i]['token']
                if(self.tokens[i+1]['token'] == '--'):
                    step = ("-" + step)
                i += 1
                isSepCount += 1

            if(self.tokens[i]['type'] == 'FOR'):
                self.code += self.tokens[i]['token']

            if(self.tokens[i]['type'] == 'PAREN_START'):
                isParenStart = True
                self.code += " "
            i += 1
        
        self.tabs += "\t"
        self.code += initVariable + " in range(" + start + "," + stop + "," + step + "):\n"
        
        # TO BE REMOVED ONCE CODELINES ARE INTERPRETED
        self.code += self.tabs + "pass\n"
        return i

    def Function(self, i):
        if(self.tokens[i]['type'] == 'DEF'):
            while(self.tokens[i]['type'] != 'CURLY_START'):
                print(self.tokens[i]['token'])
                self.code += self.tokens[i]['token'] + " "   
                i = i + 1
        self.code += self.tabs + ":\n"
        self.tabs += "\t"
        return i

    def FunctionCall(self, i):
        self.code += self.tabs
        while(self.tokens[i]['type'] != 'PAREN_END'):
            if(self.tokens[i]['type'] != 'PAREN_START'):
                pass #ignore
            self.code += self.tokens[i]['token']
            i = i + 1
        self.code += ")\n"
        return i


    def Interpret(self):
        i = 0
        while i < len(self.tokens):
            lNum = self.tokens[i]['lineNumber']
            if(self.tokens[i]['type'] == 'FOR'):
                i = self.Loops(i)

            if((self.tokens[i]['type'] == 'IF') or (self.tokens[i]['type'] == 'ELIF') or (self.tokens[i]['type'] == 'ELSE')):
                i = self.Conditions(i)

            if(self.tokens[i]['type'] == 'CURLY_END'):
                self.tabs = self.tabs[:-1]

            if(self.tokens[i]['type'] == 'DEF'):
                i = self.Function(i)
            
            if(self.tokens[i]['type'] == 'IDENTIFIER' and self.tokens[i-1]['type'] != 'DEF'):
                i = i + 1 
                if(self.tokens[i]['type'] == 'PAREN_START'):
                    i = i - 1 
                    i = self.FunctionCall(i)
                else:
                    i = i - 1
            i += 1
        self.code += "\nmain()"
    
    def Build(self):
        filename = "build/build.py"
        if os.path.exists(filename):
            location = os.getcwd()
            dir = "build"
            path = os.path.join(location, dir)
            shutil.rmtree(path)
        os.mkdir(os.path.dirname(filename))
        with open(filename, "w") as f:
            f.write(self.code)