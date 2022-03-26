from botoes import ImageButton, LabelButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
import requests
from kivy.app import App
from functools import partial


class BannerVendedor(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas:
            Color(rgb=(0, 0, 0, 1))
            self.rec = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.atualizar_rec, size=self.atualizar_rec)

        id_vendedor = kwargs["id_vendedor"]

        link = f'https://aplicativovendas-6d2e9-default-rtdb.firebaseio.com/.json?orderBy="id_vendedor"&equalTo="{id_vendedor}"'
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        valor = list(requisicao_dic.values())[0]
        print(valor)
        avatar = valor["avatar"]
        total_vendas = valor["total_vendas"]

        meu_aplicativo = App.get_running_app()

        imagem = ImageButton(source=f"icones/fotos_perfil/{avatar}",
                            pos_hint={"right":0.4, "top": 0.9}, size_hint=(0.3, 0.8),
                            on_release=partial(meu_aplicativo.carregar_vendas_vendedor, valor))
        label_id = LabelButton(text=f"ID Vendedor: {id_vendedor}",
                            pos_hint={"right":0.9, "top": 0.9}, size_hint=(0.5, 0.5),
                            on_release=partial(meu_aplicativo.carregar_vendas_vendedor, valor))
        label_total = LabelButton(text=f"Total de Vendas: R${total_vendas}",
                            pos_hint={"right":0.9, "top": 0.6}, size_hint=(0.5, 0.5),
                            on_release=partial(meu_aplicativo.carregar_vendas_vendedor, valor))

        self.add_widget(imagem)
        self.add_widget(label_id)
        self.add_widget(label_total)

    def atualizar_rec(self, *args):
        self.rec.pos = self.pos
        self.rec.size = self.size