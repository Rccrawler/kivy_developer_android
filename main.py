#pip install kivy
#Importa la clase App de la librería kivy.app
from kivy.app import App
#Importa la clase Button
from kivy.uix.button import Button

#Crea una clase MainApp que hereda de App
class MainApp(App):
    def build(self):
        return Button(text="Hello World!")
    
#Si el archivo es ejecutado directamente, se ejecuta la aplicación
if __name__ == "__main__":
    MainApp().run()