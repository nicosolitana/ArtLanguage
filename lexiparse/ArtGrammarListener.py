# Generated from ArtGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArtGrammarParser import ArtGrammarParser
else:
    from ArtGrammarParser import ArtGrammarParser

# This class defines a complete listener for a parse tree produced by ArtGrammarParser.
class ArtGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ArtGrammarParser#expr.
    def enterExpr(self, ctx:ArtGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#expr.
    def exitExpr(self, ctx:ArtGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#func.
    def enterFunc(self, ctx:ArtGrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#func.
    def exitFunc(self, ctx:ArtGrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#func_params.
    def enterFunc_params(self, ctx:ArtGrammarParser.Func_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#func_params.
    def exitFunc_params(self, ctx:ArtGrammarParser.Func_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#code.
    def enterCode(self, ctx:ArtGrammarParser.CodeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#code.
    def exitCode(self, ctx:ArtGrammarParser.CodeContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#init.
    def enterInit(self, ctx:ArtGrammarParser.InitContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#init.
    def exitInit(self, ctx:ArtGrammarParser.InitContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#math_expr.
    def enterMath_expr(self, ctx:ArtGrammarParser.Math_exprContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#math_expr.
    def exitMath_expr(self, ctx:ArtGrammarParser.Math_exprContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#computation.
    def enterComputation(self, ctx:ArtGrammarParser.ComputationContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#computation.
    def exitComputation(self, ctx:ArtGrammarParser.ComputationContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#size_shape.
    def enterSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#size_shape.
    def exitSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#params.
    def enterParams(self, ctx:ArtGrammarParser.ParamsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#params.
    def exitParams(self, ctx:ArtGrammarParser.ParamsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#two_params.
    def enterTwo_params(self, ctx:ArtGrammarParser.Two_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#two_params.
    def exitTwo_params(self, ctx:ArtGrammarParser.Two_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#value_type.
    def enterValue_type(self, ctx:ArtGrammarParser.Value_typeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#value_type.
    def exitValue_type(self, ctx:ArtGrammarParser.Value_typeContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#data_type.
    def enterData_type(self, ctx:ArtGrammarParser.Data_typeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#data_type.
    def exitData_type(self, ctx:ArtGrammarParser.Data_typeContext):
        pass



del ArtGrammarParser