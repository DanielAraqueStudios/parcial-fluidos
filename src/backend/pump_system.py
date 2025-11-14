"""
Pump System Analysis Module
Calculates system curves, pump curves, and operating points
"""

import numpy as np
from math import log10
from scipy.optimize import fsolve
from typing import Dict, Tuple, List


class PumpSystemAnalyzer:
    """
    Comprehensive pump system analyzer for fluid mechanics applications.
    Calculates friction factors, system curves, pump curves, and operating points.
    """
    
    def __init__(self, diameter: float = 0.0203):
        """
        Initialize pump system analyzer.
        
        Args:
            diameter: Pipe diameter in meters (default: 0.0203 m)
        """
        self.diameter = diameter
        self.area = np.pi * (diameter / 2) ** 2
        
        # System parameters (from original code)
        self.roughness_factor = 81.2  # 3.7 * D/ε
        self.reynolds_coefficient = 22706.9
        self.static_head = 7.85  # m
        self.loss_coefficient_1 = 8694.6
        self.loss_coefficient_2 = 23.65
        self.gravity_factor = 19.62  # 2*g
        
        # Pump parameters
        self.pump_max_head = 24.4  # m
        self.pump_coefficient = 0.0678
        self.pump_velocity_factor = 19.42
        
    def calculate_friction_factor(self, velocity: float) -> float:
        """
        Calculate Darcy friction factor using Colebrook-White equation.
        
        Args:
            velocity: Flow velocity in m/s
            
        Returns:
            Friction factor F (dimensionless)
        """
        term1 = 1 / (3.7 * self.roughness_factor)
        term2 = 5.74 / (self.reynolds_coefficient * velocity) ** 0.9
        F = 0.25 / (log10(term1 + term2)) ** 2
        return F
    
    def calculate_system_head(self, velocity: float) -> float:
        """
        Calculate system required head (ha) - System Resistance Curve.
        
        Args:
            velocity: Flow velocity in m/s
            
        Returns:
            System head in meters
        """
        F = self.calculate_friction_factor(velocity)
        dynamic_loss = (self.loss_coefficient_1 * F + self.loss_coefficient_2) * \
                       (velocity ** 2 / self.gravity_factor)
        ha = self.static_head + dynamic_loss
        return ha
    
    def calculate_pump_head(self, velocity: float) -> float:
        """
        Calculate pump available head (Ha) - Pump Characteristic Curve.
        
        Args:
            velocity: Flow velocity in m/s
            
        Returns:
            Pump head in meters
        """
        Ha = self.pump_max_head - self.pump_coefficient * \
             (self.pump_velocity_factor * velocity) ** 2
        return Ha
    
    def calculate_flow_rate(self, velocity: float) -> float:
        """
        Calculate volumetric flow rate from velocity.
        
        Args:
            velocity: Flow velocity in m/s
            
        Returns:
            Flow rate in m³/s
        """
        return velocity * self.area
    
    def find_operating_point(self, initial_guess: float = 0.5) -> Dict[str, float]:
        """
        Find the operating point where system curve intersects pump curve.
        
        Args:
            initial_guess: Initial velocity guess for solver in m/s
            
        Returns:
            Dictionary with operating point data
        """
        def difference(v):
            return self.calculate_pump_head(v) - self.calculate_system_head(v)
        
        try:
            v_operating = fsolve(difference, initial_guess)[0]
            ha_operating = self.calculate_system_head(v_operating)
            Ha_operating = self.calculate_pump_head(v_operating)
            Q_operating = self.calculate_flow_rate(v_operating)
            F_operating = self.calculate_friction_factor(v_operating)
            
            # Calculate Reynolds number approximation
            reynolds_partial = self.reynolds_coefficient * v_operating
            
            result = {
                'velocity': v_operating,
                'head': ha_operating,
                'head_pump': Ha_operating,
                'flow_rate_m3s': Q_operating,
                'flow_rate_ls': Q_operating * 1000,
                'friction_factor': F_operating,
                'reynolds_partial': reynolds_partial,
                'difference': abs(ha_operating - Ha_operating),
                'success': True
            }
            
        except Exception as e:
            result = {
                'success': False,
                'error': str(e)
            }
        
        return result
    
    def generate_curves(self, v_min: float = 0.1, v_max: float = 2.0, 
                       num_points: int = 500) -> Dict[str, np.ndarray]:
        """
        Generate system and pump curves over a velocity range.
        
        Args:
            v_min: Minimum velocity in m/s
            v_max: Maximum velocity in m/s
            num_points: Number of points to calculate
            
        Returns:
            Dictionary with velocity, flow rate, system head, and pump head arrays
        """
        velocities = np.linspace(v_min, v_max, num_points)
        
        ha_values = np.array([self.calculate_system_head(v) for v in velocities])
        Ha_values = np.array([self.calculate_pump_head(v) for v in velocities])
        flow_rates = np.array([self.calculate_flow_rate(v) for v in velocities])
        
        return {
            'velocities': velocities,
            'flow_rates': flow_rates,
            'system_head': ha_values,
            'pump_head': Ha_values
        }
    
    def get_system_info(self) -> Dict[str, float]:
        """
        Get system configuration information.
        
        Returns:
            Dictionary with system parameters
        """
        return {
            'diameter': self.diameter,
            'area': self.area,
            'static_head': self.static_head,
            'pump_max_head': self.pump_max_head,
            'roughness_factor': self.roughness_factor
        }
    
    def analyze_complete_system(self, v_min: float = 0.1, v_max: float = 2.0,
                               num_points: int = 500) -> Dict:
        """
        Perform complete system analysis including curves and operating point.
        
        Args:
            v_min: Minimum velocity in m/s
            v_max: Maximum velocity in m/s
            num_points: Number of points for curves
            
        Returns:
            Complete analysis dictionary with all results
        """
        curves = self.generate_curves(v_min, v_max, num_points)
        operating_point = self.find_operating_point()
        system_info = self.get_system_info()
        
        return {
            'curves': curves,
            'operating_point': operating_point,
            'system_info': system_info
        }
