import models, algorithms

def apply_monte_carlo_2d(coords, func_str, points):
    current_zone = models.TwoDimensionalZone(coords)

    func = algorithms.create_2dfunc_from_str(func_str)

    result = algorithms.monte_carlo_2d(current_zone, points, func)

    result['x1'] = round(result['x1'], 6)
    result['x2'] = round(result['x2'], 6)
    result['func_val'] = round(result['func_val'], 6)
    return result

def get_data_from_vals(values):
    coords = {
                'x1_left': float(values['x1_left']),
                'x1_right': float(values['x1_right']),
                'x2_left': float(values['x2_left']),
                'x2_right': float(values['x2_right']),
            }
    points = int(values['points'])
    func_str = values['func']
    return coords, points, func_str