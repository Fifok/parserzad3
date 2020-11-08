# Generated from .\Graph.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):

    # Enter a parse tree produced by GraphParser#graph.
    def enterGraph(self, ctx:GraphParser.GraphContext):
        pass

    # Exit a parse tree produced by GraphParser#graph.
    def exitGraph(self, ctx:GraphParser.GraphContext):
        pass


    # Enter a parse tree produced by GraphParser#typegraph.
    def enterTypegraph(self, ctx:GraphParser.TypegraphContext):
        pass

    # Exit a parse tree produced by GraphParser#typegraph.
    def exitTypegraph(self, ctx:GraphParser.TypegraphContext):
        pass


    # Enter a parse tree produced by GraphParser#namegraph.
    def enterNamegraph(self, ctx:GraphParser.NamegraphContext):
        pass

    # Exit a parse tree produced by GraphParser#namegraph.
    def exitNamegraph(self, ctx:GraphParser.NamegraphContext):
        pass


    # Enter a parse tree produced by GraphParser#nodeindex.
    def enterNodeindex(self, ctx:GraphParser.NodeindexContext):
        pass

    # Exit a parse tree produced by GraphParser#nodeindex.
    def exitNodeindex(self, ctx:GraphParser.NodeindexContext):
        pass


    # Enter a parse tree produced by GraphParser#node.
    def enterNode(self, ctx:GraphParser.NodeContext):
        pass

    # Exit a parse tree produced by GraphParser#node.
    def exitNode(self, ctx:GraphParser.NodeContext):
        pass


    # Enter a parse tree produced by GraphParser#name.
    def enterName(self, ctx:GraphParser.NameContext):
        pass

    # Exit a parse tree produced by GraphParser#name.
    def exitName(self, ctx:GraphParser.NameContext):
        pass


    # Enter a parse tree produced by GraphParser#edge.
    def enterEdge(self, ctx:GraphParser.EdgeContext):
        pass

    # Exit a parse tree produced by GraphParser#edge.
    def exitEdge(self, ctx:GraphParser.EdgeContext):
        pass


    # Enter a parse tree produced by GraphParser#weight.
    def enterWeight(self, ctx:GraphParser.WeightContext):
        pass

    # Exit a parse tree produced by GraphParser#weight.
    def exitWeight(self, ctx:GraphParser.WeightContext):
        pass


    # Enter a parse tree produced by GraphParser#source.
    def enterSource(self, ctx:GraphParser.SourceContext):
        pass

    # Exit a parse tree produced by GraphParser#source.
    def exitSource(self, ctx:GraphParser.SourceContext):
        pass


    # Enter a parse tree produced by GraphParser#destination.
    def enterDestination(self, ctx:GraphParser.DestinationContext):
        pass

    # Exit a parse tree produced by GraphParser#destination.
    def exitDestination(self, ctx:GraphParser.DestinationContext):
        pass



del GraphParser