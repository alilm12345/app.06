import flet as ft
import random

#Funcion peincipal
def main(page: ft.Page):
    #Variables globales
    global numero_Secreto,entrada_numero,texto_resultado,bot
    
    page.title = "Adivina el numero"
    
    #Generar un numero aleatorio
    numero_Secreto = random.randing(1,100)
    
    #crear los elementos de la interfaz
    titulo=ft.Text("Adivina el numero secreto entre 1 y 100",size= 20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    heigh=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        )
        bgcolor="blue",
        width=page.window.width,
        heigh=page.widow.height,
        padding=20
        
        
    )

ft.app(main)
