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

    x_expression_horizontal = x ** 2
    y_expression_horizontal = y ** 2 
    cercle = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((50, 26), (50, 74), cercle, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((50, 74), (50, 26), cercle, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((38, 26), (30, 26), cercle, cartesian_variables, BATTERY_VOLTAGE)
    ]
    ground_position = (38, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (50, 26), 1: (50, 74) }
    )
    
    world.compute()
    world.show_all()
