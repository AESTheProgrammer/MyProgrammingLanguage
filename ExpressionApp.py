from Block import Block
from gen.ExprParser import ExprParser
from gen.ExprLexer import ExprLexer
from gen.ExprVisitor import ExprVisitor
from AntrlToProgram import AntlrToProgram
from ExpressionProcessor import ExpressionProcessor
from antlr4 import FileStream, CommonTokenStream
import sys


def getParser(fileName: str) -> ExprParser:
    input = FileStream(fileName)
    lexer = ExprLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    return parser


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Usage: file name"
    fileName = sys.argv[1]
    parser = getParser(fileName)
    antlrAST = parser.prog()
    exprVisitor = AntlrToProgram()  # ExprVisitor()
    prog = exprVisitor.visitProgram(antlrAST)
    if len(exprVisitor.semanticErrors) > 0:
        for err in exprVisitor.semanticErrors:
            print(err)
    else:
        ep = ExpressionProcessor(prog.blocks)
        for evaluation in ep.getEvaluationResult():
            print(evaluation)
    print("============DONE!=============")