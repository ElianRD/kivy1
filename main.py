from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import threading



class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.start_button = Button(text='Iniciar Servidor')
        self.start_button.bind(on_press=self.start_server)
        layout.add_widget(self.start_button)
        return layout

    def start_server(self, instance):
        def run_server():
            os.system('python app.py')  # Ejecuta el servidor Flask en un subproceso

        server_thread = threading.Thread(target=run_server)
        server_thread.start()


if __name__ == '__main__':
    MyApp().run()
