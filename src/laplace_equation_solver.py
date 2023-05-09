import numpy as np

from src.coordinate_and_position import CoordinateSystem
from src.fields import ScalarField


class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 1000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters1
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def _solve_in_cartesian_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_x: float,
            delta_y: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the electrical components' voltage at a
            given point (x, y) in space.
        delta_x : float
            Small discretization of the x-axis.
        delta_y : float
            Small discretization of the y-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(x, y) = 0 if (x, y) is not a point belonging to an electrical component of the circuit.
        """
        num_rows, num_cols = constant_voltage.shape

        # Initialisé le potentiel array with zeros
        potentiel = np.copy(constant_voltage)

        #  relaxation iterations
        
        for _ in range(self.nb_iterations):
            potentiel[1:num_rows-1, 1:num_cols-1] = (
            (potentiel[2:, 1:num_cols-1] + potentiel[:num_rows-2, 1:num_cols-1]) * delta_y**2 +
            (potentiel[1:num_rows-1, 2:] + potentiel[1:num_rows-1, :num_cols-2]) * delta_x**2
            ) / (2 * (delta_x**2 + delta_y**2))
            #for i in range(1, num_rows - 1):
                #for j in range(1, num_cols - 1):
                # relaxation equation
                    #potentiel[i,j] = ((potentiel[i+int(delta_x),j]+ potentiel[i-int(delta_x),j]) * (delta_y)**2 +
                    #(potentiel[i,j+int(delta_y)]+ potentiel[i,j-int(delta_y)]) * (delta_x)**2)/(2 * ((delta_x**2)+(delta_y**2)))
            np.copyto(potentiel, constant_voltage, where=constant_voltage !=0)
        return ScalarField(potentiel)
        #raise NotImplementedError

    def _solve_in_polar_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_r: float,
            delta_theta: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (r, θ) → V(r, θ), where V(r, θ) is the electrical components' voltage at a
            given point (r, θ) in space.
        delta_r : float
            Small discretization of the r-axis.
        delta_theta : float
            Small discretization of the θ-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (r, θ) → P(r, θ), where P(r, θ) is the electric potential at a given point
            (r, θ) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(r, θ) = 0 if (r, θ) is not a point belonging to an electrical component of the circuit.
        """
        num_rows, num_cols = constant_voltage.shape

        # Initialisé le potentiel array with zeros
        pot = np.copy(constant_voltage)

        #  relaxation iterations
        
        for _ in range(self.nb_iterations):
            for i in range(1, num_rows - 1):
                for j in range(1, num_cols - 1):
                    r = np.sqrt((i)**(2) + (j)**2)
                    th = np.arctan(j/i)
                # relaxation equation
                    pot[i, j] = (((delta_theta)**(2)*r**(2)*(pot[r+delta_r,th]+pot[r-delta_r,th])+
                    r*delta_r*delta_theta**(2)*(pot(r+delta_r,th))
                    +delta_r**(2)*(pot[r,th+delta_theta]+pot[r,th-delta_theta]))/(2*r**(2)*delta_theta**(2)+
                     r*delta_r*delta_theta**(2)+ 2*delta_r**(2)))
        return pot
        #raise NotImplementedError

    def solve(
            self,
            constant_voltage: ScalarField,
            coordinate_system: CoordinateSystem,
            delta_q1: float,
            delta_q2: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ representing a constant voltage field.
        coordinate_system : CoordinateSystem
            Coordinate system.
        delta_q1 : float
            Small discretization of the first axis.
        delta_q2 : float
            Small discretization of the second axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ  representing the potential in the 2D world.
        """
        if coordinate_system == CoordinateSystem.CARTESIAN:
            return self._solve_in_cartesian_coordinate(constant_voltage, delta_q1, delta_q2)
        elif coordinate_system == CoordinateSystem.POLAR:
            return self._solve_in_polar_coordinate(constant_voltage, delta_q1, delta_q2)
        else:
            raise NotImplementedError("Only the cartesian and polar coordinates system are implemented.")
