from resources.compile import ArtLangCompiler
from resources.interpreter import Interpreter
class Art:
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.code = ""
    
    def Execute(self):
        comp = ArtLangCompiler(self.sourceFile)
        errCount = comp.Main()
        try:
            if errCount == 0:
                intptr = Interpreter(comp.tokenDf)
                print('[INFO] Interpreting Source code...')
                intptr.Interpret()
                intptr.Build()
                self.code = intptr.code
            else:
                print('[ERROR] Please fix error(s) on the codes first.')
        except:
                print('[ERROR] Interpreter encountered an error.')
