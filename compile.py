# import the tokenizer module
# access interface functions using tk
import tokenizer as tk   
from parse import Parse

class ArtLangCompiler:
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        self.tokenDf = None
        self.ErrorCount = 0
    
    def Tokenize(self):
        self.tokenDf = tk.Tokenize(self.sourceFile)
        return tk.GetErrorCount()

    def Parse(self):
        prMod = Parse(self.sourceFile, self.tokenDf)
        prMod.Parser()
        return prMod.GetErrorCount()
    
    def Main(self):
        try:
            tkErr = self.Tokenize()
            prErr = self.Parse()
            self.ErrorCount  = tkErr + prErr
            return self.ErrorCount 
        except:
            return 1

    
