# Generated from Scene.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,30,8,1,1,1,1,1,1,1,1,1,3,1,36,8,1,3,1,38,8,1,1,2,4,2,41,
        8,2,11,2,12,2,42,1,2,1,2,3,2,47,8,2,1,3,1,3,1,3,4,3,52,8,3,11,3,
        12,3,53,1,3,4,3,57,8,3,11,3,12,3,58,3,3,61,8,3,1,4,1,4,1,4,4,4,66,
        8,4,11,4,12,4,67,1,4,4,4,71,8,4,11,4,12,4,72,3,4,75,8,4,1,5,1,5,
        3,5,79,8,5,1,6,1,6,1,6,3,6,84,8,6,1,7,1,7,3,7,88,8,7,1,7,0,0,8,0,
        2,4,6,8,10,12,14,0,0,101,0,19,1,0,0,0,2,37,1,0,0,0,4,40,1,0,0,0,
        6,48,1,0,0,0,8,62,1,0,0,0,10,76,1,0,0,0,12,80,1,0,0,0,14,85,1,0,
        0,0,16,17,3,2,1,0,17,18,5,6,0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,
        1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,38,3,4,2,0,24,
        29,5,4,0,0,25,26,3,10,5,0,26,27,3,4,2,0,27,30,1,0,0,0,28,30,3,4,
        2,0,29,25,1,0,0,0,29,28,1,0,0,0,30,38,1,0,0,0,31,35,3,10,5,0,32,
        33,5,4,0,0,33,36,3,4,2,0,34,36,3,4,2,0,35,32,1,0,0,0,35,34,1,0,0,
        0,36,38,1,0,0,0,37,23,1,0,0,0,37,24,1,0,0,0,37,31,1,0,0,0,38,3,1,
        0,0,0,39,41,3,12,6,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,
        43,1,0,0,0,43,46,1,0,0,0,44,47,3,6,3,0,45,47,3,8,4,0,46,44,1,0,0,
        0,46,45,1,0,0,0,46,47,1,0,0,0,47,5,1,0,0,0,48,60,3,10,5,0,49,51,
        5,4,0,0,50,52,3,12,6,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,61,1,0,0,0,55,57,3,12,6,0,56,55,1,0,0,0,57,58,1,
        0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,49,1,0,0,0,60,
        56,1,0,0,0,60,61,1,0,0,0,61,7,1,0,0,0,62,74,5,4,0,0,63,65,3,10,5,
        0,64,66,3,12,6,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,75,1,0,0,0,69,71,3,12,6,0,70,69,1,0,0,0,71,72,1,0,0,0,
        72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,63,1,0,0,0,74,70,1,
        0,0,0,74,75,1,0,0,0,75,9,1,0,0,0,76,78,5,2,0,0,77,79,5,3,0,0,78,
        77,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,83,5,1,0,0,81,84,5,3,0,
        0,82,84,3,14,7,0,83,81,1,0,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,13,
        1,0,0,0,85,87,5,5,0,0,86,88,5,3,0,0,87,86,1,0,0,0,87,88,1,0,0,0,
        88,15,1,0,0,0,15,21,29,35,37,42,46,53,58,60,67,72,74,78,83,87
    ]

class SceneParser ( Parser ):

    grammarFileName = "Scene.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<End/>'" ]

    symbolicNames = [ "<INVALID>", "H", "Y", "ND", "OBJ", "NEAR_OBJ", "END", 
                      "WS" ]

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
    H=1
    Y=2
    ND=3
    OBJ=4
    NEAR_OBJ=5
    END=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0)):
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
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.clause()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(SceneParser.OBJ)
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 25
                    self.date()
                    self.state = 26
                    self.clause()
                    pass
                elif token in [1]:
                    self.state = 28
                    self.clause()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.date()
                self.state = 35
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 32
                    self.match(SceneParser.OBJ)
                    self.state = 33
                    self.clause()
                    pass
                elif token in [1]:
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
                if not (_la==1):
                    break

            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 44
                self.date_tail()
                pass
            elif token in [4]:
                self.state = 45
                self.obj_tail()
                pass
            elif token in [6]:
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
            if token in [4]:
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
                    if not (_la==1):
                        break

                pass
            elif token in [1]:
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 55
                    self.clause_f()
                    self.state = 58 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                pass
            elif token in [6]:
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
            if token in [2]:
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
                    if not (_la==1):
                        break

                pass
            elif token in [1]:
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 69
                    self.clause_f()
                    self.state = 72 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                pass
            elif token in [6]:
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
            if _la==3:
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
            if token in [3]:
                self.state = 81
                self.match(SceneParser.ND)
                pass
            elif token in [5]:
                self.state = 82
                self.near_date()
                pass
            elif token in [1, 2, 4, 6]:
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
            if _la==3:
                self.state = 86
                self.match(SceneParser.ND)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





