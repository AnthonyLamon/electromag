import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_cercle = x ** 2
    y_expression_cercle = y ** 2 
    cercle = (x_expression_cercle, y_expression_cercle)
    
    x_expression_horizontal = x 
    y_expression_horizontal = y * 0  
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((38, 26), (38, 74), cercle, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 74), (30, 26), cercle, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((38, 26), (30, 26), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((38, 74), (30, 26), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE)
    ]
    ground_position = (38, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (50, 26), 1: (50, 74) }
    )
    
    world.compute()
    world.show_all()
