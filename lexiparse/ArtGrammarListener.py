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


    # Enter a parse tree produced by ArtGrammarParser#consts.
    def enterConsts(self, ctx:ArtGrammarParser.ConstsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#consts.
    def exitConsts(self, ctx:ArtGrammarParser.ConstsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#glob.
    def enterGlob(self, ctx:ArtGrammarParser.GlobContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#glob.
    def exitGlob(self, ctx:ArtGrammarParser.GlobContext):
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


    # Enter a parse tree produced by ArtGrammarParser#loop.
    def enterLoop(self, ctx:ArtGrammarParser.LoopContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#loop.
    def exitLoop(self, ctx:ArtGrammarParser.LoopContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#loop_body.
    def enterLoop_body(self, ctx:ArtGrammarParser.Loop_bodyContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#loop_body.
    def exitLoop_body(self, ctx:ArtGrammarParser.Loop_bodyContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#loop_init.
    def enterLoop_init(self, ctx:ArtGrammarParser.Loop_initContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#loop_init.
    def exitLoop_init(self, ctx:ArtGrammarParser.Loop_initContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#loop_cond.
    def enterLoop_cond(self, ctx:ArtGrammarParser.Loop_condContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#loop_cond.
    def exitLoop_cond(self, ctx:ArtGrammarParser.Loop_condContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#loop_incdec.
    def enterLoop_incdec(self, ctx:ArtGrammarParser.Loop_incdecContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#loop_incdec.
    def exitLoop_incdec(self, ctx:ArtGrammarParser.Loop_incdecContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#init.
    def enterInit(self, ctx:ArtGrammarParser.InitContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#init.
    def exitInit(self, ctx:ArtGrammarParser.InitContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#init_int.
    def enterInit_int(self, ctx:ArtGrammarParser.Init_intContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#init_int.
    def exitInit_int(self, ctx:ArtGrammarParser.Init_intContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#init_bool.
    def enterInit_bool(self, ctx:ArtGrammarParser.Init_boolContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#init_bool.
    def exitInit_bool(self, ctx:ArtGrammarParser.Init_boolContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#func_call.
    def enterFunc_call(self, ctx:ArtGrammarParser.Func_callContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#func_call.
    def exitFunc_call(self, ctx:ArtGrammarParser.Func_callContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#call_params.
    def enterCall_params(self, ctx:ArtGrammarParser.Call_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#call_params.
    def exitCall_params(self, ctx:ArtGrammarParser.Call_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#if_else.
    def enterIf_else(self, ctx:ArtGrammarParser.If_elseContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#if_else.
    def exitIf_else(self, ctx:ArtGrammarParser.If_elseContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#if_cond.
    def enterIf_cond(self, ctx:ArtGrammarParser.If_condContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#if_cond.
    def exitIf_cond(self, ctx:ArtGrammarParser.If_condContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#elif_cond.
    def enterElif_cond(self, ctx:ArtGrammarParser.Elif_condContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#elif_cond.
    def exitElif_cond(self, ctx:ArtGrammarParser.Elif_condContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#else_cond.
    def enterElse_cond(self, ctx:ArtGrammarParser.Else_condContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#else_cond.
    def exitElse_cond(self, ctx:ArtGrammarParser.Else_condContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#condition_base.
    def enterCondition_base(self, ctx:ArtGrammarParser.Condition_baseContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#condition_base.
    def exitCondition_base(self, ctx:ArtGrammarParser.Condition_baseContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#condition_body.
    def enterCondition_body(self, ctx:ArtGrammarParser.Condition_bodyContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#condition_body.
    def exitCondition_body(self, ctx:ArtGrammarParser.Condition_bodyContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#condition.
    def enterCondition(self, ctx:ArtGrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#condition.
    def exitCondition(self, ctx:ArtGrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#ifel_body.
    def enterIfel_body(self, ctx:ArtGrammarParser.Ifel_bodyContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#ifel_body.
    def exitIfel_body(self, ctx:ArtGrammarParser.Ifel_bodyContext):
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


    # Enter a parse tree produced by ArtGrammarParser#canvas_def.
    def enterCanvas_def(self, ctx:ArtGrammarParser.Canvas_defContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#canvas_def.
    def exitCanvas_def(self, ctx:ArtGrammarParser.Canvas_defContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#outline_def.
    def enterOutline_def(self, ctx:ArtGrammarParser.Outline_defContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#outline_def.
    def exitOutline_def(self, ctx:ArtGrammarParser.Outline_defContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#outline_params.
    def enterOutline_params(self, ctx:ArtGrammarParser.Outline_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#outline_params.
    def exitOutline_params(self, ctx:ArtGrammarParser.Outline_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#rgb_def.
    def enterRgb_def(self, ctx:ArtGrammarParser.Rgb_defContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#rgb_def.
    def exitRgb_def(self, ctx:ArtGrammarParser.Rgb_defContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#fill_def.
    def enterFill_def(self, ctx:ArtGrammarParser.Fill_defContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#fill_def.
    def exitFill_def(self, ctx:ArtGrammarParser.Fill_defContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#fill_params.
    def enterFill_params(self, ctx:ArtGrammarParser.Fill_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#fill_params.
    def exitFill_params(self, ctx:ArtGrammarParser.Fill_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#draw_shape.
    def enterDraw_shape(self, ctx:ArtGrammarParser.Draw_shapeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#draw_shape.
    def exitDraw_shape(self, ctx:ArtGrammarParser.Draw_shapeContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#draw_params.
    def enterDraw_params(self, ctx:ArtGrammarParser.Draw_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#draw_params.
    def exitDraw_params(self, ctx:ArtGrammarParser.Draw_paramsContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#size_shape.
    def enterSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#size_shape.
    def exitSize_shape(self, ctx:ArtGrammarParser.Size_shapeContext):
        pass


    # Enter a parse tree produced by ArtGrammarParser#size_params.
    def enterSize_params(self, ctx:ArtGrammarParser.Size_paramsContext):
        pass

    # Exit a parse tree produced by ArtGrammarParser#size_params.
    def exitSize_params(self, ctx:ArtGrammarParser.Size_paramsContext):
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