import xml.sax
import re
import networkx as nx
import pickle

class LinkHandler(xml.sax.ContentHandler):
    def __init__(self, graph):
        self.graph = graph
        self.current_tag = ""
        self.in_text_tag = False
        self.title = ""
        self.text = ""
        self.page_count = 0

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "text":
            self.in_text_tag = True
            self.text = ""
        elif tag == "title":
            self.title = ""

    def characters(self, content):
        if self.in_text_tag:
            self.text += content
        if self.current_tag == "title":
            self.title += content

    def endElement(self, tag):
        if tag == "text":
            self.in_text_tag = False
            self.page_count += 1
            if self.page_count % 10000 == 0:
                print(f"{self.page_count} pages traitées...")

            source = self.title.strip()
            if source in self.graph:  # Vérification si la page source existe
                links = re.findall(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]", self.text)
                for link in links:
                    target = link.strip()
                    if target in self.graph:  # Vérification si la page cible existe
                        self.graph.add_edge(source, target)

if __name__ == "__main__":
    graph = pickle.load(open('wikipedia.pickle', 'rb'))
    print("Graphe chargé avec succès.")
    parser = xml.sax.make_parser()
    handler = LinkHandler(graph)
    parser.setContentHandler(handler)
    parser.parse("frwiki-20240701-pages-articles.xml")  

    print("Sauvegarde du graphe complet...")
    nx.write_gexf(graph, "wikipedia.gexf")
    print(f"Graphe sauvegardé avec {graph.number_of_nodes()} nœuds et {graph.number_of_edges()} arêtes.")