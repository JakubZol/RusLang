from ANTLR import RusLangLexer, RusLangListener, RusLangParser
from RusLangListenerImpl import RusLangListenerImpl
from antlr4 import *


# def read_file(path):
#     file = open(path, "r")
#     content = file.readlines()
#     string_content = ""
#     return string_content.join(content)


input_stream = FileStream("test.txt", encoding='utf-8')

lexer = RusLangLexer.RusLangLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = RusLangParser.RusLangParser(stream)

tree = parser.program()

parse_tree_walker = ParseTreeWalker()
listener = RusLangListenerImpl()


parse_tree_walker.walk(listener, tree)
print(listener.code)





