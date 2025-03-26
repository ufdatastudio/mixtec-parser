# gabrielayoubi03
# Implements a visitor-based interpreter for the ANTLR-generated parse tree (SceneParser)
# This class walks the parse tree and builds a nested dictionary representing the scene semantics

from antlr4 import *
from SceneParser import SceneParser
from SceneVisitor import SceneVisitor  # ANTLR-generated base class

class SceneInterpreterVisitor(SceneVisitor):
    # Entry point: visit the root rule 's' which consists of one or more 'sent' entries
    def visitS(self, ctx:SceneParser.SContext):
        return [self.visit(sent) for sent in ctx.sent()]

    # Visit a sentence (sent) which could be a clause, or involve an object and/or date
    def visitSent(self, ctx:SceneParser.SentContext):
        if ctx.clause():
            return self.visit(ctx.clause())
        elif ctx.OBJ():
            if ctx.date():
                return {
                    "type": "obj-date-clause",
                    "obj": ctx.OBJ().getText(),
                    "date": self.visit(ctx.date()),
                    "clause": self.visit(ctx.clause())
                }
            else:
                return {
                    "type": "obj-clause",
                    "obj": ctx.OBJ().getText(),
                    "clause": self.visit(ctx.clause())
                }
        elif ctx.date():
            if ctx.OBJ():
                return {
                    "type": "date-obj-clause",
                    "date": self.visit(ctx.date()),
                    "obj": ctx.OBJ().getText(),
                    "clause": self.visit(ctx.clause())
                }
            else:
                return {
                    "type": "date-clause",
                    "date": self.visit(ctx.date()),
                    "clause": self.visit(ctx.clause())
                }

    # Visit a clause: one or more humans, optionally followed by a date_tail or obj_tail
    def visitClause(self, ctx:SceneParser.ClauseContext):
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        result = {"type": "clause", "elements": clause_fs}
        if ctx.date_tail():
            result["tail"] = self.visit(ctx.date_tail())
        elif ctx.obj_tail():
            result["tail"] = self.visit(ctx.obj_tail())
        return result

    # Visit a simple human clause feature (clause_f), optionally with a date or near object
    def visitClause_f(self, ctx:SceneParser.Clause_fContext):
        base = {"type": "h"}
        if ctx.ND():
            base["nd"] = ctx.ND().getText()
        elif ctx.near_date():
            base["near_date"] = self.visit(ctx.near_date())
        return base

    # Visit a date_tail which includes a date, and may optionally include obj + human(s)
    def visitDate_tail(self, ctx:SceneParser.Date_tailContext):
        data = {"type": "date_tail", "date": self.visit(ctx.date())}
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        if ctx.OBJ():
            data["obj"] = ctx.OBJ().getText()
        if clause_fs:
            data["clauses"] = clause_fs
        return data

    # Visit an obj_tail which includes obj, and optionally a date and human(s)
    def visitObj_tail(self, ctx:SceneParser.Obj_tailContext):
        data = {"type": "obj_tail", "obj": ctx.OBJ().getText()}
        if ctx.date():
            data["date"] = self.visit(ctx.date())
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        if clause_fs:
            data["clauses"] = clause_fs
        return data

    # Visit a date token: 'y' followed by optional 'nd' (name-date)
    def visitDate(self, ctx:SceneParser.DateContext):
        data = {"type": "date", "y": ctx.Y().getText()}
        if ctx.ND():
            data["nd"] = ctx.ND().getText()
        return data

    # Visit a near_date token: 'near_obj' optionally followed by 'nd'
    def visitNear_date(self, ctx:SceneParser.Near_dateContext):
        data = {"type": "near_obj", "value": ctx.NEAR_OBJ().getText()}
        if ctx.ND():
            data["nd"] = ctx.ND().getText()
        return data