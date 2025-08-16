
# scene_interpreter_visitor.py
# XML-based visitor interpreter for ANTLR-generated parse trees
# Parses token XML using ElementTree and returns structured representations

import xml.etree.ElementTree as ET
from antlr4 import *
from SceneParser import SceneParser
from SceneVisitor import SceneVisitor

# Helper function to parse an XML string into a flat dictionary
def parse_token_xml(xml_str: str) -> dict:
    root = ET.fromstring(xml_str)
    return {child.tag: child.text for child in root}

class SceneInterpreterVisitor(SceneVisitor):
    def visitS(self, ctx:SceneParser.SContext):
        return [self.visit(sent) for sent in ctx.sent()]

    def visitSent(self, ctx:SceneParser.SentContext):
        if ctx.clause():
            return self.visit(ctx.clause())
        elif ctx.OBJ():
            if ctx.date():
                return {
                    "type": "obj-date-clause",
                    "obj": parse_token_xml(ctx.OBJ().getText()),
                    "date": self.visit(ctx.date()),
                    "clause": self.visit(ctx.clause())
                }
            else:
                return {
                    "type": "obj-clause",
                    "obj": parse_token_xml(ctx.OBJ().getText()),
                    "clause": self.visit(ctx.clause())
                }
        elif ctx.date():
            if ctx.OBJ():
                return {
                    "type": "date-obj-clause",
                    "date": self.visit(ctx.date()),
                    "obj": parse_token_xml(ctx.OBJ().getText()),
                    "clause": self.visit(ctx.clause())
                }
            else:
                return {
                    "type": "date-clause",
                    "date": self.visit(ctx.date()),
                    "clause": self.visit(ctx.clause())
                }

    def visitClause(self, ctx:SceneParser.ClauseContext):
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        result = {"type": "clause", "elements": clause_fs}
        if ctx.date_tail():
            result["tail"] = self.visit(ctx.date_tail())
        elif ctx.obj_tail():
            result["tail"] = self.visit(ctx.obj_tail())
        return result

    def visitClause_f(self, ctx:SceneParser.Clause_fContext):
        data = {"type": "h", **parse_token_xml(ctx.H().getText())}
        if ctx.ND():
            data["namedate"] = parse_token_xml(ctx.ND().getText())
        elif ctx.near_date():
            data["near_date"] = self.visit(ctx.near_date())
        return data

    def visitDate_tail(self, ctx:SceneParser.Date_tailContext):
        data = {"type": "date_tail", "date": self.visit(ctx.date())}
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        if ctx.OBJ():
            data["obj"] = parse_token_xml(ctx.OBJ().getText())
        if clause_fs:
            data["clauses"] = clause_fs
        return data

    def visitObj_tail(self, ctx:SceneParser.Obj_tailContext):
        data = {"type": "obj_tail", "obj": parse_token_xml(ctx.OBJ().getText())}
        if ctx.date():
            data["date"] = self.visit(ctx.date())
        clause_fs = [self.visit(cf) for cf in ctx.clause_f()]
        if clause_fs:
            data["clauses"] = clause_fs
        return data

    def visitDate(self, ctx:SceneParser.DateContext):
        data = {"type": "date", **parse_token_xml(ctx.Y().getText())}
        if ctx.ND():
            data["namedate"] = parse_token_xml(ctx.ND().getText())
        return data

    def visitNear_date(self, ctx:SceneParser.Near_dateContext):
        data = {"type": "near_obj", **parse_token_xml(ctx.NEAR_OBJ().getText())}
        if ctx.ND():
            data["namedate"] = parse_token_xml(ctx.ND().getText())
        return data
