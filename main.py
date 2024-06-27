from wfc_lib import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_rule = Rule(
        "1",
        lambda x, y: {
            (x+1, y): ["2", "3"],
            (x, y + 1): ["2", "3"],
            (x, y - 1): ["2", "3"],
            (x - 1, y): ["2", "3"]
        }
    )

    second_rule = Rule(
        "2",
        lambda x, y: {
            (x + 1, y): ["1", "3"],
            (x, y + 1): ["1", "3"],
            (x, y - 1): ["1", "3"],
            (x - 1, y): ["1", "3"]
        }
    )

    third_rule = Rule(
        "3",
        lambda x, y: {
            (x + 1, y): ["1", "2"],
            (x, y + 1): ["1", "2"],
            (x, y - 1): ["1", "2"],
            (x - 1, y): ["1", "2"]
        }
    )

    grass = Rule(
        "grass",
        lambda x, y: {  # Rule uses a lambda
            (x, y + 1): ["air"],  # Which takes the x and y coordinate of the state
            (x, y - 1): ["dirt", "stone"]  # And returns what the states relative to it must be
        }
    )

    dirt = Rule(
        "dirt",
        lambda x, y: {
            (x, y + 1): ["dirt", "grass"],
            (x, y - 1): ["stone", "dirt"]
        }
    )

    stone = Rule(
        "stone",
        lambda x, y: {
            (x, y + 1): ["stone", "dirt"]
        }
    )

    air = Rule(
        "air",
        lambda x, y: {
            (x, y + 1): ["air"]
        }
    )

    rule_collection = RuleCollection(
        [
            grass,
            dirt,
            stone,
            air
        ]
    )

    wave = Wave(10, 10, rule_collection)

    print(first_rule.applies_to)
    print(second_rule.applies_to)
    print(rule_collection.members)
    print(wave.wave)

    wave.auto_run()

    print(wave.wave)

    matrix = [[None for _ in range(10)] for _ in range(10)]

    for (x, y), content in wave.wave.items():
        matrix[y][x] = list(content.keys())[0]

    [print(row) for row in matrix]
