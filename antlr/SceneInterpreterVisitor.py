from antlr.SceneVisitor import SceneVisitor
from antlr.SceneParser import SceneParser
from tree_node import *
from antlr.TokenConvertor import TokenConvertor
import tokens as tokens

class SceneInterpreterVisitor(SceneVisitor):

    def visitS(self, ctx: SceneParser.SContext):
        children = []
        for sent_ctx, end_ctx in zip(ctx.sent(), ctx.END()):
            sent_node = self.visit(sent_ctx)
            end_token = TokenConvertor.convert_token(end_ctx.getSymbol())
            end_node = LeafNode(end_token)
            children.append(sent_node)
            children.append(end_node)

        return Start(first_token=None, children=children).interpret()

    def visitSent(self, ctx: SceneParser.SentContext):
        children = []
        for child in ctx.getChildren():
            if hasattr(child, 'accept'):
                children.append(self.visit(child))
        first_token = children[0].get_token()
        return Sent(first_token, children)

    def visitClause(self, ctx: SceneParser.ClauseContext):
        children = []
        for child in ctx.getChildren():
            if hasattr(child, 'accept'):
                children.append(self.visit(child))
        first_token = children[0].get_token()
        return Clause(first_token, children)

    def visitDate_tail(self, ctx: SceneParser.Date_tailContext):
        children = []
        for child in ctx.getChildren():
            if hasattr(child, 'accept'):
                children.append(self.visit(child))
        first_token = children[0].get_token()
        return DateTail(first_token, children)

    def visitObj_tail(self, ctx: SceneParser.Obj_tailContext):
        children = []

        # First child is always the OBJ
        obj_token = TokenConvertor.convert_token(ctx.OBJ().getSymbol())
        children.append(LeafNode(obj_token))

        if ctx.date():
            date_node = self.visit(ctx.date())
            children.append(date_node)
        clause_fs = ctx.clause_f()
        for cf in clause_fs:
            children.append(self.visit(cf))

        first_token = children[0].get_token()
        return ObjTail(first_token, children)

    def visitDate(self, ctx: SceneParser.DateContext):
        children = []
        year_token = TokenConvertor.convert_token(ctx.Y().getSymbol())
        children.append(LeafNode(year_token))

        if ctx.ND():
            nd_token = TokenConvertor.convert_token(ctx.ND().getSymbol())
            children.append(LeafNode(nd_token))

        return Date(year_token, children)

    def visitClause_f(self, ctx: SceneParser.Clause_fContext):
        children = []
        h_token = TokenConvertor.convert_token(ctx.H().getSymbol())
        children.append(LeafNode(h_token))

        if ctx.ND():
            nd_token = TokenConvertor.convert_token(ctx.ND().getSymbol())
            children.append(LeafNode(nd_token))
        elif ctx.near_date():
            children.append(self.visit(ctx.near_date()))

        return ClauseF(h_token, children)

    def visitNear_date(self, ctx: SceneParser.Near_dateContext):
        children = []
        near_obj_token = TokenConvertor.convert_token(ctx.NEAR_OBJ().getSymbol())
        children.append(LeafNode(near_obj_token))

        if ctx.ND():
            nd_token = TokenConvertor.convert_token(ctx.ND().getSymbol())
            children.append(LeafNode(nd_token))

        return NearDate(near_obj_token, children)
