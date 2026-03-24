# Generated from Scene.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SceneParser import SceneParser
else:
    from SceneParser import SceneParser

# This class defines a complete listener for a parse tree produced by SceneParser.
class SceneListener(ParseTreeListener):

    # Enter a parse tree produced by SceneParser#document.
    def enterDocument(self, ctx:SceneParser.DocumentContext):
        pass

    # Exit a parse tree produced by SceneParser#document.
    def exitDocument(self, ctx:SceneParser.DocumentContext):
        pass


    # Enter a parse tree produced by SceneParser#sent.
    def enterSent(self, ctx:SceneParser.SentContext):
        pass

    # Exit a parse tree produced by SceneParser#sent.
    def exitSent(self, ctx:SceneParser.SentContext):
        pass


    # Enter a parse tree produced by SceneParser#clause.
    def enterClause(self, ctx:SceneParser.ClauseContext):
        pass

    # Exit a parse tree produced by SceneParser#clause.
    def exitClause(self, ctx:SceneParser.ClauseContext):
        pass


    # Enter a parse tree produced by SceneParser#date_tail.
    def enterDate_tail(self, ctx:SceneParser.Date_tailContext):
        pass

    # Exit a parse tree produced by SceneParser#date_tail.
    def exitDate_tail(self, ctx:SceneParser.Date_tailContext):
        pass


    # Enter a parse tree produced by SceneParser#obj_tail.
    def enterObj_tail(self, ctx:SceneParser.Obj_tailContext):
        pass

    # Exit a parse tree produced by SceneParser#obj_tail.
    def exitObj_tail(self, ctx:SceneParser.Obj_tailContext):
        pass


    # Enter a parse tree produced by SceneParser#date.
    def enterDate(self, ctx:SceneParser.DateContext):
        pass

    # Exit a parse tree produced by SceneParser#date.
    def exitDate(self, ctx:SceneParser.DateContext):
        pass


    # Enter a parse tree produced by SceneParser#clause_f.
    def enterClause_f(self, ctx:SceneParser.Clause_fContext):
        pass

    # Exit a parse tree produced by SceneParser#clause_f.
    def exitClause_f(self, ctx:SceneParser.Clause_fContext):
        pass


    # Enter a parse tree produced by SceneParser#near_date.
    def enterNear_date(self, ctx:SceneParser.Near_dateContext):
        pass

    # Exit a parse tree produced by SceneParser#near_date.
    def exitNear_date(self, ctx:SceneParser.Near_dateContext):
        pass



del SceneParser