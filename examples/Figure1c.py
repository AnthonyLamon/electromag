from examples import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

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
        VoltageSource((52, 26), (48, 26), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((52, 26), (54, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((54, 26), (54, 26.4), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((54, 26.4),(56, 26.4), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((56, 26.4), (56, 26.9), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((56, 26.9),(58, 26.9), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 26.9), (58, 27.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 27.7),(60, 27.7), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 27.7), (60, 28.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 28.7),(62, 28.7), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((62, 28.7), (62, 30), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((62, 30),(64, 30), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((64, 30), (64, 31.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((64, 31.7),(66, 31.7), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((66, 31.7),(66, 34), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((66, 34),(68, 34), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((68, 34),(68, 37.2), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((68, 37.2),(70, 37.2), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 37.2),(70, 54.8), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((70, 54.8),(68, 54.8), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((68, 54.8),(68, 58), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((68, 58),(66, 58), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((66, 58),(66, 60.2), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((66, 60.2),(64, 60.2), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((64, 60.2),(64, 62), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((64, 62),(62, 62), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((62, 62),(62, 63.3), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((62, 63.3),(60, 63.3), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 63.3),(60, 64.3), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 64.3),(58, 64.3), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 64.3),(58, 65.1), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 65.1),(56, 65.1), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((56, 65.1),(56, 65.6), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((56, 65.6),(54, 65.6), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((54, 65.6),(54, 66), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((54, 66),(46, 66), horizontal_eqs, cartesian_variables,HIGH_WIRE_RESISTANCE),
        Wire((46, 66),(46, 65.6), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((46, 65.6),(44, 65.6), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((44, 65.6),(44, 65.1), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((44, 65.1),(42, 65.1), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((42, 65.1),(42, 64.3), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 64.3),(40, 64.3), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((40, 64.3),(40, 63.3), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 63.3),(38, 63.3), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((38, 63.3),(38, 62), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((38, 62),(36, 62), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((36, 62),(36, 60.3), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((36, 60.3),(34, 60.3), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((34, 60.3),(34, 58), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((34, 58),(32, 58), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((32, 58),(32, 54.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((32, 54.7),(30, 54.7), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((30, 54.7),(30, 37.2), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 37.2),(32, 37.2), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((32, 37.2),(32, 34), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((32, 34),(34, 34), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((34, 34),(34, 31.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((34, 31.7),(36, 31.7), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((36, 31.7),(36, 30), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((36, 30),(38, 30), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((38, 30),(38, 28.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((38, 28.7),(40, 28.7), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((40, 28.7),(40, 26.7), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 26.7),(42, 26.7), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((42, 26.7),(42, 26.9), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 26.9),(44, 26.9), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
        Wire((44, 26.9),(44, 26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((44, 26),(48, 26), horizontal_eqs, cartesian_variables,LOW_WIRE_RESISTANCE),
    ]
    
    
    
    ground_position = (52, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    
    world.compute()
    world.show_all()

