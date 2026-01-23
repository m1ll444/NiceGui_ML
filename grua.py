from nicegui import ui

# Función para las acciones (puedes conectar esto a tu lógica real)
def accion(nombre):
    ui.notify(f'Ejecutando: {nombre}', type='info')

# Estilo de la página
ui.query('body').style('background-color: #1a1a1a; color: white;')

with ui.column().classes('w-full items-center h-screen justify-center gap-6'):
    
    # 1. LA PANTALLA GRANDE
    with ui.card().classes('w-96 h-48 bg-slate-800 border-2 border-blue-500 shadow-lg flex items-center justify-center'):
        ui.label('SISTEMA DE GRÚA ACTIVO').classes('text-blue-400 text-2xl font-mono animate-pulse')
        ui.label('Esperando comando...').classes('text-slate-400 text-xs')

    # 2. PANEL DE BOTONES (Organizados estéticamente)
    with ui.card().classes('p-6 bg-slate-900 border border-slate-700 shadow-2xl'):
        ui.label('MANDO DE DIRECCIÓN').classes('text-center w-full mb-4 text-slate-500 font-bold')
        
        # Grid para las flechas
        with ui.grid(columns=3).classes('gap-4 items-center justify-items-center'):
            ui.label('') # Espacio vacío
            ui.button(icon='arrow_upward', on_click=lambda: accion('Arriba')).props('elevated round color=blue')
            ui.label('') # Espacio vacío
            
            ui.button(icon='arrow_back', on_click=lambda: accion('Izquierda')).props('elevated round color=blue')
            ui.button(icon='stop', on_click=lambda: accion('Detener')).props('elevated round color=red')
            ui.button(icon='arrow_forward', on_click=lambda: accion('Derecha')).props('elevated round color=blue')
            
            ui.label('') # Espacio vacío
            ui.button(icon='arrow_downward', on_click=lambda: accion('Abajo')).props('elevated round color=blue')
            ui.label('') # Espacio vacío

        ui.separator().classes('my-4 bg-slate-700')

        # Botones de acción (Pinza)
        with ui.row().classes('w-full justify-between gap-4'):
            ui.button('AGARRAR', icon='back_hand', on_click=lambda: accion('Agarrar')).props('color=green').classes('w-40')
            ui.button('SOLTAR', icon='front_hand', on_click=lambda: accion('Soltar')).props('color=orange').classes('w-40')

# Ejecución
ui.run(title='Mando de Grúa', port=8080, reload=False, show=True)