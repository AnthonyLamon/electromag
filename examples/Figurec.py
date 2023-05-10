import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, cos, sin

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    WIRE_RESISTANCE = 1.0
    CIRCLE_RADIUS = 30

    polar_variables = Symbol("r"), Symbol("theta")
    r, theta = polar_variables

    x_expression = r * cos(theta)
    y_expression = r * sin(theta)
    equations = (x_expression, y_expression)

    wires = [
        Wire((50, 26), (50, 76), equations, polar_variables, WIRE_RESISTANCE),
        Wire((CIRCLE_RADIUS, 0), (CIRCLE_RADIUS, 2 * CIRCLE_RADIUS), equations, polar_variables, WIRE_RESISTANCE),
        Wire((CIRCLE_RADIUS, 2 * CIRCLE_RADIUS), (10, 2 * CIRCLE_RADIUS), equations, polar_variables, WIRE_RESISTANCE),
        Wire((10, 2 * CIRCLE_RADIUS), (10, 0), equations, polar_variables, WIRE_RESISTANCE),
        VoltageSource((0, 0), (CIRCLE_RADIUS, 0), equations, polar_variables, BATTERY_VOLTAGE)
    ]
    ground_position = (0, 0)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (10, 0), 1: (CIRCLE_RADIUS, 0), 2: (CIRCLE_RADIUS, 2 * CIRCLE_RADIUS), 3: (10, 2 * CIRCLE_RADIUS)}
    )

    world.compute()
    world.show_all()
