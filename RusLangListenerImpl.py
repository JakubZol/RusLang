from ANTLR import RusLangListener, RusLangParser, RusLangLexer
import antlr4 as antlr
from antlr4.tree import Tree as t


class RusLangListenerImpl(RusLangListener.RusLangListener):

    def __init__(self):

        self.code = ""
        self.indent_level = 0
        self.complement_for = False

    def addIndent(self):
        indent_string = ""
        for i in range(0, self.indent_level):
            indent_string += "\t"
        return indent_string


    def enterVar_type(self, ctx: RusLangParser.RusLangParser.Var_typeContext):
        pass
        # Exit a parse tree produced by RusLangParser#var_type.


    def exitVar_type(self, ctx: RusLangParser.RusLangParser.Var_typeContext):
        pass
        # Enter a parse tree produced by RusLangParser#value.

    def enterListValue(self, ctx:RusLangParser.RusLangParser.ListValueContext):
        pass

    # Exit a parse tree produced by RusLangParser#listValue.
    def exitListValue(self, ctx:RusLangParser.RusLangParser.ListValueContext):
        pass


    # Enter a parse tree produced by RusLangParser#listExpression.
    def enterListExpression(self, ctx:RusLangParser.RusLangParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by RusLangParser#listExpression.
    def exitListExpression(self, ctx:RusLangParser.RusLangParser.ListExpressionContext):
        pass

    def enterValue(self, ctx: RusLangParser.RusLangParser.ValueContext):
        pass
        # Exit a parse tree produced by RusLangParser#value.


    def exitValue(self, ctx: RusLangParser.RusLangParser.ValueContext):
        pass
        # Enter a parse tree produced by RusLangParser#varDeclaration.

    def enterVarDeclaration(self, ctx: RusLangParser.RusLangParser.VarDeclarationContext):
        pass
        # Exit a parse tree produced by RusLangParser#varDeclaration.


    def exitVarDeclaration(self, ctx: RusLangParser.RusLangParser.VarDeclarationContext):
        pass
        # Enter a parse tree produced by RusLangParser#varAssignment.


    def enterVarAssignment(self, ctx: RusLangParser.RusLangParser.VarAssignmentContext):
        pass
        # Exit a parse tree produced by RusLangParser#varAssignment.


    def exitVarAssignment(self, ctx: RusLangParser.RusLangParser.VarAssignmentContext):
        pass

    def enterArithmeticExpression(self, ctx: RusLangParser.RusLangParser.ArithmeticExpressionContext):
        pass

        # Exit a parse tree produced by RusLangParser#arithmeticExpression.

    def exitArithmeticExpression(self, ctx: RusLangParser.RusLangParser.ArithmeticExpressionContext):
        pass

        # Enter a parse tree produced by RusLangParser#stringExpression.

    def enterStringExpression(self, ctx: RusLangParser.RusLangParser.StringExpressionContext):
        pass

        # Exit a parse tree produced by RusLangParser#stringExpression.

    def exitStringExpression(self, ctx: RusLangParser.RusLangParser.StringExpressionContext):
        pass
        # Enter a parse tree produced by RusLangParser#booleanExpression.

    def enterBooleanExpression(self, ctx: RusLangParser.RusLangParser.BooleanExpressionContext):
        pass

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

    def visitTerminal(self, node:t.TerminalNode):

        ttype = node.getSymbol().type
        parser = RusLangParser.RusLangParser

        immutable_values = [parser.T_VAR_ID, parser.T_NUMBER_VAL, parser.T_STRING_VAL, parser.T_LSQUARE,
                            parser.T_RSQUARE, parser.T_LBRACKET, parser.T_RBRACKET]
        immutable_ops = [parser.T_PLUS, parser.T_MINUS, parser.T_MUL, parser.T_DIV, parser.T_G, parser.T_L,
                         parser.T_GEQ, parser.T_LEQ]
        mutables = {
            parser.T_DOTS: ":\n",
            parser.T_END_LINE: "\n",
            parser.T_POW: " ** ",
            parser.T_CONCAT: " + ",
            parser.T_ASSIGN: " = ",
            parser.T_EQ: " == ",
            parser.T_NEQ: " != ",
            parser.T_COMMA: ", ",
            parser.T_NOT: " not ",
            parser.T_AND: " and ",
            parser.T_OR: " or ",
            parser.T_TRUE: "True",
            parser.T_FALSE: "False",
            parser.T_WHILE: "while ",
            parser.T_PRINT: "print",
            parser.T_FOR: "for ",
            parser.T_FROM: " in range (",
            parser.T_TO: ", ",
            parser.T_BREAK: "break",
            parser.T_CONTINUE: "continue",
            parser.T_RETURN: "return ",
            parser.T_FUNCTION: "def "
        }

        if ttype in immutable_ops:
            self.code += " " + node.getText() + " "
        if ttype in immutable_values:
            self.code += node.getText()
        if ttype in mutables.keys():

            if ttype == parser.T_DOTS and self.complement_for:
                self.complement_for = False
                self.code += ")"

            self.code += mutables[ttype]

            if ttype == parser.T_FOR:
                self.complement_for = True
            if ttype == parser.T_DOTS:
                self.indent_level += 1
                self.code += self.addIndent()

            if ttype == parser.T_END_LINE:
                self.code += self.addIndent()
        if ttype == parser.T_END:
            self.indent_level -= 1




