import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, sqrt

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_cercle = x
    y_expression_cercle = (24 - sqrt(576-x**2)) 
    cercle_inf = (x_expression_cercle, y_expression_cercle)

    x_expression_cercle = x
    y_expression_cercle =  (sqrt(576-x**2)+24)
    cercle_sup = (x_expression_cercle, y_expression_cercle)
    
    x_expression_horizontal = x 
    y_expression_horizontal = y * 0  
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((38, 26), (62, 50), cercle_inf, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((62, 50), (38, 74), cercle_sup, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 26), (6, 50), cercle_inf, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((6, 50), (30, 74), cercle_sup, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((38, 26), (30, 26), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((38, 74), (30, 26), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE)
    ]
    ground_position = (38, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (38, 26), 1: (62, 50), 2: (30, 26), 3: (6, 50), 4: (30, 74), 5: (38, 74) }
    )
    
    world.compute()
    world.show_all()
