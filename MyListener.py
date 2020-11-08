from GraphLexer import GraphLexer
from GraphParser import GraphParser
from GraphListener import GraphListener
from antlr4 import FileStream, CommonTokenStream,ParseTreeWalker
import networkx as nx


class MyListiner(GraphListener):
    def __init__(self,graph):
        self.graph = graph

    def exitNode(self,ctx:GraphParser.NodeContext):
        self.graph.add_node(int(ctx.nodeindex().getText()),name=ctx.name().getText())

    def exitEdge(self,ctx:GraphParser.EdgeContext):
        self.graph.add_edge(int(ctx.source().getText()),int(ctx.destination().getText()),weight=int(ctx.weight().getText()))

def make_digraph_from_file(file):
        # print("Start making graph")
        # start = time.time()
        new_graph = nx.Graph()  
        input = FileStream(file)
        lexer = GraphLexer(input)
        stream = CommonTokenStream(lexer)
        parser = GraphParser(stream)
        tree = parser.graph()
        listiner = MyListiner(new_graph)
        walker = ParseTreeWalker()
        walker.walk(listiner,tree)
        # print(f"End making graph: {time.time()-start}")   
        return new_graph
