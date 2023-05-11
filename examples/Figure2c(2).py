import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

import math

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y"), Symbol("r"), Symbol("M")
    x, y, r, M = cartesian_variables

    x_expression_sup = x
    y_expression_sup = float(math.sqrt(abs(r ** 2 -  (x - M )**2)))
    cercle_supérieur = (x_expression_sup, y_expression_sup)
    
    
    x_expression_inf = x
    y_expression_inf = -float(math.sqrt(abs(r ** 2 -  (x - M )**2)))
    cercle_inférieur = (x_expression_inf, y_expression_inf )

    wires = [
        VoltageSource((60, 50, 10, 50), (60, 50, 10, 50), cercle_inférieur, cartesian_variables, BATTERY_VOLTAGE)
    ]
    
    
    
    
    ground_position = (60, 50, 10, 50)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    world.compute()
    world.show_all()

