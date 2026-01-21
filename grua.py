from nicegui import ui

def accion(nombre):
    ui.notify(f'Botón presionado: {nombre}')

ui.label('Panel de Control').classes('text-2xl font-bold mb-4')

with ui.column().classes('items-center gap-4'):

    ui.button('⬆ Arriba', on_click=lambda: accion('Arriba'))

    with ui.row().classes('gap-4'):
        ui.button('⬅ Izquierda', on_click=lambda: accion('Izquierda'))
        ui.button('➡ Derecha', on_click=lambda: accion('Derecha'))

    ui.button('⬇ Abajo', on_click=lambda: accion('Abajo'))

    with ui.row().classes('gap-4 mt-4'):
        ui.button('Agarrar', color='green', on_click=lambda: accion('Agarrar'))
        ui.button('Soltar', color='red', on_click=lambda: accion('Soltar'))

ui.run(host='127.0.0.1',
    port=8080,
    reload=False,
    show=False)
