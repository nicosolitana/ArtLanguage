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

import pyglet 
from pyglet import shapes 
from pyglet.gl import glClearColor

import os
from re import T
import shutil
from inspect import iscode

class Interpreter:
    def __init__(self, tokendf):
        self.tokens = tokendf.to_dict(orient='records')
        self.tabs = ""
        self.code = ""
        self.funcStack = []
        self.variableList = {} # stores the variable name and its current type
    
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
        # self.code += self.tabs + "pass\n"
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
        self.code += self.tabs + "z += 1\n"
        return i

    # function for grammars: init_int, math_expr, "x++"
    def Assign(self, i):
        # IDENTIFIER
        self.code += self.tokens[i]['token']
        i += 1

        if (self.tokens[i]['type'] == "ASSIGN_OP"):
            # ASSIGN_OP
            self.code += self.tokens[i]['token']
            i += 1

            # INTEGER / value_type 1
            self.code += self.tokens[i]['token']

            i += 1
            if (self.tokens[i]['type'] == "MATH_OP"):
                self.code += self.tokens[i]['token'] # MATH_OP
                i += 1
                self.code += self.tokens[i]['token'] # value_type 2
            else:
                i -= 1
        elif (self.tokens[i]['type'] == "INCDEC_OP"):
            if (self.tokens[i]['token'] == "++"):
                self.code += "+=1"
            elif (self.tokens[i]['token'] == "--"):
                self.code += "-=1"

        return i

    # function for Function declaration : def sampleTest(a,b,c)
    def Function(self, i):
        self.funcStack.append(self.tokens[i+1]['token'])
        if(self.tokens[i]['type'] == 'DEF'):
            while(self.tokens[i]['type'] != 'CURLY_START'):
                self.code += self.tokens[i]['token'] 
                if(self.tokens[i]['type'] == 'DEF'):
                    self.code += " "
                i = i + 1
        self.code += self.tabs + ":\n"
        self.tabs += "\t"
        self.code += self.tabs + "global z\n"
        return i

    # function for Function call: sampleTest(a,b,c)
    def FunctionCall(self, i):
        self.code += self.tabs
        funcName = self.tokens[i]['token']
        while(self.tokens[i]['type'] != 'PAREN_END'):
            if(self.tokens[i]['type'] != 'PAREN_START'):
                pass #ignore
            self.code += self.tokens[i]['token']
            i = i + 1
        self.code += ")\n"

        # TESTING ONLY FOR RECURSION
        if (funcName == self.funcStack[-1]):
            self.code += self.tabs + "z += 1\n"
        return i

    def Fill(self, i):
        var = self.tokens[i]['token']
        red = self.tokens[i + 6]['token']
        green = self.tokens[i + 8]['token']
        blue = self.tokens[i + 10]['token']
        opacity = self.tokens[i + 13]['token']
        self.code += self.tabs
        self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',var,'"') + ".color = (" + red + "," + green + "," + blue + ")\n"
        self.code += self.tabs
        self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',var,'"') + ".opacity = " + opacity + "\n"
        return i + 14
                          
    def Outline(self, i): 
        shapeName = self.tokens[i]['token']
        thickness = self.tokens[i+4]['token']
        red = self.tokens[i+8]['token']
        blue = self.tokens[i+10]['token']
        green = self.tokens[i+12]['token']
        opacity = self.tokens[i+15]['token']
        i += 16
        if self.variableList[shapeName] == "Rectangle" or self.variableList[shapeName] == "Square":
            self.code += self.tabs
            self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".border_color = (" + red + "," + green + "," + blue + ")\n"
            self.code += self.tabs
            self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".border = " + thickness + "\n"
            self.code += self.tabs
            self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".opacity = " + opacity + "\n"
        elif self.variableList[shapeName] == "Circle":
            self.code += self.tabs + "x = globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".x\n" 
            self.code += self.tabs + "y = globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".y\n" 
            self.code += self.tabs + "rad = globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + ".radius\n" 
            self.code += self.tabs + "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName+"b",'"') 
            self.code += "= shapes.Circle(x, y, rad+{}, batch=batch)\n".format(thickness)
            self.code += self.tabs + "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName+"b",'"') + ".color = (" + red + "," + green + "," + blue + ")\n"
            self.code += self.tabs + "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName+"b",'"') + ".opacity = " + opacity + "\n" 
            self.code += self.tabs + "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') 
            self.code += "= shapes.Circle(x, y, rad, batch=batch)\n"
        return i

    # function for shape declaration
    def DeclareShape(self, i):
        shapeType = self.tokens[i]['token']
        i = i + 1
        shapeName = self.tokens[i]['token']

        if shapeName in self.variableList.keys(): # if the variable has been previously declared
            self.variableList.update({shapeName: shapeType})
        else:
            self.variableList[shapeName] = shapeType
            # NO NEED TO DECLARE VARIABLE IN PYTHON
            # self.code += self.tabs
            #self.code += "global " + shapeName + "\n"
        return i

    def Globals(self, i):
        self.code += self.tabs + self.tokens[i+2]['token']
        self.code += self.tabs + self.tokens[i+3]['token'] 
        self.code += self.tabs + self.tokens[i+4]['token'] + "\n"
        i += 4
        return i

    #Function for iniitializing code : e.g import library
    def InitializeCode(self):
        self.code = "import pyglet \nfrom pyglet import shapes \nfrom pyglet.gl import glClearColor\n\n"
        self.code += "batch = pyglet.graphics.Batch()\n"
        self.code += "window = pyglet.window.Window(0, 0)\n" # Note: Set "window" for canvas!
        self.code += "glClearColor(255, 255, 255, 1.0)\n" 
        self.code += "z = 0\n" 
        return self.code

    def Draw(self, i): # for line and arc
        shapeName = self.tokens[i]['token']
        i = i + 3
        if self.variableList[shapeName] == "Straight":
            self.code += self.tabs
            self.code += "globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + "= shapes.Line"
            while self.tokens[i]['type'] != "PAREN_END":
                self.code += self.tokens[i]['token']
                i = i + 1
            self.code += ", color=(101,45,144), width=2, batch=batch)\n"
        elif self.variableList[shapeName] == "Arc":
            self.code += self.tabs
            print("How to draw an arc?")

        return i

    #Function for printing the displaying pyglet after main()
    def PrintMain(self):
        self.tabs += "\t"
        
        self.code += "\nmain()\n"
        self.code += "@window.event\ndef on_draw():\n"
        self.code += (self.tabs + "global window, batch\n")
        self.code += (self.tabs + "window.clear()\n")
        self.code += (self.tabs + "batch.draw()\n")
        self.tabs = self.tabs[:-1]
        self.code += "pyglet.app.run()\n"
        return self.code 

    def Size(self, i):
        shapeName = self.tokens[i]['token']
        i = i + 3
        if self.variableList[shapeName] == "Dot":
            self.code += self.tabs
            self.code += ("globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + "= shapes.BorderedRectangle")
            while self.tokens[i]['type'] != "PAREN_END":
                self.code += self.tokens[i]['token']
                i = i + 1
            self.code += ",width=0.1, height=0.1, border=1, batch=batch)\n"
        elif self.variableList[shapeName] == "Rectangle" or self.variableList[shapeName] == "Square":
            self.code += self.tabs
            self.code += ("globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + "= shapes.BorderedRectangle")
            while self.tokens[i]['type'] != "PAREN_END":
                self.code += self.tokens[i]['token']
                i = i + 1
            if self.variableList[shapeName] == "Square":
                self.code += "," + self.tokens[i-1]['token']
            self.code += ", batch=batch)\n"
        elif self.variableList[shapeName] == "Circle":
            self.code += self.tabs
            self.code += ("globals()[f{0}{1}{{z}}{2}]".format('"',shapeName,'"') + "= shapes.Circle")
            while self.tokens[i]['type'] != "PAREN_END":
                self.code += self.tokens[i]['token']
                i = i + 1
            self.code += ", batch=batch)\n"
            pass
        return i
            
    def Canvas(self, i):
        width = self.tokens[i+2]['token']
        height = self.tokens[i+4]['token']
        self.code += (self.tabs + "global window\n")
        self.code += (self.tabs + ("window.width ={}\n".format(width)))
        self.code += (self.tabs + ("window.height ={}\n".format(height)))
        #self.code += (self.tabs + ("glClearColor(255, 255, 255, 1.0)\n"))
        i += 5
        return i

    def Interpret(self):
        self.InitializeCode() # importing/initializing pyglet
        
        i = 0
        while i < len(self.tokens):
            lNum = self.tokens[i]['lineNumber']
            if(self.tokens[i]['type'] == 'FOR'):
                i = self.Loops(i)

            if((self.tokens[i]['type'] == 'IF') or (self.tokens[i]['type'] == 'ELIF') or (self.tokens[i]['type'] == 'ELSE')):
                i = self.Conditions(i)

            if(self.tokens[i]['type'] == 'CURLY_END'):
                self.tabs = self.tabs[:-1]

            if (i < len(self.tokens) - 1):
                if(self.tokens[i]['type'] == "IDENTIFIER" and (self.tokens[i + 1]['type'] == "ASSIGN_OP" or self.tokens[i + 1]['type'] == "INCDEC_OP")):
                    self.code += self.tabs
                    i = self.Assign(i)
                    self.code += "\n"

            if(self.tokens[i]['type'] == 'DEF'):
                i = self.Function(i)
            
            if(self.tokens[i]['type'] == 'CANVAS'):
                i = self.Canvas(i)
            
            if(self.tokens[i]['type'] == 'GLOBAL'):
                i = self.Globals(i)

            if(self.tokens[i]['type'] == 'IDENTIFIER' and self.tokens[i-1]['type'] != 'DEF'):
                i = i + 1 
                if(self.tokens[i]['type'] == 'PAREN_START'):
                    i = i - 1 
                    i = self.FunctionCall(i)
                else:
                    i = i - 1

            if (i < len(self.tokens) - 2):
                if (self.tokens[i]['type'] == "IDENTIFIER" and self.tokens[i + 1]['type'] == "DOT_NOTATION" and self.tokens[i + 2]['type'] == "FILL"):
                    i = self.Fill(i)

            if (self.tokens[i]['type'] == "STRAIGHT" or self.tokens[i]['type'] == "SQUARE" or self.tokens[i]['type'] == "RECTANGLE" or self.tokens[i]['type'] == "CIRCLE" or self.tokens[i]['type'] == "DOT" or self.tokens[i]['type'] == "ARC" or self.tokens[i]['type'] == "PIXEL"):
                i = self.DeclareShape(i)
            
            if (i < len(self.tokens) - 2):
                if (self.tokens[i]['type'] == "IDENTIFIER" and self.tokens[i + 1]['type'] == "DOT_NOTATION" and self.tokens[i + 2]['type'] == "DRAW"):
                    i = self.Draw(i)

            if (i < len(self.tokens) - 2):
                if (self.tokens[i]['type'] == "IDENTIFIER" and self.tokens[i + 1]['type'] == "DOT_NOTATION" and self.tokens[i + 2]['type'] == "SIZE"):
                    i = self.Size(i)

            if (i < len(self.tokens) - 2):
                if (self.tokens[i]['type'] == "IDENTIFIER" and self.tokens[i + 1]['type'] == "DOT_NOTATION" and self.tokens[i + 2]['type'] == "OUTLINE"):
                    i = self.Outline(i)

            i += 1
        self.PrintMain() # prints main() and on window event
        
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
    
    def Run(self):
        exec(self.code)
        #exec(open("build/build.py").read())