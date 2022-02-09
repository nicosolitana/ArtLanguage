import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNodeImpl
from sqlalchemy import null
from lexiparse.ArtGrammarLexer import ArtGrammarLexer
from lexiparse.ArtGrammarParser import ArtGrammarParser
from lexiparse.ArtGrammarVisitor import ArtGrammarVisitor
from IPython.utils.capture import capture_output
from semantics import SemanticAnalyzer

class Parse:
    
    def __init__(self, filepath, tokendf):
        self.data = FileStream(filepath)
        self.tokendf = tokendf
        self.Error = []
        self.ParserErr = 0

    def Traverse(self, tree, rule_names, indent = 0):
        if tree.getText() == "<EOF>":
            return
        elif isinstance(tree, TerminalNodeImpl):
            print("{0}{1}".format("  " * indent, tree.getText()))
        else:
            print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
            for child in tree.children:
                self.Traverse(child, rule_names, indent + 1)
    
    def DisplayTree(self, tree, parser):
        print(Trees.toStringTree(tree, None, parser))

    def SemanticAnalysis(self):
        smA = SemanticAnalyzer(self.tokendf)
        smA.SemanticAnalysis()
        for errMsg in smA.errorLst:
            print(errMsg)
        self.Error = smA.errorLst

    def Parser(self):
        with capture_output() as start_parse:
            lexer = ArtGrammarLexer(self.data )
            stream = CommonTokenStream(lexer)
            parser = ArtGrammarParser(stream)
            tree = parser.expr()
        start_parse()
        self.SemanticAnalysis()
        self.ParserErr = parser.getNumberOfSyntaxErrors()
        # UNCOMMENT CODE BELOW TO DISPLAY PARSE TREE
        #print('\n\nParse Tree is displayed below:')
        #self.Traverse(tree, parser.ruleNames)
    
    def GetErrorCount(self):
        count = len(self.Error) + self.ParserErr 
        return count