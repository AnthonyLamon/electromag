import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, sqrt

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World, circuit_node


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1
    LOW_WIRE_RESISTANCE = 0.1

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_cercle = x
    y_expression_cercle = x**2/24
    cercle_inf = (x_expression_cercle, y_expression_cercle)

    x_expression_cercle = x
    y_expression_cercle =  -x**2/24
    cercle_sup = (x_expression_cercle, y_expression_cercle)
    
    x_expression_horizontal = x 
    y_expression_horizontal = y * 0  
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((38, 26), (62, 50), cercle_inf, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((38, 74), (62, 50), cercle_sup, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 26), (6, 50), cercle_inf, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 74), (6, 50), cercle_sup, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((30, 26), (38, 26), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((38, 74), (30, 74), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE)
    ]
    ground_position = (30, 26)

    circuit = Circuit(wires, ground_position)
    #world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    #world.show_circuit(
      #  {0: (38, 26), 1: (62, 50), 2: (30, 26), 3: (6, 50), 4: (30, 74), 5: (38, 74) }
    #)
    


    #world.compute()
    #world.show_all()
    print(circuit.has_voltage_sources)
    print(circuit.is_closed)
    print(circuit.nodes)
    #print(circuit._set_potentials())

    #l'erreur à l'air d etre ici "component.current*component.resistance" ligne 268 de circuit. Il n'y a pas l'air d'avoir de courant (NoneType)
