# Generated from RusLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RusLangParser import RusLangParser
else:
    from RusLangParser import RusLangParser

# This class defines a complete listener for a parse tree produced by RusLangParser.
class RusLangListener(ParseTreeListener):

    # Enter a parse tree produced by RusLangParser#var_type.
    def enterVar_type(self, ctx:RusLangParser.Var_typeContext):
        pass

    # Exit a parse tree produced by RusLangParser#var_type.
    def exitVar_type(self, ctx:RusLangParser.Var_typeContext):
        pass


    # Enter a parse tree produced by RusLangParser#value.
    def enterValue(self, ctx:RusLangParser.ValueContext):
        pass

    # Exit a parse tree produced by RusLangParser#value.
    def exitValue(self, ctx:RusLangParser.ValueContext):
        pass


    # Enter a parse tree produced by RusLangParser#varDeclaration.
    def enterVarDeclaration(self, ctx:RusLangParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by RusLangParser#varDeclaration.
    def exitVarDeclaration(self, ctx:RusLangParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by RusLangParser#varAssignment.
    def enterVarAssignment(self, ctx:RusLangParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by RusLangParser#varAssignment.
    def exitVarAssignment(self, ctx:RusLangParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by RusLangParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:RusLangParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:RusLangParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#stringExpression.
    def enterStringExpression(self, ctx:RusLangParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#stringExpression.
    def exitStringExpression(self, ctx:RusLangParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#booleanExpression.
    def enterBooleanExpression(self, ctx:RusLangParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#booleanExpression.
    def exitBooleanExpression(self, ctx:RusLangParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#printExpression.
    def enterPrintExpression(self, ctx:RusLangParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#printExpression.
    def exitPrintExpression(self, ctx:RusLangParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#expression.
    def enterExpression(self, ctx:RusLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#expression.
    def exitExpression(self, ctx:RusLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#code.
    def enterCode(self, ctx:RusLangParser.CodeContext):
        pass

    # Exit a parse tree produced by RusLangParser#code.
    def exitCode(self, ctx:RusLangParser.CodeContext):
        pass


    # Enter a parse tree produced by RusLangParser#program.
    def enterProgram(self, ctx:RusLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RusLangParser#program.
    def exitProgram(self, ctx:RusLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RusLangParser#forLoopExpression.
    def enterForLoopExpression(self, ctx:RusLangParser.ForLoopExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#forLoopExpression.
    def exitForLoopExpression(self, ctx:RusLangParser.ForLoopExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#whileLoopExpression.
    def enterWhileLoopExpression(self, ctx:RusLangParser.WhileLoopExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#whileLoopExpression.
    def exitWhileLoopExpression(self, ctx:RusLangParser.WhileLoopExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#loopCode.
    def enterLoopCode(self, ctx:RusLangParser.LoopCodeContext):
        pass

    # Exit a parse tree produced by RusLangParser#loopCode.
    def exitLoopCode(self, ctx:RusLangParser.LoopCodeContext):
        pass


    # Enter a parse tree produced by RusLangParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:RusLangParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:RusLangParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#elifExpression.
    def enterElifExpression(self, ctx:RusLangParser.ElifExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#elifExpression.
    def exitElifExpression(self, ctx:RusLangParser.ElifExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#elseExpression.
    def enterElseExpression(self, ctx:RusLangParser.ElseExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#elseExpression.
    def exitElseExpression(self, ctx:RusLangParser.ElseExpressionContext):
        pass


    # Enter a parse tree produced by RusLangParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:RusLangParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by RusLangParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:RusLangParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by RusLangParser#argList.
    def enterArgList(self, ctx:RusLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by RusLangParser#argList.
    def exitArgList(self, ctx:RusLangParser.ArgListContext):
        pass


    # Enter a parse tree produced by RusLangParser#fullArgList.
    def enterFullArgList(self, ctx:RusLangParser.FullArgListContext):
        pass

    # Exit a parse tree produced by RusLangParser#fullArgList.
    def exitFullArgList(self, ctx:RusLangParser.FullArgListContext):
        pass


    # Enter a parse tree produced by RusLangParser#functionCall.
    def enterFunctionCall(self, ctx:RusLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by RusLangParser#functionCall.
    def exitFunctionCall(self, ctx:RusLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by RusLangParser#valueList.
    def enterValueList(self, ctx:RusLangParser.ValueListContext):
        pass

    # Exit a parse tree produced by RusLangParser#valueList.
    def exitValueList(self, ctx:RusLangParser.ValueListContext):
        pass


    # Enter a parse tree produced by RusLangParser#fullValueList.
    def enterFullValueList(self, ctx:RusLangParser.FullValueListContext):
        pass

    # Exit a parse tree produced by RusLangParser#fullValueList.
    def exitFullValueList(self, ctx:RusLangParser.FullValueListContext):
        pass


