from nicegui import ui

#Funciones
def sumar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        suma = n1 + n2
        resultado.set_text(f'Resultado: {suma}')

def restar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        resta = n1 - n2
        resultado.set_text(f'Resultado: {resta}')

def multiplicar():
        n1 = float(num1.value)
        n2 = float(num2.value)
        multiplicacion = n1 * n2
        resultado.set_text(f'Resultado: {multiplicacion}')

def dividir():
        n1 = float(num1.value)
        n2 = float(num2.value)
        if n2 != 0:
            division = n1 / n2
            resultado.set_text(f'Resultado: {division}')
        else:
            resultado.set_text('Error: División por cero')


#Estructura de la interfaz de usuario
with ui.card().classes("w-60 m-auto p-4"):
    ui.label('Calculadora').classes ("font-sans") 
    with ui.column().classes("w-full items-center"):
        num1 = ui.input('Número 1').classes("w-full")
        num2 = ui.input('Número 2').classes("w-full")   
    with ui.row().classes("w-full gap-2 mt-4"):    
        bt_sumar = ui.button('Sumar').classes("bg-blue-500 text-white flex-1").on_click(sumar)
        bt_restar = ui.button('Restar').classes("bg-green-500 text-white flex-1").on_click(restar)
    with ui.row().classes("w-full gap-2 mt-2"):
        bt_multiplicar = ui.button('Multiplicar').classes("bg-yellow-500 text-white flex-1").on_click(multiplicar)
        bt_dividir = ui.button('Dividir').classes("bg-red-500 text-white flex-1").on_click(dividir)
    resultado = ui.label('Resultado: ').classes("font-sans mt-4")
ui.run()