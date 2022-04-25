import PySimpleGUI as sg
import traceback

import ui
import matplotlib.pyplot as plt

layout = [ [sg.Text('Координаты области по x1: '), sg.Text('от'), sg.InputText(key='x1_left', default_text='-2'),
             sg.Text('до'), sg.InputText(key='x1_right', default_text='4')],
            [sg.Text('Координаты области по x2: '), sg.Text('от'), sg.InputText(key='x2_left', default_text='-2'),
             sg.Text('до'), sg.InputText(key='x2_right', default_text='4')],
            [sg.Text('Для функции '), sg.InputText(key='func', default_text='x1^2 + x2^2')],
            [sg.Text('Число точек '), sg.InputText(key='points', default_text='100')],
            [sg.Text('Результат:  '), sg.Text(key='result')],
            [sg.Button('Расчет'), sg.Button('Эксперимент'), sg.Button('Выход')]]

window = sg.Window(title="Метод Монте-Карло", layout=layout, margins=(100, 50))


try:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Выход':
            break
        elif event == 'Расчет':
            coords, points, func_str = ui.get_data_from_vals(values)
            result = ui.apply_monte_carlo_2d(coords, func_str, points)
            result_repr = f'x1={result["x1"]} x2={result["x2"]} f(x1,x2)={result["func_val"]}'
            window['result'].update(str(result_repr))
        elif event == 'Эксперимент':
            coords, points, func_str = ui.get_data_from_vals(values)
            precise_result = ui.apply_monte_carlo_2d(coords, func_str, 25000)['func_val']
            points = [
                25, 50, 100, 250, 500, 1000, 2500, 5000, 10000
            ]
            function_values = []
            for p in points:
                result = ui.apply_monte_carlo_2d(coords, func_str, p)
                function_values.append(result['func_val'])
            diffs = list(map(lambda x: abs(x - precise_result), function_values))
            fig, ax = plt.subplots()
            plt.plot(points, diffs, marker="." )
            # plt.xticks(points)
            # plt.yticks(diffs)
            plt.show()
            print(points, function_values, diffs)
    window.close()
except Exception as e:
    tb = traceback.format_exc()
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)

