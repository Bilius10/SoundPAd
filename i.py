import flet as ft
from pygame import mixer
import time

mixer.init()


def inicial(page):

    page.title = "SoundPad"
    page.window_width = 300
    page.window_height = 550
    page.window_resizable = False

    def tocar(num):
        mixer.music.load(f'{num}.mp3')
        mixer.music.play()
        time.sleep(20)

    button_width = 125  # Ajuste a largura conforme necessário
    button_height = 40  # Ajuste a altura conforme necessário

    page.add(
        ft.Column(
            [
                ft.Row([ft.ElevatedButton(text="Pia cheia de louça", on_click=lambda e: tocar(1), width=button_width, height=button_height),
                        ft.ElevatedButton(text="E o pix", on_click=lambda e: tocar(2), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="English or spanish?", on_click=lambda e: tocar(3), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Tenteii", on_click=lambda e: tocar(4), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Apanhar e ficar calado", on_click=lambda e: tocar(5), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Vamo acordar", on_click=lambda e: tocar(6), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Confiança", on_click=lambda e: tocar(7), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Rizada", on_click=lambda e: tocar(8), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Banido", on_click=lambda e: tocar(9), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Boa noite", on_click=lambda e: tocar(10), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Bom dia", on_click=lambda e: tocar(11), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Cavalo", on_click=lambda e: tocar(12), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Para de mandar audio", on_click=lambda e: tocar(20), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Ele fez dnv", on_click=lambda e: tocar(14), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="Cade oce", on_click=lambda e: tocar(15), width=button_width, height=button_height),
                        ft.ElevatedButton(text="Moreno ta ignorante", on_click=lambda e: tocar(16), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="So quer mamão?", on_click=lambda e: tocar(17), width=button_width, height=button_height),
                        ft.ElevatedButton(text="turururu", on_click=lambda e: tocar(18), width=button_width, height=button_height)]),
                ft.Row([ft.ElevatedButton(text="tum", on_click=lambda e: tocar(21), width=button_width, height=button_height),
                        ft.ElevatedButton(text="vo nada", on_click=lambda e: tocar(22), width=button_width, height=button_height)])
            ]
        )
    )


ft.app(inicial)
