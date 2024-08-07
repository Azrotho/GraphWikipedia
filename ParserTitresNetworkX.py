import xml.sax
import pickle
import networkx as nx

class PageHandler(xml.sax.ContentHandler):
    def __init__(self, graph):
        self.graph = graph
        self.current_tag = ""
        self.title = ""
        self.ns = ""
        self.page_count = 0

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "page":
            self.title = ""
            self.ns = ""

    def characters(self, content):
        if self.current_tag == "title":
            self.title += content
        elif self.current_tag == "ns":
            self.ns += content

    def endElement(self, tag):
        if tag == "page":
            if self.ns.strip() == "0":
                self.graph.add_node(self.title.strip())
                self.page_count += 1
                if self.page_count % 10000 == 0:
                    print(f"{self.page_count} pages ajoutées au graphe...")

if __name__ == "__main__":
    graph = nx.DiGraph()
    parser = xml.sax.make_parser()
    handler = PageHandler(graph)
    parser.setContentHandler(handler)
    parser.parse("frwiki-20240701-pages-articles.xml") 

    print("Sauvegarde du graphe avec les pages...")
    pickle.dump(graph, open('wikipedia.pickle', 'wb'))
    print(f"Graphe sauvegardé avec {graph.number_of_nodes()} nœuds.")