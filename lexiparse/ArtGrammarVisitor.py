# Generated from ArtGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArtGrammarParser import ArtGrammarParser
else:
    from ArtGrammarParser import ArtGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ArtGrammarParser.

class ArtGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArtGrammarParser#expr.
    def visitExpr(self, ctx:ArtGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#func.
    def visitFunc(self, ctx:ArtGrammarParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#func_params.
    def visitFunc_params(self, ctx:ArtGrammarParser.Func_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#code.
    def visitCode(self, ctx:ArtGrammarParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#init.
    def visitInit(self, ctx:ArtGrammarParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#math_expr.
    def visitMath_expr(self, ctx:ArtGrammarParser.Math_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#computation.
    def visitComputation(self, ctx:ArtGrammarParser.ComputationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#size_shape.
    def visitSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#params.
    def visitParams(self, ctx:ArtGrammarParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#two_params.
    def visitTwo_params(self, ctx:ArtGrammarParser.Two_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#value_type.
    def visitValue_type(self, ctx:ArtGrammarParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#data_type.
    def visitData_type(self, ctx:ArtGrammarParser.Data_typeContext):
        return self.visitChildren(ctx)



del ArtGrammarParser