import PySimpleGUI as sg
import traceback
import models
import algorithms

layout = [ [sg.Text('Координаты области по x1: '), sg.Text('от'), sg.InputText(key='x1_left', default_text='-2'),
             sg.Text('до'), sg.InputText(key='x1_right', default_text='4')],
            [sg.Text('Координаты области по x2: '), sg.Text('от'), sg.InputText(key='x2_left', default_text='-2'),
             sg.Text('до'), sg.InputText(key='x2_right', default_text='4')],
            [sg.Text('Для функции '), sg.InputText(key='func', default_text='x1^2 + x2^2')],
            [sg.Text('Число точек '), sg.InputText(key='points', default_text='100')],
            [sg.Text('Результат:  '), sg.Text(key='result')],
            [sg.Button('Расчет'), sg.Button('Выход')]]

window = sg.Window(title="Метод Монте-Карло", layout=layout, margins=(100, 50))

try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход':
            break

        coords = {
            'x1_left': float(values['x1_left']),
            'x1_right': float(values['x1_right']),
            'x2_left': float(values['x2_left']),
            'x2_right': float(values['x2_right']),
        }
        points = int(values['points'])
        func_str = values['func']

        current_zone = models.TwoDimensionalZone(coords)

        func = algorithms.create_2dfunc_from_str(func_str)

        result = algorithms.monte_carlo_2d(current_zone, points, func)

        result['x1'] = round(result['x1'], 6)
        result['x2'] = round(result['x2'], 6)
        result['func_val'] = round(result['func_val'], 6)

        result_repr = f'x1={result["x1"]} x2={result["x2"]} f(x1,x2)={result["func_val"]}'
        window['result'].update(str(result_repr))
    window.close()
except Exception as e:
    tb = traceback.format_exc()
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)

