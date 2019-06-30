from ANTLR import RusLangListener, RusLangParser, RusLangLexer
import antlr4 as antlr


class RusLangListenerImpl(RusLangListener.RusLangListener):

    def __init__(self):

        self.code = ""
        self.indent_level = 0
        self.current_level = 0

    def addIndent(self):
        for i in range(0, self.indent_level):
            self.code += "\t"

    def enterVar_type(self, ctx: RusLangParser.RusLangParser.Var_typeContext):
        pass
        # Exit a parse tree produced by RusLangParser#var_type.


    def exitVar_type(self, ctx: RusLangParser.RusLangParser.Var_typeContext):
        pass
        # Enter a parse tree produced by RusLangParser#value.


    def enterValue(self, ctx: RusLangParser.RusLangParser.ValueContext):
        pass
        # Exit a parse tree produced by RusLangParser#value.


    def exitValue(self, ctx: RusLangParser.RusLangParser.ValueContext):
        pass
        # Enter a parse tree produced by RusLangParser#varDeclaration.

    def enterVarDeclaration(self, ctx: RusLangParser.RusLangParser.VarDeclarationContext):

        self.code += str(ctx.T_VAR_ID()) + " = "
        # Exit a parse tree produced by RusLangParser#varDeclaration.


    def exitVarDeclaration(self, ctx: RusLangParser.RusLangParser.VarDeclarationContext):
        self.code += "\n"
        # Enter a parse tree produced by RusLangParser#varAssignment.


    def enterVarAssignment(self, ctx: RusLangParser.RusLangParser.VarAssignmentContext):
        self.code += str(ctx.T_VAR_ID()) + " = "
        # Exit a parse tree produced by RusLangParser#varAssignment.


    def exitVarAssignment(self, ctx: RusLangParser.RusLangParser.VarAssignmentContext):
        self.code += "\n"
        # Enter a parse tree produced by RusLangParser#arithmeticExpression.

    def enterArithmeticExpression(self, ctx: RusLangParser.RusLangParser.ArithmeticExpressionContext):

        if len(ctx.children) > 1:
            if self.current_level == 0:
                text = ctx.getText()
                new_text = ""
                arithmetic_tokens = "+-*/"
                for sign in text:
                    if sign in arithmetic_tokens:
                        new_text += " " + sign + " "
                        arithmetic_tokens.replace(sign, "")
                    else:
                        new_text += sign

                self.code += new_text
        self.current_level += 1

        # Exit a parse tree produced by RusLangParser#arithmeticExpression.

    def exitArithmeticExpression(self, ctx: RusLangParser.RusLangParser.ArithmeticExpressionContext):
        self.current_level -= 1

        # Enter a parse tree produced by RusLangParser#stringExpression.

    def enterStringExpression(self, ctx: RusLangParser.RusLangParser.StringExpressionContext):
        if len(ctx.children) > 1:
            if self.current_level == 0:
                text = ctx.getText()
                text = text.replace("++", " + ")

                self.code += text
        self.current_level += 1
        # Exit a parse tree produced by RusLangParser#stringExpression.

    def exitStringExpression(self, ctx: RusLangParser.RusLangParser.StringExpressionContext):
        self.current_level -= 1
        # Enter a parse tree produced by RusLangParser#booleanExpression.

    def enterBooleanExpression(self, ctx: RusLangParser.RusLangParser.BooleanExpressionContext):
        text = ctx.getText()
        text = text.replace("или", " or ")
        text = text.replace("и", " and ")
        text = text.replace("правда", "true")
        text = text.replace("ложный", "false")
        text = text.replace("не", " not ")

        self.code += text
        # Exit a parse tree produced by RusLangParser#booleanExpression.

    def exitBooleanExpression(self, ctx: RusLangParser.RusLangParser.BooleanExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#printExpression.

    def enterPrintExpression(self, ctx: RusLangParser.RusLangParser.PrintExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#printExpression.

    def exitPrintExpression(self, ctx: RusLangParser.RusLangParser.PrintExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#expression.

    def enterExpression(self, ctx: RusLangParser.RusLangParser.ExpressionContext):
        pass
        # text = ctx.getText()
        # if ctx.varDeclaration() is not None or ctx.varAssignment() is not None:
        #     text = text.replace("<-", "=")
        #     text = text.replace("номер", "")
        #     text = text.replace("надпись", "")
        #     text = text.replace("логический", "")
        #     text = text.replace('правда', "true")
        #     text = text.replace("ложный", "false")
        # elif ctx.printExpression() is not None:
        #     text = text.replace('показ', 'print')
        # elif ctx.forLoopExpression() is not None:
        #     text = text.replace('для', 'for ')
        #     text = text.replace('от', ' in range(')
        #     text = text.replace('до', ',')
        #     text = text.replace(":", "):\n")
        #     text = text.split(":")[0] + ":"
        # elif ctx.whileLoopExpression() is not None:
        #     text = text.replace('пока', 'while ')
        #     text = text.replace(":", "):\n")
        #     text = text.split(":")[0] + ":"
        #
        # self.code += text + "\n"

        # Exit a parse tree produced by RusLangParser#expression.
    def exitExpression(self, ctx: RusLangParser.RusLangParser.ExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#code.

    def enterCode(self, ctx: RusLangParser.RusLangParser.CodeContext):
        pass
        # Exit a parse tree produced by RusLangParser#code.

    def exitCode(self, ctx: RusLangParser.RusLangParser.CodeContext):
        pass
        # Enter a parse tree produced by RusLangParser#program.

    def enterProgram(self, ctx: RusLangParser.RusLangParser.ProgramContext):
        pass
        # Exit a parse tree produced by RusLangParser#program.

    def exitProgram(self, ctx: RusLangParser.RusLangParser.ProgramContext):
        pass
        # Enter a parse tree produced by RusLangParser#forLoopExpression.

    def enterForLoopExpression(self, ctx: RusLangParser.RusLangParser.ForLoopExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#forLoopExpression.

    def exitForLoopExpression(self, ctx: RusLangParser.RusLangParser.ForLoopExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#whileLoopExpression.

    def enterWhileLoopExpression(self, ctx: RusLangParser.RusLangParser.WhileLoopExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#whileLoopExpression.

    def exitWhileLoopExpression(self, ctx: RusLangParser.RusLangParser.WhileLoopExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#loopCode.

    def enterLoopCode(self, ctx: RusLangParser.RusLangParser.LoopCodeContext):
        pass
        # Exit a parse tree produced by RusLangParser#loopCode.

    def exitLoopCode(self, ctx: RusLangParser.RusLangParser.LoopCodeContext):
        pass
        # Enter a parse tree produced by RusLangParser#conditionalExpression.

    def enterConditionalExpression(self, ctx: RusLangParser.RusLangParser.ConditionalExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#conditionalExpression.

    def exitConditionalExpression(self, ctx: RusLangParser.RusLangParser.ConditionalExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#elifExpression.

    def enterElifExpression(self, ctx: RusLangParser.RusLangParser.ElifExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#elifExpression.

    def exitElifExpression(self, ctx: RusLangParser.RusLangParser.ElifExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#elseExpression.

    def enterElseExpression(self, ctx: RusLangParser.RusLangParser.ElseExpressionContext):
        pass
        # Exit a parse tree produced by RusLangParser#elseExpression.

    def exitElseExpression(self, ctx: RusLangParser.RusLangParser.ElseExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#functionDeclaration.

    def enterFunctionDeclaration(self, ctx: RusLangParser.RusLangParser.FunctionDeclarationContext):
        pass
        # Exit a parse tree produced by RusLangParser#functionDeclaration.

    def exitFunctionDeclaration(self, ctx: RusLangParser.RusLangParser.FunctionDeclarationContext):
        pass
        # Enter a parse tree produced by RusLangParser#argList.

    def enterArgList(self, ctx: RusLangParser.RusLangParser.ArgListContext):
        pass
        # Exit a parse tree produced by RusLangParser#argList.

    def exitArgList(self, ctx: RusLangParser.RusLangParser.ArgListContext):
        pass
        # Enter a parse tree produced by RusLangParser#fullArgList.

    def enterFullArgList(self, ctx: RusLangParser.RusLangParser.FullArgListContext):
        pass
        # Exit a parse tree produced by RusLangParser#fullArgList.

    def exitFullArgList(self, ctx: RusLangParser.RusLangParser.FullArgListContext):
        pass
        # Enter a parse tree produced by RusLangParser#functionCall.

    def enterFunctionCall(self, ctx: RusLangParser.RusLangParser.FunctionCallContext):
        pass
        # Exit a parse tree produced by RusLangParser#functionCall.

    def exitFunctionCall(self, ctx: RusLangParser.RusLangParser.FunctionCallContext):
        pass
        # Enter a parse tree produced by RusLangParser#valueList.

    def enterValueList(self, ctx: RusLangParser.RusLangParser.ValueListContext):
        pass
        # Exit a parse tree produced by RusLangParser#valueList.

    def exitValueList(self, ctx: RusLangParser.RusLangParser.ValueListContext):
        pass
        # Enter a parse tree produced by RusLangParser#fullValueList.

    def enterFullValueList(self, ctx: RusLangParser.RusLangParser.FullValueListContext):
        pass
        # Exit a parse tree produced by RusLangParser#fullValueList.

    def exitFullValueList(self, ctx: RusLangParser.RusLangParser.FullValueListContext):
        pass
