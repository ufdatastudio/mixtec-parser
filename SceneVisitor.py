# Generated from Scene.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SceneParser import SceneParser
else:
    from SceneParser import SceneParser

# This class defines a complete generic visitor for a parse tree produced by SceneParser.

class SceneVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SceneParser#s.
    def visitS(self, ctx:SceneParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#sent.
    def visitSent(self, ctx:SceneParser.SentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#clause.
    def visitClause(self, ctx:SceneParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#date_tail.
    def visitDate_tail(self, ctx:SceneParser.Date_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#obj_tail.
    def visitObj_tail(self, ctx:SceneParser.Obj_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#date.
    def visitDate(self, ctx:SceneParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#clause_f.
    def visitClause_f(self, ctx:SceneParser.Clause_fContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SceneParser#near_date.
    def visitNear_date(self, ctx:SceneParser.Near_dateContext):
        return self.visitChildren(ctx)



del SceneParser