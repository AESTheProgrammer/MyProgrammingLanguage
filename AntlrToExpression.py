# # Generated from C:/Users/armin/Desktop/Worksapce/Projects/YetAnotherLang\Expr.g4 by ANTLR 4.12.0
# from antlr4 import *
# from Multiplication import Multiplication
# from Addition import Addition
# from VariableDeclaration import VariableDeclaration
# from Variable import Variable
# from gen.ExprParser import ExprParser
# from gen.ExprVisitor import ExprVisitor
#
#
# class AntlrToExpression(ExprVisitor):
#     vars = {}
#
#     # Visit a parse tree produced by ExprParser#Program.
#     def visitProgram(self, ctx: ExprParser.ProgramContext):
#         return self.visitChildren(ctx)
#
#     # Visit a parse tree produced by ExprParser#Declaration.
#     def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
#         decl = VariableDeclaration(ctx.ID(), ctx.INT_TYPE(), ctx.NUM())
#         self.vars[ctx.ID()] = decl
#         return self.visitChildren(ctx)
#
#     # Visit a parse tree produced by ExprParser#Multiplication.
#     def visitMultiplication(self, ctx: ExprParser.MultiplicationContext):
#         left = self.visit(ctx.getChild(0))
#         right = self.visit(ctx.getChild(2))
#         return Multiplication(left, right)
#
#     # Visit a parse tree produced by ExprParser#Addition.
#     def visitAddition(self, ctx: ExprParser.AdditionContext):
#         left = self.visit(ctx.getChild(0))
#         right = self.visit(ctx.getChild(2))
#         return Addition(left, right)
#
#     # Visit a parse tree produced by ExprParser#Variable.
#     def visitVariable(self, ctx: ExprParser.VariableContext):
#         return self.visitChildren(ctx)
#
#     # Visit a parse tree produced by ExprParser#Number.
#     def visitNumber(self, ctx: ExprParser.NumberContext):
#         return self.visitChildren(ctx)
#
#
# del ExprParser
