from resources.compile import ArtLangCompiler
from resources.interpreter import Interpreter
class Art:
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.runnable = ""
    
    def Execute(self):
        comp = ArtLangCompiler(self.sourceFile)
        errCount = comp.Main()
        self.token = comp.tokenDf
        try:
            if errCount == 0:
                intptr = Interpreter(comp.tokenDf)
                print('[INFO] Interpreting Source code...')
                intptr.Interpret()
                intptr.Build()
                self.runnable = intptr.code
                self.token = intptr.tokens
            else:
                print('[ERROR] Please fix error(s) on the codes first.')
        except:
                print('[ERROR] Interpreter encountered an error.')
