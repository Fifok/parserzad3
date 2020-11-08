# Generated from .\Graph.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\6\4%\n\4\r\4\16\4&\3")
        buf.write("\5\3\5\3\6\6\6,\n\6\r\6\16\6-\3\6\6\6\61\n\6\r\6\16\6")
        buf.write("\62\3\7\3\7\3\7\3\7\3\7\3\b\6\b;\n\b\r\b\16\b<\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fX\n\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\2\2\16\3\3\5\2\7\4\t\5\13\6\r\7")
        buf.write("\17\b\21\t\23\n\25\13\27\f\31\r\3\2\b\3\2\62;\4\2C\\c")
        buf.write("|\4\2]]__\4\2\13\13\"\"\4\2\f\f\17\17\5\2$$}}\177\177")
        buf.write("\2c\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5!\3\2")
        buf.write("\2\2\7$\3\2\2\2\t(\3\2\2\2\13+\3\2\2\2\r\64\3\2\2\2\17")
        buf.write(":\3\2\2\2\21>\3\2\2\2\23B\3\2\2\2\25F\3\2\2\2\27W\3\2")
        buf.write("\2\2\31[\3\2\2\2\33\34\7i\2\2\34\35\7t\2\2\35\36\7c\2")
        buf.write("\2\36\37\7r\2\2\37 \7j\2\2 \4\3\2\2\2!\"\t\2\2\2\"\6\3")
        buf.write("\2\2\2#%\5\5\3\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'\b\3\2\2\2()\t\3\2\2)\n\3\2\2\2*,\5\t\5\2+*\3\2")
        buf.write("\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\61\5\5")
        buf.write("\3\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\f\3\2\2\2\64\65\5\23\n\2\65\66\7/\2\2\66\67\7")
        buf.write("/\2\2\678\5\23\n\28\16\3\2\2\29;\t\2\2\2:9\3\2\2\2;<\3")
        buf.write("\2\2\2<:\3\2\2\2<=\3\2\2\2=\20\3\2\2\2>?\t\4\2\2?@\3\2")
        buf.write("\2\2@A\b\t\2\2A\22\3\2\2\2BC\t\5\2\2CD\3\2\2\2DE\b\n\2")
        buf.write("\2E\24\3\2\2\2FG\t\6\2\2GH\3\2\2\2HI\b\13\2\2I\26\3\2")
        buf.write("\2\2JX\t\7\2\2KL\7p\2\2LM\7c\2\2MN\7o\2\2NO\7g\2\2OX\7")
        buf.write("?\2\2PQ\7y\2\2QR\7g\2\2RS\7k\2\2ST\7i\2\2TU\7j\2\2UV\7")
        buf.write("v\2\2VX\7?\2\2WJ\3\2\2\2WK\3\2\2\2WP\3\2\2\2XY\3\2\2\2")
        buf.write("YZ\b\f\2\2Z\30\3\2\2\2[\\\7=\2\2\\]\3\2\2\2]^\b\r\2\2")
        buf.write("^\32\3\2\2\2\b\2&-\62<W\3\2\3\2")
        return buf.getvalue()


class GraphLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE = 1
    NUMBER = 2
    LETTER = 3
    CHAR = 4
    EDGE = 5
    WEIGHT = 6
    BRACKET = 7
    WHITESPACE = 8
    NEWLINE = 9
    IGNORE = 10
    SEMICOLON = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'graph'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "NUMBER", "LETTER", "CHAR", "EDGE", "WEIGHT", "BRACKET", 
            "WHITESPACE", "NEWLINE", "IGNORE", "SEMICOLON" ]

    ruleNames = [ "TYPE", "DIGIT", "NUMBER", "LETTER", "CHAR", "EDGE", "WEIGHT", 
                  "BRACKET", "WHITESPACE", "NEWLINE", "IGNORE", "SEMICOLON" ]

    grammarFileName = "Graph.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


