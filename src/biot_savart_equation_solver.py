import numpy as np
from scipy.constants import mu_0, pi

from src.coordinate_and_position import CoordinateSystem
from src.fields import VectorField


class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def _solve_in_cartesian_coordinate(
            self,
            electric_current: VectorField,
            delta_x: float,
            delta_y: float
    ) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.
        delta_x : float
            Small discretization of the x-axis.
        delta_y : float
            Small discretization of the y-axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world.
        """
        pos = []
        current = []
        #On fait une matrice où on met 0 de champ sur les fils car pas de champs à ces endroits
        magnetic_field = np.zeros((np.shape(electric_current)[0], np.shape(electric_current)[1], 3))
        #On va ajouter les endroits où il y a du courant et leur valeur dans les listes
        for ligne, valeur in enumerate(electric_current):
            for colonne, position in enumerate(valeur):
                #Y'a t'il un courant?
                if position[0] or position[1] !=0:
                    #Si oui on l'ajoute
                    pos.append((ligne, colonne, 0))
                    current.append(position)
        
        
        for ligne, valeur in enumerate(magnetic_field):
            for colonne, position in enumerate(valeur):
                #On regarde uniquement les valeurs à l'extérieur du circuit
                if (ligne, colonne, 0) not in pos:
                    #On crée le vecteur r
                    r = np.array([ligne, colonne, 0] - np.array(pos))
                    #On trouve sa norme
                    r_norm = (np.linalg.norm(r, axis=1))
                    #On fait le produit vectoriel entre le courant (dl) et le vecteur r
                    cross_product = np.cross(current, r)
                    #On trouve le champ magnétique en z 
                    magnetic_field[ligne, colonne] = [int(0), int(0), np.sum(mu_0*cross_product[:, 2]/ (4* pi * r_norm) ** 3)]
                    
        return VectorField(magnetic_field)
            

    def _solve_in_polar_coordinate(
            self,
            electric_current: VectorField,
            delta_r: float,
            delta_theta: float
    ) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (r, θ) → (I_r(r, θ), I_θ(r, θ), I_z(r, θ)), where I_r(r, θ), I_θ(r, θ) and
            I_z(r, θ) are the 3 components of the electric current vector at a given point (r, θ) in space. Note that
            I_z = 0 is always True in our 2D world.
        delta_r : float
            Small discretization of the r-axis.
        delta_theta : float
            Small discretization of the θ-axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (r, θ) → (B_r(r, θ), B_θ(r, θ), B_z(r, θ)), where B_r(r, θ), B_θ(r, θ) and
            B_z(r, θ) are the 3 components of the magnetic vector at a given point (r, θ) in space. Note that
            B_r = B_θ = 0 is always True in our 2D world.
        """
        
            
        raise NotImplementedError
        

    def solve(
            self,
            electric_current: VectorField,
            coordinate_system: CoordinateSystem,
            delta_q1: float,
            delta_q2: float
    ) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ representing currents in the 2D world.
        coordinate_system : CoordinateSystem
            Coordinate system.
        delta_q1 : float
            Small discretization of the first axis.
        delta_q2 : float
            Small discretization of the second axis.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ representing the magnetic field in the 2D world.
        """
        if coordinate_system == CoordinateSystem.CARTESIAN:
            return self._solve_in_cartesian_coordinate(electric_current, delta_q1, delta_q2)
        elif coordinate_system == CoordinateSystem.POLAR:
            return self._solve_in_polar_coordinate(electric_current, delta_q1, delta_q2)
        else:
            raise NotImplementedError("Only the cartesian and polar coordinates solvers are implemented.")
