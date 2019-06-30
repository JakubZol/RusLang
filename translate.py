from ANTLR import RusLangLexer, RusLangParser
from RusLangListenerImpl import RusLangListenerImpl
from antlr4 import *
import sys


def translate(input_file, output_file):

    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = RusLangLexer.RusLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RusLangParser.RusLangParser(stream)

    tree = parser.program()

    parse_tree_walker = ParseTreeWalker()
    listener = RusLangListenerImpl()

    parse_tree_walker.walk(listener, tree)

    file = open(output_file, "w+")
    file.write(listener.code)
    file.close()


path = str(sys.argv[1])
target = str(sys.argv[2])
translate(path, target)





