# Generated from C:/Users/camil/OneDrive - University of South Florida/Desktop/ANTLR/Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#start.
    def enterStart(self, ctx:GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by GrammarParser#start.
    def exitStart(self, ctx:GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by GrammarParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:GrammarParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:GrammarParser.MulDivExprContext):
        # Check if this is a division operation
        if ctx.op.type == GrammarParser.DIV:
            # The denominator is the second expression in the MulDivExpr rule
            denominator = ctx.expr(1)

            # Check if the denominator is zero
            if denominator.getText() == '0':
                raise ValueError("Division by zero is not allowed!")
        pass


    # Enter a parse tree produced by GrammarParser#IntExpr.
    def enterIntExpr(self, ctx:GrammarParser.IntExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#IntExpr.
    def exitIntExpr(self, ctx:GrammarParser.IntExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#ParenExpr.
    def enterParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#ParenExpr.
    def exitParenExpr(self, ctx:GrammarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:GrammarParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:GrammarParser.AddSubExprContext):
        pass



del GrammarParser