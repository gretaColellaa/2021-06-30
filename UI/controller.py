import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_statistiche(self, e):
        localization = self._view.ddLocal.value

        stat = self._model.calcolaStatistiche(localization)
        self._view.txt_result.controls.append(ft.Text(f"Il nodo {localization} è connesso al :"))

        for s in stat:
            self._view.txt_result.controls.append(ft.Text(f"nodo {s[0]} con peso = {s[1]}"))

        self._view.update_page()

    def handle_cammino(self, e):
        localization = self._view.ddLocal.value

        path = self._model.cerca_cammino(localization)
        self._view.txt_result.controls.append(ft.Text(f"Il cammino più lungo dal nodo : {localization} è:"))

        for n in path[0]:
            self._view.txt_result.controls.append(ft.Text(f"{n}"))

        self._view.txt_result.controls.append(ft.Text(f"con peso: {path[1]}"))
        self._view.update_page()



    def start(self):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumNodes()} nodi"
                                                      f" e {self._model.getNumEdges()} archi"))


        for n in sorted(self._model._nodes):
            #print(n)
            self._view.ddLocal.options.append(ft.dropdown.Option(n))

        self._view.update_page()





