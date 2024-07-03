import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_statistiche(self, e):
        loc = self._view.dd_localizzazione.value
        if loc is None:
            self._view.create_alert("Selezionare una localizzazione")
            return
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a:{loc}"))
        analisi=self._model.getAnalisi(loc)
        for nodo,peso in analisi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo} - {peso}"))
        self._view.update_page()


    def handle_cammino(self, e):
        costo, listaNodi = self._model.getBestPath()
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore è costituita da {costo} attori"))
        for nodo in listaNodi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()
        #dizio = self._model.analisi(porzione)
    def creaGrafo(self):
        grafo = self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo:
            self._view.dd_localizzazione.options.append(ft.dropdown.Option(
                text=nodo))
        self._view.update_page()