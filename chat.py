from nicegui import ui

#Variables globales
mensajes = []

def enviar(nickname, text):
    name = nickname.value
    msg = text.value
    if nickname.value and text.value:
        mensajes.append((name, msg))
        text.value = ''
        chat_box.refresh()
    else:
        ui.notify('Por favor, ingresa un apodo y un mensaje.', type='warning')

@ui.refreshable
def chat_box():
    with ui.column().classes('w-full border p-4 rounded bg-gray-100 h-80 overflow-y-auto'):
        for name, msg in mensajes:
            with ui.row().classes('items-center'):
                ui.label(f'{name}:').classes('font-bold text-blue-600')
                ui.label(msg).classes('ml-2')

@ui.page('/')
def index():
    ui.query('body').classes('bg-gray-200 flex items-center justify-center h-screen')
    with ui.card().classes('w-96 p-4'):
        ui.label('Chat grupal').classes('text-2xl font-bold mb-4 text-center')
        chat_box()
        with ui.row().classes('mt-4'):
            user_input = ui.input(placeholder='Apodo').classes('flex-1 mr-2')
            msg_input = ui.input(placeholder='Mensaje').classes('flex-2 mr-2')
            ui.button(icon='send',on_click=lambda: enviar(user_input, msg_input))

ui.run(host='0.0.0.0', port=8080, reload=False)