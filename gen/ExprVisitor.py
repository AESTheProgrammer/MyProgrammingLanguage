# Generated from C:/Users/armin/Desktop/Worksapce/Projects/YetAnotherLang/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#Program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FunctionDecl.
    def visitFunctionDecl(self, ctx:ExprParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfStmt.
    def visitIfStmt(self, ctx:ExprParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Parameters.
    def visitParameters(self, ctx:ExprParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#LessThan.
    def visitLessThan(self, ctx:ExprParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Number.
    def visitNumber(self, ctx:ExprParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulOrDiv.
    def visitMulOrDiv(self, ctx:ExprParser.MulOrDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:ExprParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FunctionCall.
    def visitFunctionCall(self, ctx:ExprParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#SubOrAdd.
    def visitSubOrAdd(self, ctx:ExprParser.SubOrAddContext):
        return self.visitChildren(ctx)



del ExprParser