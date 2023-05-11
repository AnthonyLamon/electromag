import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, sqrt 

import numpy as np

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World, circuit_node, electrical_components

from src.electrical_components import CurrentSource

if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.1

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_cercle = x
    y_expression_cercle = (x**2)/24
    cercle_inf = (x_expression_cercle, y_expression_cercle)

    x_expression_cercle = x
    y_expression_cercle = (-x**2)/24
    cercle_sup = (x_expression_cercle, y_expression_cercle)
    
    x_expression_horizontal = x 
    y_expression_horizontal = y * 0  
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((38, 26), (62, 50), cercle_inf, cartesian_variables, 0.01),
        Wire((38, 74), (62, 50), cercle_sup, cartesian_variables, 0.01),
        Wire((30, 26), (6, 50), cercle_inf, cartesian_variables, 0.01),
        Wire((30, 74), (6, 50), cercle_sup, cartesian_variables, 0.01),
        VoltageSource((30, 26), (38, 26), horizontal_eqs, cartesian_variables, 1.0),
        Wire((38, 74), (30, 74), horizontal_eqs, cartesian_variables, 1.00)
    ]
    ground_position = (30, 26)   
    circuit = Circuit(wires, ground_position)
    circuit._set_potentials()
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
    {0: (38, 26), 1: (62, 50), 2: (30, 26), 3: (6, 50), 4: (30, 74), 5: (38, 74) }
    )
    
    
    world.compute()
    world.show_all()
    #print(circuit.has_voltage_sources)
    #print(circuit.is_closed)
    #print(circuit.nodes)
    #print(circuit._set_potentials())

    #l'erreur à l'air d etre ici "component.current*component.resistance" ligne 268 de circuit. Il n'y a pas l'air d'avoir de courant (NoneType)
    #print(circuit._get_voltage_sources())
    #print(circuit._get_current_sources(wires))
    #print(circuit._get_node_current_constraints())
    #print(circuit._get_loop_voltage_constraints())
    #print(circuit._get_current_source_constraints())
    #print(circuit._get_constraints())
    #print(circuit._set_currents())
    #print(circuit3.current)
    #print(circuit4.current)
    #print(circuit5.current)
    #print(circuit6.current)
    #print(circuit8.current)
    circuit7 = electrical_components((38, 26), (62, 50), cercle_inf, cartesian_variables,Wire)
    circuit2 = CurrentSource((38, 26), (62, 50), cercle_inf, cartesian_variables,0)
    circuit3 = CurrentSource((38, 74), (62, 50), cercle_sup, cartesian_variables,0)
    circuit4 = CurrentSource((30, 26), (6, 50), cercle_inf, cartesian_variables,0)
    circuit5 = CurrentSource((30, 74), (6, 50), cercle_sup, cartesian_variables,0)
    circuit6 = CurrentSource((30, 26), (38, 26), horizontal_eqs, cartesian_variables,0)
    circuit8 = CurrentSource((38, 74), (30, 74), horizontal_eqs, cartesian_variables,0)
    