import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._localization = {}
        self._nodes = []
        self._edges = []
        self._interactions = []
        self._idMapInteractionType = {}
        pass


    def creaGrafo(self):
        self._nodes = DAO.getNodi()
        print(len(self._nodes))
        self._grafo.add_nodes_from(self._nodes)



        for l in DAO.getLoc(): # per ogni loc, metto nel dizionario { geneid : local}
            self._localization[l[0]] = l[1]

        self._interactions = DAO.getInteractions()
        for i in self._interactions:
            local1 = self._localization[i[0]]
            local2 = self._localization[i[1]]

            if local1 != local2 and local1 in self._nodes and local2 in self._nodes: # se hanno localizations diverse
                if (local1,local2) in self._idMapInteractionType.keys() : #dizionario tra duo localizations
                    if i[2] not in self._idMapInteractionType[local1,local2]:
                        self._idMapInteractionType[local1,local2].append(i[2]) #aggiungo il tipo alla lista di tipi
                elif  (local2,local1) in self._idMapInteractionType.keys():
                    if i[2] not in self._idMapInteractionType[local2,local1]:
                        self._idMapInteractionType[local2,local1].append(i[2]) #aggiungo il tipo alla lista di tipi

                else:
                    #print((local1, local2))
                    self._idMapInteractionType[local1,local2] = [i[2]] #creo la lista con il primo tipo


        for l1,l2 in self._idMapInteractionType.keys():
            self._edges.append((l1,l2, {"weight": len(self._idMapInteractionType[l1,l2])}))

        self._grafo.add_edges_from(self._edges)

    def getNumNodes(self):
        return len(self._nodes)

    def getNumEdges(self):
        return len(self._edges)


    def calcolaStatistiche(self, l):

        archi = self._grafo.edges(l, data=True)
        stat = []
        for a in archi:
            u,v,w = a[0],a[1],a[2]["weight"]
            if l == u:
                stat.append((v,w))
            elif l == v:
                stat.append((u,w))

        return stat

    def cerca_cammino(self, partenza):
        self._best_cammino = []
        self._best_peso = 0
        self._ricorsione([partenza], 0, {partenza})
        return self._best_cammino, self._best_peso

    def _ricorsione(self, cammino_parziale, peso_parziale, visited):
        ultimo = cammino_parziale[-1]

        # Caso finale: aggiorna se questo cammino è migliore
        if peso_parziale > self._best_peso:
            self._best_peso = peso_parziale
            self._best_cammino = list(cammino_parziale)

        for vicino in self._grafo.neighbors(ultimo):
            if vicino not in visited:
                peso = self._grafo[ultimo][vicino]['weight']

                visited.add(vicino)
                cammino_parziale.append(vicino)

                self._ricorsione(cammino_parziale, peso_parziale + peso, visited)

                # Backtrack
                visited.remove(vicino)
                cammino_parziale.pop()






