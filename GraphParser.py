# Generated from .\Graph.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\6\2\37\n\2\r\2\16\2 \3\3\3\3\3\4\3\4")
        buf.write("\3\5\6\5(\n\5\r\5\16\5)\3\6\3\6\3\6\3\7\3\7\6\7\61\n\7")
        buf.write("\r\7\16\7\62\5\7\65\n\7\3\b\3\b\3\b\3\b\3\b\3\t\6\t=\n")
        buf.write("\t\r\t\16\t>\3\n\6\nB\n\n\r\n\16\nC\3\13\6\13G\n\13\r")
        buf.write("\13\16\13H\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2H\2")
        buf.write("\26\3\2\2\2\4\"\3\2\2\2\6$\3\2\2\2\b\'\3\2\2\2\n+\3\2")
        buf.write("\2\2\f\64\3\2\2\2\16\66\3\2\2\2\20<\3\2\2\2\22A\3\2\2")
        buf.write("\2\24F\3\2\2\2\26\27\5\4\3\2\27\31\5\6\4\2\30\32\5\n\6")
        buf.write("\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\36\3\2\2\2\35\37\5\16\b\2\36\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 \36\3\2\2\2 !\3\2\2\2!\3\3\2\2\2\"#\7\3\2\2#\5")
        buf.write("\3\2\2\2$%\7\5\2\2%\7\3\2\2\2&(\7\4\2\2\'&\3\2\2\2()\3")
        buf.write("\2\2\2)\'\3\2\2\2)*\3\2\2\2*\t\3\2\2\2+,\5\b\5\2,-\5\f")
        buf.write("\7\2-\13\3\2\2\2.\65\7\6\2\2/\61\7\5\2\2\60/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2")
        buf.write("\64.\3\2\2\2\64\60\3\2\2\2\65\r\3\2\2\2\66\67\5\22\n\2")
        buf.write("\678\7\7\2\289\5\24\13\29:\5\20\t\2:\17\3\2\2\2;=\7\4")
        buf.write("\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\21\3\2\2")
        buf.write("\2@B\7\4\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("\23\3\2\2\2EG\7\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI")
        buf.write("\3\2\2\2I\25\3\2\2\2\n\33 )\62\64>CH")
        return buf.getvalue()


class GraphParser ( Parser ):

    grammarFileName = "Graph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'graph'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "TYPE", "NUMBER", "LETTER", "CHAR", "EDGE", 
                      "WEIGHT", "BRACKET", "WHITESPACE", "NEWLINE", "IGNORE", 
                      "SEMICOLON" ]

    RULE_graph = 0
    RULE_typegraph = 1
    RULE_namegraph = 2
    RULE_nodeindex = 3
    RULE_node = 4
    RULE_name = 5
    RULE_edge = 6
    RULE_weight = 7
    RULE_source = 8
    RULE_destination = 9

    ruleNames =  [ "graph", "typegraph", "namegraph", "nodeindex", "node", 
                   "name", "edge", "weight", "source", "destination" ]

    EOF = Token.EOF
    TYPE=1
    NUMBER=2
    LETTER=3
    CHAR=4
    EDGE=5
    WEIGHT=6
    BRACKET=7
    WHITESPACE=8
    NEWLINE=9
    IGNORE=10
    SEMICOLON=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typegraph(self):
            return self.getTypedRuleContext(GraphParser.TypegraphContext,0)


        def namegraph(self):
            return self.getTypedRuleContext(GraphParser.NamegraphContext,0)


        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.NodeContext)
            else:
                return self.getTypedRuleContext(GraphParser.NodeContext,i)


        def edge(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.EdgeContext)
            else:
                return self.getTypedRuleContext(GraphParser.EdgeContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)




    def graph(self):

        localctx = GraphParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_graph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.typegraph()
            self.state = 21
            self.namegraph()
            self.state = 23 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 22
                    self.node()

                else:
                    raise NoViableAltException(self)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.edge()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GraphParser.NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypegraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GraphParser.TYPE, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_typegraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypegraph" ):
                listener.enterTypegraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypegraph" ):
                listener.exitTypegraph(self)




    def typegraph(self):

        localctx = GraphParser.TypegraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typegraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(GraphParser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamegraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(GraphParser.LETTER, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_namegraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamegraph" ):
                listener.enterNamegraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamegraph" ):
                listener.exitNamegraph(self)




    def namegraph(self):

        localctx = GraphParser.NamegraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namegraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GraphParser.LETTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeindexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.NUMBER)
            else:
                return self.getToken(GraphParser.NUMBER, i)

        def getRuleIndex(self):
            return GraphParser.RULE_nodeindex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeindex" ):
                listener.enterNodeindex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeindex" ):
                listener.exitNodeindex(self)




    def nodeindex(self):

        localctx = GraphParser.NodeindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nodeindex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.match(GraphParser.NUMBER)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GraphParser.NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeindex(self):
            return self.getTypedRuleContext(GraphParser.NodeindexContext,0)


        def name(self):
            return self.getTypedRuleContext(GraphParser.NameContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = GraphParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.nodeindex()
            self.state = 42
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(GraphParser.CHAR, 0)

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.LETTER)
            else:
                return self.getToken(GraphParser.LETTER, i)

        def getRuleIndex(self):
            return GraphParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = GraphParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphParser.CHAR]:
                self.state = 44
                self.match(GraphParser.CHAR)
                pass
            elif token in [GraphParser.LETTER]:
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 45
                    self.match(GraphParser.LETTER)
                    self.state = 48 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==GraphParser.LETTER):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def source(self):
            return self.getTypedRuleContext(GraphParser.SourceContext,0)


        def EDGE(self):
            return self.getToken(GraphParser.EDGE, 0)

        def destination(self):
            return self.getTypedRuleContext(GraphParser.DestinationContext,0)


        def weight(self):
            return self.getTypedRuleContext(GraphParser.WeightContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)




    def edge(self):

        localctx = GraphParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.source()
            self.state = 53
            self.match(GraphParser.EDGE)
            self.state = 54
            self.destination()
            self.state = 55
            self.weight()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeightContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.NUMBER)
            else:
                return self.getToken(GraphParser.NUMBER, i)

        def getRuleIndex(self):
            return GraphParser.RULE_weight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeight" ):
                listener.enterWeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeight" ):
                listener.exitWeight(self)




    def weight(self):

        localctx = GraphParser.WeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_weight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 57
                    self.match(GraphParser.NUMBER)

                else:
                    raise NoViableAltException(self)
                self.state = 60 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.NUMBER)
            else:
                return self.getToken(GraphParser.NUMBER, i)

        def getRuleIndex(self):
            return GraphParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)




    def source(self):

        localctx = GraphParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.match(GraphParser.NUMBER)
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GraphParser.NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestinationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GraphParser.NUMBER)
            else:
                return self.getToken(GraphParser.NUMBER, i)

        def getRuleIndex(self):
            return GraphParser.RULE_destination

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestination" ):
                listener.enterDestination(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestination" ):
                listener.exitDestination(self)




    def destination(self):

        localctx = GraphParser.DestinationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destination)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 67
                    self.match(GraphParser.NUMBER)

                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





