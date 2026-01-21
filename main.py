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
    num1 = ui.input('Número 1').classes("w-full")
    num2 = ui.input('Número 2').classes("w-full")   
    bt_sumar = ui.button('Sumar').classes("w-full bg-blue-500 text-white").on_click(sumar)
    bt_restar = ui.button('Restar').classes("w-full bg-green-500 text-white mt-2").on_click(restar)
    bt_multiplicar = ui.button('Multiplicar').classes("w-full bg-yellow-500 text-white mt-2").on_click(multiplicar)
    bt_dividir = ui.button('Dividir').classes("w-full bg-red-500 text-white mt-2").on_click(dividir)
    resultado = ui.label('Resultado: ').classes("font-sans mt-4")
