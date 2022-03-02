from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *




# file onde contém a parte visual da página
GUI = Builder.load_file("main.kv")

# parte lógica do programa - padrão para iniciar o app
class MainApp(App):

    def build(self):
        return GUI


    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela




MainApp().run()



