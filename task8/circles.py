import math
from typing import List, Set, Dict, Tuple, Union
from typing import Sequence, Iterator


def safe_radius_of(number: Union[int, float]) -> Union[int, float]:
    if not (
            isinstance(number, int) or
            isinstance(number, float)
    ):
        raise TypeError('Radius should be either "int" or "float" data type!')
    if number < 0:
        raise ValueError('Radius value should be more that "0"!')
    return number


def calculate_square_of(number: Union[int, float]) -> Union[int, float]:
    return number ** 2


def multiply_by_pi(number: Union[int, float]) -> Union[int, float]:
    return math.pi * number


def double_of(number: Union[int, float]) -> Union[int, float]:
    return number * 2


class Circle:
    def __init__(self, identifier: int, radius: Union[int, float], color: str) -> None:
        self.identifier = identifier
        self._radius = lambda: safe_radius_of(radius)
        self._color = color

    def change_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError('Color should be "str" data type!')
        self._color = color

    def diameter(self) -> Union[int, float]:
        return double_of(self._radius())

    def area(self) -> Union[int, float]:
        return multiply_by_pi(calculate_square_of(self._radius()))

    def perimeter(self) -> Union[int, float]:
        return double_of(multiply_by_pi(self._radius()))

    def __str__(self) -> str:
        return f'Circle(radius={self._radius()}, color="{self._color}")'


class Circles:
    def __init__(self, *circles: Circle) -> None:
        self._circles = circles

    def update_colors(self, new_colors: Dict[int, str]) -> None:
        for identifier, color in new_colors.items():
            this = self.find(identifier)
            this.change_color(color)
            print(this)

    def find(self, identifier: int) -> Circle:
        for this in self._circles:
            if this.identifier == identifier:
                return this

        raise ValueError(f"There is no circle with this identifier: {identifier}")

    def show_diameters(self) -> None:
        for circle in self._circles:
            print(f"A diameter of {circle} is {circle.diameter()}")

    def show_areas(self) -> None:
        for circle in self._circles:
            print(f"An area of {circle} is {circle.area()}")

    def show_perimeters(self) -> None:
        for circle in self._circles:
            print(f"A perimeter of {circle} is {circle.perimeter()}")


if __name__ == "__main__":
    circles = Circles(
        Circle(1, 1, 'red'),
        Circle(2, 0.2, 'super-red'),
        Circle(3, 3, 'green'),
        Circle(4, 5, 'super-green'),
    )
    circles.show_diameters()
    circles.show_areas()
    circles.show_perimeters()
    circles.update_colors({
        1: 'blue',
        2: 'red',
        3: 'black',
        4: 'purple'
    })