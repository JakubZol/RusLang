from ANTLR import RusLangLexer, RusLangParser
from RusLangListenerImpl import RusLangListenerImpl
from antlr4 import *


def translate(file):

    input_stream = FileStream(file, encoding='utf-8')

    lexer = RusLangLexer.RusLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RusLangParser.RusLangParser(stream)

    tree = parser.program()

    parse_tree_walker = ParseTreeWalker()
    listener = RusLangListenerImpl()

    parse_tree_walker.walk(listener, tree)

    file = open("out.py", "w+")
    file.write(listener.code)
    file.close()


translate("ruslang.txt")





