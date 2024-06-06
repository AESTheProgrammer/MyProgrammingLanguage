# Generated from C:/Users/armin/Desktop/Worksapce/Projects/YetAnotherLang/Expr.g4 by ANTLR 4.13.1
from antlr4 import *

from Block import Block
from Expression import Expression
from FunctionCall import FunctionCall
from IfStmt import IfStmt
from Multiplication import Multiplication
from Addition import Addition
from Parenthesis import Parenthesis
from Subtraction import Subtraction
from Division import Division
from LessThan import LessThan
from gen.ExprVisitor import ExprVisitor
from gen.ExprParser import ExprParser
from VariableDeclaration import VariableDeclaration
from Variable import Variable
from Number import Number
from Program import Program
from FunctionDeclaration import FunctionDeclaration

from typing import Set, List, Tuple, Union, Dict

valueTypes = Union[int]


class AntlrToProgram(ExprVisitor):
    vars: List[Set[str]] = []
    funcs: Dict[str, FunctionDeclaration] = {}
    semanticErrors: List[str] = []  # 1. duplicate declarations 2. reference to undeclared

    # Visit a parse tree produced by ExprParser#Program.
    def visitProgram(self, ctx: ExprParser.ProgramContext) -> ExprParser:
        prog = Program()
        childCnt = ctx.getChildCount()
        for i in range(childCnt):
            if i == childCnt - 1:
                # this child is EOF
                pass
            else:
                # self.vars: [str] = []
                prog.add_block(self.visit(ctx.getChild(i)))
        return prog

    # Visit a parse tree produced by ExprParser#FunctionDecl.
    def visitFunctionDecl(self, ctx: ExprParser.FunctionDeclContext) -> FunctionDeclaration:
        idToken: Token = ctx.ID().getSymbol()
        line = idToken.line
        column = idToken.column + 1
        identifier = ctx.ID().getText()
        params = self.visit(ctx.params())
        block = self.visit(ctx.blok())
        functionDeclaration = FunctionDeclaration(identifier, block, params)
        if identifier in self.funcs:
            self.semanticErrors.append(f"Error: Function {identifier} is already declared({line}, {column})")
        else:
            self.funcs[identifier] = functionDeclaration
        return functionDeclaration

    # Visit a parse tree produced by ExprParser#Parameters.
    def visitParameters(self, ctx: ExprParser.ParametersContext) -> ExprParser:
        parameters: List[Tuple[str, str]] = []
        for i in range(0, ctx.getChildCount(), 3):
            parameters.append((ctx.getChild(i).getText(), ctx.getChild(i + 1).getText()))
        return parameters

    # Visit a parse tree produced by ExprParser#Block.
    def visitBlock(self, ctx: ExprParser.BlockContext) -> Block:
        self.vars.append(set())
        block = Block()
        childCnt = ctx.getChildCount()
        for i in range(childCnt):
            if i == 0 or i == childCnt - 1:
                pass
            else:
                block.add_expr(self.visit(ctx.getChild(i)))
        self.vars.pop()
        return block

    # Visit a parse tree produced by ExprParser#IfStmt.
    def visitIfStmt(self, ctx: ExprParser.IfStmtContext) -> IfStmt:
        condition = self.visit(ctx.expr())
        block = self.visit(ctx.blok())
        return IfStmt(condition, block)

    # Visit a parse tree produced by ExprParser#Declaration.
    def visitDeclaration(self, ctx: ExprParser.DeclarationContext) -> VariableDeclaration:
        idToken: Token = ctx.ID().getSymbol()
        line = idToken.line
        column = idToken.column + 1
        identifier = ctx.ID().getText()
        if identifier in self.vars[-1]:
            self.semanticErrors.append(f"Error: Variable {identifier} already declared({line}, {column})")
        else:
            self.vars.append(identifier)
        type = ctx.getChild(2).getText()
        value = int(ctx.NUM().getText())
        return VariableDeclaration(identifier, type, value)

    # Visit a parse tree produced by ExprParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx: ExprParser.ParenthesizedExprContext):
        # print(ctx.expr().getText())
        return Parenthesis(self.visit(ctx.expr()))

    # Visit a parse tree produced by ExprParser#Multiplication.
    def visitMulOrDiv(self, ctx: ExprParser.MulOrDivContext) -> Union[Division, Multiplication]:
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if ctx.getChild(1).getText() == '*':
            return Multiplication(left, right)
        if ctx.getChild(1).getText() == '/':
            return Division(left, right)

    # Visit a parse tree produced by ExprParser#Subtraction.
    def visitSubOrAdd(self, ctx: ExprParser.SubOrAddContext) -> Union[Addition, Subtraction]:
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if ctx.getChild(1).getText() == '-':
            return Subtraction(left, right)
        if ctx.getChild(1).getText() == '+':
            return Addition(left, right)

    # Visit a parse tree produced by ExprParser#LessThan.
    def visitLessThan(self, ctx: ExprParser.LessThanContext) -> LessThan:
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return LessThan(left, right)

    # Visit a parse tree produced by ExprParser#Variable.
    def visitVariable(self, ctx: ExprParser.VariableContext) -> Variable:
        idToken: Token = ctx.ID().getSymbol()
        line = idToken.line
        column = idToken.column + 1
        identifier = ctx.ID().getText()
        isVariableDeclared = False
        for blocksVars in self.vars:
            if identifier in blocksVars:
                isVariableDeclared = True
                break
        if not isVariableDeclared:
            self.semanticErrors.append(f"Error: Variable {identifier} not declared({line}, {column})")
        return Variable(identifier)

    # Visit a parse tree produced by ExprParser#Number.
    def visitNumber(self, ctx: ExprParser.NumberContext) -> Number:
        return Number(int(ctx.NUM().getText()))

    # Visit a parse tree produced by ExprParser#FunctionCall.
    def visitFunctionCall(self, ctx: ExprParser.FunctionCallContext) -> FunctionCall:
        idToken: Token = ctx.ID().getSymbol()
        line = idToken.line
        column = idToken.column + 1
        identifier = ctx.ID().getText()
        if identifier not in self.funcs:
            self.semanticErrors.append(f"Error: Function {identifier} not declared({line}, {column})")
        args: List[Expression] = []
        for i in range(2, ctx.getChildCount() - 1, 2):
            args.append(self.visit((ctx.getChild(i))))
        if len(args) != self.funcs[identifier].getParamCount():
            self.semanticErrors.append(f"Error: {len(args)} arguments were given, {self.funcs[identifier].getParamCount()} ({line}, {column})")
        return FunctionCall(identifier, args)


del ExprParser
