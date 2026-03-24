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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\6\2\31\n\2\r\2\16")
        buf.write("\2\32\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3+\n\3\5\3-\n\3\3\4\6\4\60\n\4\r\4\16\4\61")
        buf.write("\3\4\3\4\5\4\66\n\4\3\5\3\5\3\5\6\5;\n\5\r\5\16\5<\3\5")
        buf.write("\6\5@\n\5\r\5\16\5A\5\5D\n\5\3\6\3\6\3\6\6\6I\n\6\r\6")
        buf.write("\16\6J\3\6\6\6N\n\6\r\6\16\6O\5\6R\n\6\3\7\3\7\5\7V\n")
        buf.write("\7\3\b\3\b\3\b\5\b[\n\b\3\t\3\t\5\t_\n\t\3\t\2\2\n\2\4")
        buf.write("\6\b\n\f\16\20\2\2\2l\2\22\3\2\2\2\4,\3\2\2\2\6/\3\2\2")
        buf.write("\2\b\67\3\2\2\2\nE\3\2\2\2\fS\3\2\2\2\16W\3\2\2\2\20\\")
        buf.write("\3\2\2\2\22\23\7\13\2\2\23\30\7\b\2\2\24\25\7\f\2\2\25")
        buf.write("\26\5\4\3\2\26\27\7\r\2\2\27\31\3\2\2\2\30\24\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2")
        buf.write("\2\34\35\7\t\2\2\35\3\3\2\2\2\36-\5\6\4\2\37$\7\6\2\2")
        buf.write(" !\5\f\7\2!\"\5\6\4\2\"%\3\2\2\2#%\5\6\4\2$ \3\2\2\2$")
        buf.write("#\3\2\2\2%-\3\2\2\2&*\5\f\7\2\'(\7\6\2\2(+\5\6\4\2)+\5")
        buf.write("\6\4\2*\'\3\2\2\2*)\3\2\2\2+-\3\2\2\2,\36\3\2\2\2,\37")
        buf.write("\3\2\2\2,&\3\2\2\2-\5\3\2\2\2.\60\5\16\b\2/.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\65\3\2\2\2\63")
        buf.write("\66\5\b\5\2\64\66\5\n\6\2\65\63\3\2\2\2\65\64\3\2\2\2")
        buf.write("\65\66\3\2\2\2\66\7\3\2\2\2\67C\5\f\7\28:\7\6\2\29;\5")
        buf.write("\16\b\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=D\3\2")
        buf.write("\2\2>@\5\16\b\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2")
        buf.write("\2BD\3\2\2\2C8\3\2\2\2C?\3\2\2\2CD\3\2\2\2D\t\3\2\2\2")
        buf.write("EQ\7\6\2\2FH\5\f\7\2GI\5\16\b\2HG\3\2\2\2IJ\3\2\2\2JH")
        buf.write("\3\2\2\2JK\3\2\2\2KR\3\2\2\2LN\5\16\b\2ML\3\2\2\2NO\3")
        buf.write("\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QF\3\2\2\2QM\3\2\2")
        buf.write("\2QR\3\2\2\2R\13\3\2\2\2SU\7\3\2\2TV\7\5\2\2UT\3\2\2\2")
        buf.write("UV\3\2\2\2V\r\3\2\2\2WZ\7\4\2\2X[\7\5\2\2Y[\5\20\t\2Z")
        buf.write("X\3\2\2\2ZY\3\2\2\2Z[\3\2\2\2[\17\3\2\2\2\\^\7\7\2\2]")
        buf.write("_\7\5\2\2^]\3\2\2\2^_\3\2\2\2_\21\3\2\2\2\21\32$*,\61")
        buf.write("\65<ACJOQUZ^")
        return buf.getvalue()


class SceneParser ( Parser ):

    grammarFileName = "Scene.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<document>'", "'</document>'", 
                     "<INVALID>", "<INVALID>", "'<scene>'", "'</scene>'" ]

    symbolicNames = [ "<INVALID>", "Y", "H", "ND", "OBJ", "NEAR_OBJ", "DOCUMENT_OPEN", 
                      "DOCUMENT_CLOSE", "WS", "XML_DECL", "SCENE_OPEN", 
                      "SCENE_CLOSE" ]

    RULE_document = 0
    RULE_sent = 1
    RULE_clause = 2
    RULE_date_tail = 3
    RULE_obj_tail = 4
    RULE_date = 5
    RULE_clause_f = 6
    RULE_near_date = 7

    ruleNames =  [ "document", "sent", "clause", "date_tail", "obj_tail", 
                   "date", "clause_f", "near_date" ]

    EOF = Token.EOF
    Y=1
    H=2
    ND=3
    OBJ=4
    NEAR_OBJ=5
    DOCUMENT_OPEN=6
    DOCUMENT_CLOSE=7
    WS=8
    XML_DECL=9
    SCENE_OPEN=10
    SCENE_CLOSE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML_DECL(self):
            return self.getToken(SceneParser.XML_DECL, 0)

        def DOCUMENT_OPEN(self):
            return self.getToken(SceneParser.DOCUMENT_OPEN, 0)

        def DOCUMENT_CLOSE(self):
            return self.getToken(SceneParser.DOCUMENT_CLOSE, 0)

        def SCENE_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(SceneParser.SCENE_OPEN)
            else:
                return self.getToken(SceneParser.SCENE_OPEN, i)

        def sent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SceneParser.SentContext)
            else:
                return self.getTypedRuleContext(SceneParser.SentContext,i)


        def SCENE_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(SceneParser.SCENE_CLOSE)
            else:
                return self.getToken(SceneParser.SCENE_CLOSE, i)

        def getRuleIndex(self):
            return SceneParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = SceneParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SceneParser.XML_DECL)
            self.state = 17
            self.match(SceneParser.DOCUMENT_OPEN)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.match(SceneParser.SCENE_OPEN)
                self.state = 19
                self.sent()
                self.state = 20
                self.match(SceneParser.SCENE_CLOSE)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SceneParser.SCENE_OPEN):
                    break

            self.state = 26
            self.match(SceneParser.DOCUMENT_CLOSE)
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.H]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.clause()
                pass
            elif token in [SceneParser.OBJ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(SceneParser.OBJ)
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SceneParser.Y]:
                    self.state = 30
                    self.date()
                    self.state = 31
                    self.clause()
                    pass
                elif token in [SceneParser.H]:
                    self.state = 33
                    self.clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SceneParser.Y]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.date()
                self.state = 40
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SceneParser.OBJ]:
                    self.state = 37
                    self.match(SceneParser.OBJ)
                    self.state = 38
                    self.clause()
                    pass
                elif token in [SceneParser.H]:
                    self.state = 39
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
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.clause_f()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SceneParser.H):
                    break

            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.Y]:
                self.state = 49
                self.date_tail()
                pass
            elif token in [SceneParser.OBJ]:
                self.state = 50
                self.obj_tail()
                pass
            elif token in [SceneParser.SCENE_CLOSE]:
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
            self.state = 53
            self.date()
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.OBJ]:
                self.state = 54
                self.match(SceneParser.OBJ)
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
            elif token in [SceneParser.H]:
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 60
                    self.clause_f()
                    self.state = 63 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.SCENE_CLOSE]:
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
            self.state = 67
            self.match(SceneParser.OBJ)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.Y]:
                self.state = 68
                self.date()
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
            elif token in [SceneParser.H]:
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 74
                    self.clause_f()
                    self.state = 77 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SceneParser.H):
                        break

                pass
            elif token in [SceneParser.SCENE_CLOSE]:
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
            self.state = 81
            self.match(SceneParser.Y)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SceneParser.ND:
                self.state = 82
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
            self.state = 85
            self.match(SceneParser.H)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SceneParser.ND]:
                self.state = 86
                self.match(SceneParser.ND)
                pass
            elif token in [SceneParser.NEAR_OBJ]:
                self.state = 87
                self.near_date()
                pass
            elif token in [SceneParser.Y, SceneParser.H, SceneParser.OBJ, SceneParser.SCENE_CLOSE]:
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
            self.state = 90
            self.match(SceneParser.NEAR_OBJ)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SceneParser.ND:
                self.state = 91
                self.match(SceneParser.ND)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





