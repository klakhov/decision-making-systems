from abc import ABC

class NDimensionalZone(ABC):
    dimensions = None
    def __init__(self, coords) -> None:
        self._coords = [None] * self.dimensions * 2
        self.coords = coords

    @property
    def coords(self):
        coords = {}
        for i in range(self.dimensions):
            coords[f'x{i+1}_left'] = self._coords[i*2]
            coords[f'x{i+1}_right'] = self._coords[i*2 + 1]
        return coords

    @coords.setter
    def coords(self, new_coords):
        if type(new_coords) is dict:
            for i in range(self.dimensions):
                self._coords[i*2] = new_coords[f'x{i+1}_left']
                self._coords[i*2 + 1] = new_coords[f'x{i+1}_right']
        elif type(new_coords) is list:
            self.raw_coords = new_coords

    @property
    def raw_coords(self):
        return self._coords

    @raw_coords.setter
    def raw_coords(self, new_raw_coords):
        if len(new_raw_coords) != self.dimensions * 2:
            raise ValueError
        self._coords = new_raw_coords

    def __str__(self):
        res = ''
        for key in self.coords:
            res += f'{key}: {self.coords[key]}, '
        return '{' + res[:-2] + '}'

class TwoDimensionalZone(NDimensionalZone):
    dimensions = 2
    def __init__(self, coords) -> None:
        super().__init__(coords)
