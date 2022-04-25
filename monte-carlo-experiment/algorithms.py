import random
from math import sin, cos, tan, exp, log, log10

def monte_carlo_2d(zone_2d, points, func_2d):
    values = []
    for i in range(points):
        x1_random = random.uniform(zone_2d.coords['x1_left'], zone_2d.coords['x1_right'])
        x2_random = random.uniform(zone_2d.coords['x2_left'], zone_2d.coords['x2_right'])
        values.append({
            'x1': x1_random,
            'x2': x2_random,
            'func_val': func_2d(x1_random, x2_random)
            })
    return min(values, key=lambda val: val['func_val'])

def create_2dfunc_from_str(expression):
    def func(x1, x2):
        str_with_values = expression.replace('^', '**')
        str_with_values = str_with_values.replace('x1', '(' + str(x1)+ ')')
        str_with_values = str_with_values.replace('x2', '(' + str(x2) + ')')
        return eval(str_with_values)
    return func
