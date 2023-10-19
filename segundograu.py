from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import math

class EquacaoQuadratica(App):
    def build(self):
        self.title = "RESULTADO BASKARA"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        Window.clearcolor = (1, 1, 1, 1)

        input_layout_a = BoxLayout(orientation='horizontal', spacing=10)
        self.label_a = Label(text="Valor de a:", halign='left', size_hint=(None, None), size=(100, 40), color=(0, 0, 0, 1), font_size=17)
        self.input_a = TextInput(multiline=False, size_hint=(None, None), size=(60, 60))
        input_layout_a.add_widget(self.label_a)
        input_layout_a.add_widget(self.input_a)

        input_layout_b = BoxLayout(orientation='horizontal', spacing=10)
        self.label_b = Label(text="Valor de b:", halign='left', size_hint=(None, None), size=(100, 40), color=(0, 0, 0, 1), font_size=17)
        self.input_b = TextInput(multiline=False, size_hint=(None, None), size=(60, 60))
        input_layout_b.add_widget(self.label_b)
        input_layout_b.add_widget(self.input_b)

        input_layout_c = BoxLayout(orientation='horizontal', spacing=10)
        self.label_c = Label(text="Valor de c:", halign='left', size_hint=(None, None), size=(100, 40), color=(0, 0, 0, 1), font_size=17)
        self.input_c = TextInput(multiline=False, size_hint=(None, None), size=(60, 60))
        input_layout_c.add_widget(self.label_c)
        input_layout_c.add_widget(self.input_c)

        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        calculate_button = Button(text="Calcular", size_hint=(None, None), size=(200, 40))
        calculate_button.bind(on_press=self.calcular_equacao)
        clear_button = Button(text="Limpar", size_hint=(None, None), size=(200, 40))
        clear_button.bind(on_press=self.limpar_campos)

        self.result_label = Label(text="", size_hint=(None, None), size=(300, 100), color=(0, 0, 0, 1), font_size=19, halign='center', valign='middle')

        layout.add_widget(input_layout_a)
        layout.add_widget(input_layout_b)
        layout.add_widget(input_layout_c)
        button_layout.add_widget(calculate_button)
        button_layout.add_widget(clear_button)
        layout.add_widget(button_layout)
        layout.add_widget(self.result_label)

        return layout

    def calcular_equacao(self, instance):
        a = self.input_a.text.strip()
        b = self.input_b.text.strip()
        c = self.input_c.text.strip()

        if not a or not b or not c:
            self.result_label.text = "Por favor, insira algum número."
            return

        a = int(a)
        b = int(b)
        c = int(c)

        if a == 0:
            self.result_label.text = "A equação não é de segundo grau!"
            return

        delta = (b**2) - (4*a*c)

        if delta < 0:
            self.result_label.text = "A equação não tem soluções reais!"
        elif delta == 0:
            x1 = -b / (2*a)
            self.result_label.text = f'Delta = {delta}\n x1 = {x1}'
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            self.result_label.text = f'Delta = {delta}\n x1 = {x1}\n x2 = {x2}'

    def limpar_campos(self, instance):
        self.input_a.text = ""
        self.input_b.text = ""
        self.input_c.text = ""
        self.result_label.text = "resposta"

if __name__ == '__main__':
    EquacaoQuadratica().run()
