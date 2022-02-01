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


    # Visit a parse tree produced by ArtGrammarParser#consts.
    def visitConsts(self, ctx:ArtGrammarParser.ConstsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#glob.
    def visitGlob(self, ctx:ArtGrammarParser.GlobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#func_params.
    def visitFunc_params(self, ctx:ArtGrammarParser.Func_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#code.
    def visitCode(self, ctx:ArtGrammarParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#loop.
    def visitLoop(self, ctx:ArtGrammarParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#loop_body.
    def visitLoop_body(self, ctx:ArtGrammarParser.Loop_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#loop_init.
    def visitLoop_init(self, ctx:ArtGrammarParser.Loop_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#loop_cond.
    def visitLoop_cond(self, ctx:ArtGrammarParser.Loop_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#loop_incdec.
    def visitLoop_incdec(self, ctx:ArtGrammarParser.Loop_incdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#init.
    def visitInit(self, ctx:ArtGrammarParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#init_int.
    def visitInit_int(self, ctx:ArtGrammarParser.Init_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#func_call.
    def visitFunc_call(self, ctx:ArtGrammarParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#call_params.
    def visitCall_params(self, ctx:ArtGrammarParser.Call_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#if_else.
    def visitIf_else(self, ctx:ArtGrammarParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#if_cond.
    def visitIf_cond(self, ctx:ArtGrammarParser.If_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#elif_cond.
    def visitElif_cond(self, ctx:ArtGrammarParser.Elif_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#else_cond.
    def visitElse_cond(self, ctx:ArtGrammarParser.Else_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#condition_base.
    def visitCondition_base(self, ctx:ArtGrammarParser.Condition_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#condition_body.
    def visitCondition_body(self, ctx:ArtGrammarParser.Condition_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#condition.
    def visitCondition(self, ctx:ArtGrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#ifel_body.
    def visitIfel_body(self, ctx:ArtGrammarParser.Ifel_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#math_expr.
    def visitMath_expr(self, ctx:ArtGrammarParser.Math_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#computation.
    def visitComputation(self, ctx:ArtGrammarParser.ComputationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#canvas_def.
    def visitCanvas_def(self, ctx:ArtGrammarParser.Canvas_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#outline_def.
    def visitOutline_def(self, ctx:ArtGrammarParser.Outline_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#outline_params.
    def visitOutline_params(self, ctx:ArtGrammarParser.Outline_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#rgb_def.
    def visitRgb_def(self, ctx:ArtGrammarParser.Rgb_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#fill_def.
    def visitFill_def(self, ctx:ArtGrammarParser.Fill_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#fill_params.
    def visitFill_params(self, ctx:ArtGrammarParser.Fill_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#draw_shape.
    def visitDraw_shape(self, ctx:ArtGrammarParser.Draw_shapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#draw_params.
    def visitDraw_params(self, ctx:ArtGrammarParser.Draw_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#size_shape.
    def visitSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArtGrammarParser#size_params.
    def visitSize_params(self, ctx:ArtGrammarParser.Size_paramsContext):
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