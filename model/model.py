import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMapDriver = {}

    def getAllAnni(self):
        return DAO.getAllYears()

    def buildGraph(self , anno1 , anno2):
        nodes = DAO.getAllNodes(anno1, anno2)
        self.grafo.add_nodes_from(nodes)

        for n in nodes:
            self.idMapDriver[n.driverId] = n

        self.grafo.clear_edges()
        edges = DAO.getAllEdges(anno1 , anno2)

        for e in edges:
            if e[0] in self.idMapDriver and e[1] in self.idMapDriver:
                u = self.idMapDriver[e[0]]
                v = self.idMapDriver[e[1]]
                peso = e[2]
                self.grafo.add_edge(u , v , weight= peso)

    def getDettagliGrafo(self):
        return self.grafo.number_of_nodes() , self.grafo.number_of_edges()

    def getDettagliPunto3(self):
        listaArchi = []
        for u , v , peso in self.grafo.edges(data=True):
                listaArchi.append((u , v , peso.get("weight" , 0)))
        listaArchi.sort(key=lambda x: x[2] , reverse=True)

        numCompConn = nx.number_connected_components(self.grafo)

        compConn = list(nx.connected_components(self.grafo))
        compConnMaggiore = max(compConn , key=len)

        nodiConGrado = []
        for nodo in compConnMaggiore:
            grado = self.grafo.degree(nodo)
            nodiConGrado.append((nodo , grado))
        nodiConGrado.sort(key=lambda x: x[1] , reverse=True)

        return listaArchi[:3] , numCompConn , nodiConGrado


