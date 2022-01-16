# Generated from ArtGrammar.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3)\n\3\f\3\16\3,\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3\66\n\3\f\3\16\39\13\3\3\3\3\3\5\3=\n\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4C\n\4\3\5\3\5\3\5\5\5H\n\5\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\ne\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\2\4\3\2\21\22\3\2\3\t\2k\2\35\3\2\2")
        buf.write("\2\4<\3\2\2\2\6B\3\2\2\2\bG\3\2\2\2\nI\3\2\2\2\fL\3\2")
        buf.write("\2\2\16P\3\2\2\2\20T\3\2\2\2\22d\3\2\2\2\24f\3\2\2\2\26")
        buf.write("j\3\2\2\2\30l\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\34\37")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37\35")
        buf.write("\3\2\2\2 !\7\2\2\3!\3\3\2\2\2\"#\7\16\2\2#$\7\22\2\2$")
        buf.write("%\7\25\2\2%&\7\26\2\2&*\7\27\2\2\')\5\b\5\2(\'\3\2\2\2")
        buf.write("),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-=\7")
        buf.write("\30\2\2./\7\16\2\2/\60\7\22\2\2\60\61\7\25\2\2\61\62\5")
        buf.write("\6\4\2\62\63\7\26\2\2\63\67\7\27\2\2\64\66\5\b\5\2\65")
        buf.write("\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3")
        buf.write("\2\2\29\67\3\2\2\2:;\7\30\2\2;=\3\2\2\2<\"\3\2\2\2<.\3")
        buf.write("\2\2\2=\5\3\2\2\2>C\7\22\2\2?@\7\22\2\2@A\7\33\2\2AC\5")
        buf.write("\6\4\2B>\3\2\2\2B?\3\2\2\2C\7\3\2\2\2DH\5\n\6\2EH\5\f")
        buf.write("\7\2FH\5\20\t\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H\t\3\2\2")
        buf.write("\2IJ\5\30\r\2JK\7\22\2\2K\13\3\2\2\2LM\7\22\2\2MN\7\32")
        buf.write("\2\2NO\5\16\b\2O\r\3\2\2\2PQ\5\26\f\2QR\7\23\2\2RS\5\26")
        buf.write("\f\2S\17\3\2\2\2TU\7\22\2\2UV\7\31\2\2VW\7\f\2\2WX\7\25")
        buf.write("\2\2XY\5\22\n\2YZ\7\26\2\2Z\21\3\2\2\2[e\5\24\13\2\\]")
        buf.write("\5\24\13\2]^\7\33\2\2^_\5\26\f\2_e\3\2\2\2`a\5\24\13\2")
        buf.write("ab\7\33\2\2bc\5\24\13\2ce\3\2\2\2d[\3\2\2\2d\\\3\2\2\2")
        buf.write("d`\3\2\2\2e\23\3\2\2\2fg\5\26\f\2gh\7\33\2\2hi\5\26\f")
        buf.write("\2i\25\3\2\2\2jk\t\2\2\2k\27\3\2\2\2lm\t\3\2\2m\31\3\2")
        buf.write("\2\2\t\35*\67<BGd")
        return buf.getvalue()


class ArtGrammarParser ( Parser ):

    grammarFileName = "ArtGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'.'", "'='" ]

    symbolicNames = [ "<INVALID>", "RECTANGLE", "SQUARE", "CIRCLE", "DOT", 
                      "STRAIGHT", "ARC", "PIXEL", "OUTLINE", "DRAW", "SIZE", 
                      "FOR", "DEF", "FILL", "CANVAS", "INTEGER", "IDENTIFIER", 
                      "MATH_OP", "COND_OP", "PAREN_START", "PAREN_END", 
                      "CURLY_START", "CURLY_END", "DOT_NOTATION", "ASSIGN_OP", 
                      "SEPARATOR", "WS" ]

    RULE_expr = 0
    RULE_func = 1
    RULE_func_params = 2
    RULE_code = 3
    RULE_init = 4
    RULE_math_expr = 5
    RULE_computation = 6
    RULE_size_shape = 7
    RULE_params = 8
    RULE_two_params = 9
    RULE_value_type = 10
    RULE_data_type = 11

    ruleNames =  [ "expr", "func", "func_params", "code", "init", "math_expr", 
                   "computation", "size_shape", "params", "two_params", 
                   "value_type", "data_type" ]

    EOF = Token.EOF
    RECTANGLE=1
    SQUARE=2
    CIRCLE=3
    DOT=4
    STRAIGHT=5
    ARC=6
    PIXEL=7
    OUTLINE=8
    DRAW=9
    SIZE=10
    FOR=11
    DEF=12
    FILL=13
    CANVAS=14
    INTEGER=15
    IDENTIFIER=16
    MATH_OP=17
    COND_OP=18
    PAREN_START=19
    PAREN_END=20
    CURLY_START=21
    CURLY_END=22
    DOT_NOTATION=23
    ASSIGN_OP=24
    SEPARATOR=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ArtGrammarParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArtGrammarParser.FuncContext)
            else:
                return self.getTypedRuleContext(ArtGrammarParser.FuncContext,i)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ArtGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ArtGrammarParser.DEF:
                self.state = 24
                self.func()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(ArtGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ArtGrammarParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def PAREN_START(self):
            return self.getToken(ArtGrammarParser.PAREN_START, 0)

        def PAREN_END(self):
            return self.getToken(ArtGrammarParser.PAREN_END, 0)

        def CURLY_START(self):
            return self.getToken(ArtGrammarParser.CURLY_START, 0)

        def CURLY_END(self):
            return self.getToken(ArtGrammarParser.CURLY_END, 0)

        def code(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArtGrammarParser.CodeContext)
            else:
                return self.getTypedRuleContext(ArtGrammarParser.CodeContext,i)


        def func_params(self):
            return self.getTypedRuleContext(ArtGrammarParser.Func_paramsContext,0)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ArtGrammarParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(ArtGrammarParser.DEF)
                self.state = 33
                self.match(ArtGrammarParser.IDENTIFIER)
                self.state = 34
                self.match(ArtGrammarParser.PAREN_START)
                self.state = 35
                self.match(ArtGrammarParser.PAREN_END)
                self.state = 36
                self.match(ArtGrammarParser.CURLY_START)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArtGrammarParser.RECTANGLE) | (1 << ArtGrammarParser.SQUARE) | (1 << ArtGrammarParser.CIRCLE) | (1 << ArtGrammarParser.DOT) | (1 << ArtGrammarParser.STRAIGHT) | (1 << ArtGrammarParser.ARC) | (1 << ArtGrammarParser.PIXEL) | (1 << ArtGrammarParser.IDENTIFIER))) != 0):
                    self.state = 37
                    self.code()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 43
                self.match(ArtGrammarParser.CURLY_END)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(ArtGrammarParser.DEF)
                self.state = 45
                self.match(ArtGrammarParser.IDENTIFIER)
                self.state = 46
                self.match(ArtGrammarParser.PAREN_START)
                self.state = 47
                self.func_params()
                self.state = 48
                self.match(ArtGrammarParser.PAREN_END)
                self.state = 49
                self.match(ArtGrammarParser.CURLY_START)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArtGrammarParser.RECTANGLE) | (1 << ArtGrammarParser.SQUARE) | (1 << ArtGrammarParser.CIRCLE) | (1 << ArtGrammarParser.DOT) | (1 << ArtGrammarParser.STRAIGHT) | (1 << ArtGrammarParser.ARC) | (1 << ArtGrammarParser.PIXEL) | (1 << ArtGrammarParser.IDENTIFIER))) != 0):
                    self.state = 50
                    self.code()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(ArtGrammarParser.CURLY_END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def SEPARATOR(self):
            return self.getToken(ArtGrammarParser.SEPARATOR, 0)

        def func_params(self):
            return self.getTypedRuleContext(ArtGrammarParser.Func_paramsContext,0)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_func_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_params" ):
                listener.enterFunc_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_params" ):
                listener.exitFunc_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_params" ):
                return visitor.visitFunc_params(self)
            else:
                return visitor.visitChildren(self)




    def func_params(self):

        localctx = ArtGrammarParser.Func_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_params)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(ArtGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(ArtGrammarParser.IDENTIFIER)
                self.state = 62
                self.match(ArtGrammarParser.SEPARATOR)
                self.state = 63
                self.func_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init(self):
            return self.getTypedRuleContext(ArtGrammarParser.InitContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(ArtGrammarParser.Math_exprContext,0)


        def size_shape(self):
            return self.getTypedRuleContext(ArtGrammarParser.Size_shapeContext,0)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = ArtGrammarParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_code)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.math_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.size_shape()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(ArtGrammarParser.Data_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = ArtGrammarParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.data_type()
            self.state = 72
            self.match(ArtGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def ASSIGN_OP(self):
            return self.getToken(ArtGrammarParser.ASSIGN_OP, 0)

        def computation(self):
            return self.getTypedRuleContext(ArtGrammarParser.ComputationContext,0)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_math_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expr" ):
                listener.enterMath_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expr" ):
                listener.exitMath_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expr" ):
                return visitor.visitMath_expr(self)
            else:
                return visitor.visitChildren(self)




    def math_expr(self):

        localctx = ArtGrammarParser.Math_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_math_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ArtGrammarParser.IDENTIFIER)
            self.state = 75
            self.match(ArtGrammarParser.ASSIGN_OP)
            self.state = 76
            self.computation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComputationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArtGrammarParser.Value_typeContext)
            else:
                return self.getTypedRuleContext(ArtGrammarParser.Value_typeContext,i)


        def MATH_OP(self):
            return self.getToken(ArtGrammarParser.MATH_OP, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_computation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputation" ):
                listener.enterComputation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputation" ):
                listener.exitComputation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComputation" ):
                return visitor.visitComputation(self)
            else:
                return visitor.visitChildren(self)




    def computation(self):

        localctx = ArtGrammarParser.ComputationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_computation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.value_type()
            self.state = 79
            self.match(ArtGrammarParser.MATH_OP)
            self.state = 80
            self.value_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_shapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def DOT_NOTATION(self):
            return self.getToken(ArtGrammarParser.DOT_NOTATION, 0)

        def SIZE(self):
            return self.getToken(ArtGrammarParser.SIZE, 0)

        def PAREN_START(self):
            return self.getToken(ArtGrammarParser.PAREN_START, 0)

        def params(self):
            return self.getTypedRuleContext(ArtGrammarParser.ParamsContext,0)


        def PAREN_END(self):
            return self.getToken(ArtGrammarParser.PAREN_END, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_size_shape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize_shape" ):
                listener.enterSize_shape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize_shape" ):
                listener.exitSize_shape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize_shape" ):
                return visitor.visitSize_shape(self)
            else:
                return visitor.visitChildren(self)




    def size_shape(self):

        localctx = ArtGrammarParser.Size_shapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_size_shape)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ArtGrammarParser.IDENTIFIER)
            self.state = 83
            self.match(ArtGrammarParser.DOT_NOTATION)
            self.state = 84
            self.match(ArtGrammarParser.SIZE)
            self.state = 85
            self.match(ArtGrammarParser.PAREN_START)
            self.state = 86
            self.params()
            self.state = 87
            self.match(ArtGrammarParser.PAREN_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def two_params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArtGrammarParser.Two_paramsContext)
            else:
                return self.getTypedRuleContext(ArtGrammarParser.Two_paramsContext,i)


        def SEPARATOR(self):
            return self.getToken(ArtGrammarParser.SEPARATOR, 0)

        def value_type(self):
            return self.getTypedRuleContext(ArtGrammarParser.Value_typeContext,0)


        def getRuleIndex(self):
            return ArtGrammarParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ArtGrammarParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.two_params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.two_params()
                self.state = 91
                self.match(ArtGrammarParser.SEPARATOR)
                self.state = 92
                self.value_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.two_params()
                self.state = 95
                self.match(ArtGrammarParser.SEPARATOR)
                self.state = 96
                self.two_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Two_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArtGrammarParser.Value_typeContext)
            else:
                return self.getTypedRuleContext(ArtGrammarParser.Value_typeContext,i)


        def SEPARATOR(self):
            return self.getToken(ArtGrammarParser.SEPARATOR, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_two_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTwo_params" ):
                listener.enterTwo_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTwo_params" ):
                listener.exitTwo_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTwo_params" ):
                return visitor.visitTwo_params(self)
            else:
                return visitor.visitChildren(self)




    def two_params(self):

        localctx = ArtGrammarParser.Two_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_two_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.value_type()
            self.state = 101
            self.match(ArtGrammarParser.SEPARATOR)
            self.state = 102
            self.value_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ArtGrammarParser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(ArtGrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_value_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_type" ):
                listener.enterValue_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_type" ):
                listener.exitValue_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_type" ):
                return visitor.visitValue_type(self)
            else:
                return visitor.visitChildren(self)




    def value_type(self):

        localctx = ArtGrammarParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==ArtGrammarParser.INTEGER or _la==ArtGrammarParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIRCLE(self):
            return self.getToken(ArtGrammarParser.CIRCLE, 0)

        def RECTANGLE(self):
            return self.getToken(ArtGrammarParser.RECTANGLE, 0)

        def SQUARE(self):
            return self.getToken(ArtGrammarParser.SQUARE, 0)

        def DOT(self):
            return self.getToken(ArtGrammarParser.DOT, 0)

        def STRAIGHT(self):
            return self.getToken(ArtGrammarParser.STRAIGHT, 0)

        def ARC(self):
            return self.getToken(ArtGrammarParser.ARC, 0)

        def PIXEL(self):
            return self.getToken(ArtGrammarParser.PIXEL, 0)

        def getRuleIndex(self):
            return ArtGrammarParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = ArtGrammarParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArtGrammarParser.RECTANGLE) | (1 << ArtGrammarParser.SQUARE) | (1 << ArtGrammarParser.CIRCLE) | (1 << ArtGrammarParser.DOT) | (1 << ArtGrammarParser.STRAIGHT) | (1 << ArtGrammarParser.ARC) | (1 << ArtGrammarParser.PIXEL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





