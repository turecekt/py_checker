"""Main file for our project."""
import triangle as tr


def input_values(point_name):  # pragma: no cover
    """
    User input method. Split user input into list.

    :param point_name: name of the point (char)
    :return: True, user input (list[int, int]) -> (tuple) | False
    """
    point = str_list_to_int(
        input(f"Zadejte souřadnice bodu {point_name}: ").split(","))
    if point:
        return point
    else:
        print("Zadejte souřadnice ve správném formátu! například: 1,1")
        return input_values(point_name)


def str_list_to_int(list_to_convert):
    """
    Check if user input is in the right format.

    :param list_to_convert: user input converted to list (list[str])
    :return: True & User input converted to (int) -> (tuple) | False
    """
    try:
        return True, (int(list_to_convert[0]), int(list_to_convert[1]))
    except ValueError or NameError:
        return False


if __name__ == '__main__':  # pragma no cover
    print("Souřadnice zadávejte ve formátu: x,y\nNapříklad: 1,1")
    triangle = tr.Triangle(input_values(point_name="A")[1],
                           input_values(point_name="B")[1],
                           input_values(point_name="C")[1])
    if triangle.is_able():
        print("Trojuholník je zostrojiteľný")
        print(
            f"Strana a: {round(triangle.a, 2)}\n"
            f"Strana b: {round(triangle.b, 2)}\n"
            f"Strana c: {round(triangle.c, 2)}"
        )
        print(f"Obvod trojúhelníku je: {round(triangle.perimeter(), 2)}")
        print(f"Obsah trojúhelníku je: {round(triangle.area(), 2)}")
        print(
            "Je pravouhlý" if triangle.is_rectangular() else "Není pravouhlý")
    else:
        print("Trojuholník nie je zostrojiteľný")
