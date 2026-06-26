import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno1 = None
        self.anno2 = None


    def handleCreaGrafo(self,e):
        if self.anno1 is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Scegliere un anno" , color="red")
            )
            self._view.update_page()
            return
        if self.anno2 is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Scegliere un anno" , color="red")
            )
            self._view.update_page()
            return
        self._model.buildGraph(self.anno1 , self.anno2)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text("Grafo correttamente creato" , color="green")
        )
        nodi , archi = self._model.getDettagliGrafo()
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {nodi} nodi")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {archi} archi")
        )
        self._view.update_page()


    def handleDettagli(self, e):
        treArchi , numCompConn , compConnMaggiore = self._model.getDettagliPunto3()
        self._view.txt_result.controls.append(
            ft.Text(f"Archi di peso maggiore:" , color="orange")
        )
        for arco in treArchi:
            self._view.txt_result.controls.append(
            ft.Text(f"{arco[0].surname} --> {arco[1].surname} ({arco[2]})")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {numCompConn} componenti connesse" , color="orange")
        )

        self._view.txt_result.controls.append(
            ft.Text(f"Componente più grande" , color="orange")
        )
        for nodi in compConnMaggiore:

            self._view.txt_result.controls.append(
            ft.Text(f"{nodi[0].surname} ({nodi[1]})")
        )

        self._view.update_page()


    def handleCerca(self, e):
        pass

    def fillDdAnni(self):
        anni = self._model.getAllAnni()
        for a in anni:
            self._view._ddAnno1.options.append(
                ft.dropdown.Option(data= a,
                                   key= a,
                                   on_click= self.scegliAnno1)
            )
            self._view._ddAnno2.options.append(
                ft.dropdown.Option(data= a,
                                   key= a,
                                   on_click=self.scegliAnno2)
            )

    def scegliAnno1(self , e):
        self.anno1 = e.control.data

    def scegliAnno2(self , e):
        self.anno2 = e.control.data

