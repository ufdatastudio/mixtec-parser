# Generated from Scene.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3 \n\3\3\3\3\3\3\3\3\3\5\3&\n\3\5")
        buf.write("\3(\n\3\3\4\6\4+\n\4\r\4\16\4,\3\4\3\4\5\4\61\n\4\3\5")
        buf.write("\3\5\3\5\6\5\66\n\5\r\5\16\5\67\3\5\6\5;\n\5\r\5\16\5")
        buf.write("<\5\5?\n\5\3\6\3\6\3\6\6\6D\n\6\r\6\16\6E\3\6\6\6I\n\6")
        buf.write("\r\6\16\6J\5\6M\n\6\3\7\3\7\5\7Q\n\7\3\b\3\b\3\b\5\bV")
        buf.write("\n\b\3\t\3\t\5\tZ\n\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2")
        buf.write("\2g\2\25\3\2\2\2\4\'\3\2\2\2\6*\3\2\2\2\b\62\3\2\2\2\n")
        buf.write("@\3\2\2\2\fN\3\2\2\2\16R\3\2\2\2\20W\3\2\2\2\22\23\5\4")
        buf.write("\3\2\23\24\7\b\2\2\24\26\3\2\2\2\25\22\3\2\2\2\26\27\3")
        buf.write("\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31(\5")
        buf.write("\6\4\2\32\37\7\6\2\2\33\34\5\f\7\2\34\35\5\6\4\2\35 \3")
        buf.write("\2\2\2\36 \5\6\4\2\37\33\3\2\2\2\37\36\3\2\2\2 (\3\2\2")
        buf.write("\2!%\5\f\7\2\"#\7\6\2\2#&\5\6\4\2$&\5\6\4\2%\"\3\2\2\2")
        buf.write("%$\3\2\2\2&(\3\2\2\2\'\31\3\2\2\2\'\32\3\2\2\2\'!\3\2")
        buf.write("\2\2(\5\3\2\2\2)+\5\16\b\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2")
        buf.write("\2,-\3\2\2\2-\60\3\2\2\2.\61\5\b\5\2/\61\5\n\6\2\60.\3")
        buf.write("\2\2\2\60/\3\2\2\2\60\61\3\2\2\2\61\7\3\2\2\2\62>\5\f")
        buf.write("\7\2\63\65\7\6\2\2\64\66\5\16\b\2\65\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28?\3\2\2\29;\5\16\b")
        buf.write("\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2>")
        buf.write("\63\3\2\2\2>:\3\2\2\2>?\3\2\2\2?\t\3\2\2\2@L\7\6\2\2A")
        buf.write("C\5\f\7\2BD\5\16\b\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3")
        buf.write("\2\2\2FM\3\2\2\2GI\5\16\b\2HG\3\2\2\2IJ\3\2\2\2JH\3\2")
        buf.write("\2\2JK\3\2\2\2KM\3\2\2\2LA\3\2\2\2LH\3\2\2\2LM\3\2\2\2")
        buf.write("M\13\3\2\2\2NP\7\3\2\2OQ\7\5\2\2PO\3\2\2\2PQ\3\2\2\2Q")
        buf.write("\r\3\2\2\2RU\7\4\2\2SV\7\5\2\2TV\5\20\t\2US\3\2\2\2UT")
        buf.write("\3\2\2\2UV\3\2\2\2V\17\3\2\2\2WY\7\7\2\2XZ\7\5\2\2YX\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\21\3\2\2\2\21\27\37%\',\60\67<>EJLP")
        buf.write("UY")
        return buf.getvalue()


class SceneParser ( Parser ):

    grammarFileName = "Scene.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<scene>'", "'</scene>'" ]

    symbolicNames = [ "<INVALID>", "Y", "H", "ND", "OBJ", "NEAR_OBJ", "END", 
                      "WS", "XML_DECL", "SCENE_OPEN", "SCENE_CLOSE" ]

    RULE_s = 0
    RULE_sent = 1
    RULE_clause = 2
    RULE_date_tail = 3
    RULE_obj_tail = 4
    RULE_date = 5
    RULE_clause_f = 6
    RULE_near_date = 7

    ruleNames =  [ "s", "sent", "clause", "date_tail", "obj_tail", "date", 
                   "clause_f", "near_date" ]

    EOF = Token.EOF
    Y=1
    H=2
    ND=3
    OBJ=4
    NEAR_OBJ=5
    END=6
    WS=7
    XML_DECL=8
    SCENE_OPEN=9
    SCENE_CLOSE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SceneParser.SentContext)
            else:
                return self.getTypedRuleContext(SceneParser.SentContext,i)


        def END(self, i:int=None):
            if i is None:
                return self.getTokens(SceneParser.END)
            else:
                return self.getToken(SceneParser.END, i)

        def getRuleIndex(self):
            return SceneParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = SceneParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sent()
                self.state = 17
                self.match(SceneParser.END)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SceneParser.Y) | (1 << SceneParser.H) | (1 << SceneParser.OBJ))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self):
            return self.getTypedRuleContext(SceneParser.ClauseContext,0)


        def OBJ(self):
            return self.getToken(SceneParser.OBJ, 0)

        def date(self):
            return self.getTypedRuleContext(SceneParser.DateContext,0)


        def getRuleIndex(self):
            return SceneParser.RULE_sent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSent" ):
                listener.enterSent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSent" ):
                listener.exitSent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSent" ):
                return visitor.visitSent(self)
            else:
                return visitor.visitChildren(self)




    def sent(self):

        localctx = SceneParser.SentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sent)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.H]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.clause()
                pass
            elif token in [SceneParser.OBJ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(SceneParser.OBJ)
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SceneParser.Y]:
                    self.state = 25
                    self.date()
                    self.state = 26
                    self.clause()
                    pass
                elif token in [SceneParser.H]:
                    self.state = 28
                    self.clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SceneParser.Y]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.date()
                self.state = 35
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SceneParser.OBJ]:
                    self.state = 32
                    self.match(SceneParser.OBJ)
                    self.state = 33
                    self.clause()
                    pass
                elif token in [SceneParser.H]:
                    self.state = 34
                    self.clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause_f(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SceneParser.Clause_fContext)
            else:
                return self.getTypedRuleContext(SceneParser.Clause_fContext,i)


        def date_tail(self):
            return self.getTypedRuleContext(SceneParser.Date_tailContext,0)


        def obj_tail(self):
            return self.getTypedRuleContext(SceneParser.Obj_tailContext,0)


        def getRuleIndex(self):
            return SceneParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause" ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause" ):
                listener.exitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClause" ):
                return visitor.visitClause(self)
            else:
                return visitor.visitChildren(self)




    def clause(self):

        localctx = SceneParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.clause_f()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SceneParser.H):
                    break

            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.Y]:
                self.state = 44
                self.date_tail()
                pass
            elif token in [SceneParser.OBJ]:
                self.state = 45
                self.obj_tail()
                pass
            elif token in [SceneParser.END]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Date_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date(self):
            return self.getTypedRuleContext(SceneParser.DateContext,0)


        def OBJ(self):
            return self.getToken(SceneParser.OBJ, 0)

        def clause_f(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SceneParser.Clause_fContext)
            else:
                return self.getTypedRuleContext(SceneParser.Clause_fContext,i)


        def getRuleIndex(self):
            return SceneParser.RULE_date_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_tail" ):
                listener.enterDate_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_tail" ):
                listener.exitDate_tail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate_tail" ):
                return visitor.visitDate_tail(self)
            else:
                return visitor.visitChildren(self)




    def date_tail(self):

        localctx = SceneParser.Date_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_date_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.date()
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.OBJ]:
                self.state = 49
                self.match(SceneParser.OBJ)
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.clause_f()
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.H]:
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 55
                    self.clause_f()
                    self.state = 58 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.END]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJ(self):
            return self.getToken(SceneParser.OBJ, 0)

        def date(self):
            return self.getTypedRuleContext(SceneParser.DateContext,0)


        def clause_f(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SceneParser.Clause_fContext)
            else:
                return self.getTypedRuleContext(SceneParser.Clause_fContext,i)


        def getRuleIndex(self):
            return SceneParser.RULE_obj_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj_tail" ):
                listener.enterObj_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj_tail" ):
                listener.exitObj_tail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_tail" ):
                return visitor.visitObj_tail(self)
            else:
                return visitor.visitChildren(self)




    def obj_tail(self):

        localctx = SceneParser.Obj_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_obj_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SceneParser.OBJ)
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.Y]:
                self.state = 63
                self.date()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 64
                    self.clause_f()
                    self.state = 67 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.H]:
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 69
                    self.clause_f()
                    self.state = 72 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.END]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Y(self):
            return self.getToken(SceneParser.Y, 0)

        def ND(self):
            return self.getToken(SceneParser.ND, 0)

        def getRuleIndex(self):
            return SceneParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)




    def date(self):

        localctx = SceneParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_date)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SceneParser.Y)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SceneParser.ND:
                self.state = 77
                self.match(SceneParser.ND)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Clause_fContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def H(self):
            return self.getToken(SceneParser.H, 0)

        def ND(self):
            return self.getToken(SceneParser.ND, 0)

        def near_date(self):
            return self.getTypedRuleContext(SceneParser.Near_dateContext,0)


        def getRuleIndex(self):
            return SceneParser.RULE_clause_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause_f" ):
                listener.enterClause_f(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause_f" ):
                listener.exitClause_f(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClause_f" ):
                return visitor.visitClause_f(self)
            else:
                return visitor.visitChildren(self)




    def clause_f(self):

        localctx = SceneParser.Clause_fContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_clause_f)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SceneParser.H)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.ND]:
                self.state = 81
                self.match(SceneParser.ND)
                pass
            elif token in [SceneParser.NEAR_OBJ]:
                self.state = 82
                self.near_date()
                pass
            elif token in [SceneParser.Y, SceneParser.H, SceneParser.OBJ, SceneParser.END]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Near_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEAR_OBJ(self):
            return self.getToken(SceneParser.NEAR_OBJ, 0)

        def ND(self):
            return self.getToken(SceneParser.ND, 0)

        def getRuleIndex(self):
            return SceneParser.RULE_near_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNear_date" ):
                listener.enterNear_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNear_date" ):
                listener.exitNear_date(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNear_date" ):
                return visitor.visitNear_date(self)
            else:
                return visitor.visitChildren(self)




    def near_date(self):

        localctx = SceneParser.Near_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_near_date)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SceneParser.NEAR_OBJ)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SceneParser.ND:
                self.state = 86
                self.match(SceneParser.ND)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





