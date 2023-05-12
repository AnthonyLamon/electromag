import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, cos, sin, pi

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        #Wire((26, 26), (26, 42), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((26, 58), (26, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((42, 26), (42, 42), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 26), (42, 74), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        #Wire((42, 58), (42, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((58, 26), (58, 42), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 26), (58, 74), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        #Wire((58, 58), (58, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((74, 26), (74, 42), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((74, 58), (74, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((26, 74), (42, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 74), (58, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 74), (74, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((26, 26), (42, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 26), (58, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 26), (74, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((26, 26), (26, 74), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        VoltageSource((74, 26), (74, 74), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE)
    ]
    ground_position = (26, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    #world.show_circuit(
        #{0: (26, 26), 1: (26, 42), 2: (26, 58), 3: (26, 74), 4: (42, 26), 5: (42, 42), 6: (42, 58), 7: (42, 74), 
         #8: (58, 26), 9: (58, 42), 10: (58, 58), 11: (58, 74), 12: (74, 26), 13: (74, 42), 14: (74, 58), 15: (74, 74)}
    #)
    world.show_circuit(
        {0: (26, 26), 1: (26, 74), 2: (74, 26), 3: (74, 74), 4: (42, 26), 5: (42, 74), 6: (58, 26), 7: (58, 74)}
    )


    
    world.compute()
    world.show_all()