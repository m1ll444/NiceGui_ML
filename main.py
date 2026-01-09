from nicegui import ui

#Funciones



#Estructura de la interfaz de usuario
with ui.card().classes("w-60 m-auto p-4"):
    ui.label('Hola, Mundo!').classes ("font-sans") 

ui.run()