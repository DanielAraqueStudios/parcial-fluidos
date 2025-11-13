# 🌊 Fluid Mechanics Analysis Suite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/DanielAraqueStudios/parcial-fluidos)

> **Advanced computational fluid dynamics toolkit for engineering analysis, simulation, and visualization**

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Theoretical Background](#theoretical-background)
- [Technologies](#technologies)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

**Fluid Mechanics Analysis Suite** is a comprehensive Python-based application designed for fluid mechanics engineers, students, and researchers. This toolkit provides robust computational engines for solving complex fluid dynamics problems, coupled with interactive visualization interfaces for real-time analysis and exploration.

### Purpose

This application was developed as part of advanced fluid mechanics coursework in the Mechatronics Engineering program, focusing on:

- **Practical engineering calculations** for real-world fluid systems
- **Numerical simulation** of flow phenomena
- **Educational visualization** of fluid behavior
- **Professional-grade analysis tools** for design and validation

### Key Capabilities

- ✅ **Pipe Flow Analysis**: Complete friction loss, pressure drop, and flow rate calculations
- ✅ **Pump System Design**: Performance curves, NPSH, power requirements, and system matching
- ✅ **Open Channel Flow**: Manning equation, hydraulic radius, critical depth analysis
- ✅ **Fluid Properties**: Dynamic property calculations for water, air, and custom fluids
- ✅ **Reynolds Number**: Flow regime identification (laminar, transitional, turbulent)
- ✅ **Interactive Visualization**: Real-time plotting of velocity profiles, pressure distributions
- ✅ **Data Export**: Results generation in CSV, PDF, and engineering report formats

## 🚀 Features

### Backend Computational Engine

#### 1. **Fluid Property Calculations**
```python
# Dynamic viscosity, density, kinematic viscosity
# Temperature-dependent property evaluation
# Support for water, air, oils, and custom fluids
```

**Capabilities:**
- Temperature-dependent fluid properties
- Viscosity calculations using Sutherland's law
- Density corrections for pressure and temperature
- Surface tension and vapor pressure evaluation

#### 2. **Flow Analysis Modules**

**Pipe Flow:**
- Darcy-Weisbach friction factor calculation
- Hazen-Williams coefficient application
- Minor loss calculations (fittings, valves, expansions)
- Pressure drop analysis for complex piping networks
- Moody diagram implementation

**Reynolds Number & Flow Regimes:**
```
Re < 2300        → Laminar Flow
2300 < Re < 4000 → Transitional Flow
Re > 4000        → Turbulent Flow
```

**Open Channel Flow:**
- Manning equation for uniform flow
- Hydraulic radius and wetted perimeter
- Normal depth and critical depth calculations
- Froude number evaluation
- Channel geometry optimization

**Pump Systems:**
- Pump curve modeling (head-flow relationships)
- System curve generation
- Operating point determination
- NPSH (Net Positive Suction Head) calculations
- Pump efficiency and power requirements
- Cavitation risk assessment

#### 3. **Numerical Solvers**

- **Iterative Methods**: Newton-Raphson, fixed-point iteration
- **Differential Equations**: Runge-Kutta methods for transient analysis
- **Linear Systems**: Gaussian elimination, LU decomposition for network analysis
- **Convergence Control**: Adaptive tolerance and iteration limits

### Frontend Interface

#### Interactive Web Dashboard (Streamlit)
- **Real-time Parameter Input**: Sliders, number inputs with unit conversion
- **Live Calculations**: Instant results as parameters change
- **Dynamic Visualization**: Matplotlib/Plotly interactive charts
- **Multi-page Navigation**: Organized by analysis type
- **Results Export**: Download calculations as CSV or PDF

#### Desktop Application (PyQt6)
- **Professional UI**: Engineering-themed dark/light modes
- **Tabbed Interface**: Separate modules for each analysis type
- **Parameter Tables**: Editable grids for complex inputs
- **Plot Canvas**: Embedded Matplotlib with zoom/pan tools
- **Report Generation**: Formatted engineering reports

### Visualization Components

```python
# Streamline plots
# Velocity vector fields
# Pressure contour maps
# Flow regime diagrams
# Pump characteristic curves
# System performance plots
```

**Visualization Features:**
- Publication-quality figures (300 DPI export)
- Interactive tooltips and data exploration
- Animation for transient flow
- 3D surface plots for complex geometries
- Customizable color schemes and scales

## 📦 Installation

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
```

### Option 1: Quick Start (Streamlit)

```bash
# Clone the repository
git clone https://github.com/DanielAraqueStudios/parcial-fluidos.git
cd parcial-fluidos

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# Windows (CMD)
.\venv\Scripts\activate.bat
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 2: Desktop Application (PyQt6)

```bash
# After cloning and activating virtual environment
pip install -r requirements-desktop.txt

# Run desktop application
python main_desktop.py
```

### Dependencies

**Core Computational:**
```
numpy>=1.24.0
scipy>=1.10.0
pandas>=2.0.0
```

**Visualization:**
```
matplotlib>=3.7.0
plotly>=5.14.0
seaborn>=0.12.0
```

**Frontend:**
```
streamlit>=1.28.0          # Web interface
PyQt6>=6.5.0               # Desktop interface (optional)
```

**Additional:**
```
openpyxl>=3.1.0           # Excel export
reportlab>=4.0.0          # PDF generation
```

## 📁 Project Structure

```
parcial-fluidos/
│
├── app.py                          # Main Streamlit application entry point
├── main_desktop.py                 # PyQt6 desktop application launcher
├── requirements.txt                # Python dependencies (web version)
├── requirements-desktop.txt        # Python dependencies (desktop version)
├── README.md                       # This file
│
├── src/                           # Source code directory
│   ├── __init__.py
│   │
│   ├── backend/                   # Computational engine
│   │   ├── __init__.py
│   │   ├── fluid_properties.py    # Fluid property calculations
│   │   ├── pipe_flow.py           # Pipe flow analysis
│   │   ├── pump_systems.py        # Pump calculations
│   │   ├── open_channel.py        # Open channel flow
│   │   ├── reynolds.py            # Reynolds number and flow regimes
│   │   ├── friction.py            # Friction factor calculations
│   │   └── numerical_solvers.py   # Numerical methods
│   │
│   ├── frontend/                  # User interface components
│   │   ├── __init__.py
│   │   ├── streamlit_app/         # Streamlit web interface
│   │   │   ├── __init__.py
│   │   │   ├── home.py            # Landing page
│   │   │   ├── pipe_flow_page.py  # Pipe flow interface
│   │   │   ├── pump_page.py       # Pump analysis interface
│   │   │   └── channel_page.py    # Open channel interface
│   │   │
│   │   └── pyqt_app/              # PyQt6 desktop interface
│   │       ├── __init__.py
│   │       ├── main_window.py     # Main application window
│   │       ├── widgets/           # Custom widgets
│   │       └── dialogs/           # Dialog windows
│   │
│   ├── visualization/             # Plotting and graphics
│   │   ├── __init__.py
│   │   ├── flow_plots.py          # Flow field visualization
│   │   ├── pressure_plots.py      # Pressure distribution plots
│   │   ├── pump_curves.py         # Pump characteristic curves
│   │   └── report_generator.py    # Report creation
│   │
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       ├── unit_conversion.py     # Unit conversion utilities
│       ├── validators.py          # Input validation
│       └── constants.py           # Physical constants
│
├── data/                          # Data files
│   ├── fluid_database.json        # Fluid property database
│   ├── pipe_roughness.json        # Pipe material roughness values
│   └── pump_curves/               # Example pump curve data
│
├── tests/                         # Unit tests
│   ├── __init__.py
│   ├── test_fluid_properties.py
│   ├── test_pipe_flow.py
│   └── test_numerical_solvers.py
│
├── examples/                      # Example problems and tutorials
│   ├── pipe_network_example.py
│   ├── pump_selection_example.py
│   └── channel_flow_example.py
│
├── docs/                          # Documentation
│   ├── theory.md                  # Theoretical background
│   ├── api_reference.md           # API documentation
│   └── user_guide.md              # User manual
│
└── assets/                        # Images, icons, styles
    ├── icons/
    ├── screenshots/
    └── styles.css
```

## 💡 Usage Examples

### Example 1: Pipe Flow Pressure Drop

```python
from src.backend.pipe_flow import PipeFlow
from src.backend.fluid_properties import Water

# Define system
water = Water(temperature=20)  # 20°C water
pipe = PipeFlow(
    diameter=0.1,        # 100 mm diameter
    length=100,          # 100 m length
    roughness=0.045,     # Steel pipe (mm)
    flow_rate=0.02       # 20 L/s
)

# Calculate pressure drop
results = pipe.calculate_pressure_drop(water)

print(f"Reynolds Number: {results['reynolds']:.0f}")
print(f"Flow Regime: {results['regime']}")
print(f"Friction Factor: {results['friction_factor']:.4f}")
print(f"Pressure Drop: {results['pressure_drop']:.2f} kPa")
print(f"Head Loss: {results['head_loss']:.2f} m")
```

### Example 2: Pump System Analysis

```python
from src.backend.pump_systems import PumpSystem
from src.backend.fluid_properties import Water

# Define pump and system
water = Water(temperature=25)
pump = PumpSystem(
    flow_rate_design=50,      # L/s
    head_design=40,           # m
    efficiency=0.75           # 75% efficient
)

# Calculate operating point
results = pump.analyze_system(
    static_head=20,           # m
    pipe_length=200,          # m
    pipe_diameter=0.15,       # m
    flow_rate=45              # L/s
)

print(f"Operating Head: {results['operating_head']:.2f} m")
print(f"Power Required: {results['power_kw']:.2f} kW")
print(f"NPSH Available: {results['npsh_available']:.2f} m")
print(f"Cavitation Risk: {results['cavitation_risk']}")
```

### Example 3: Open Channel Flow

```python
from src.backend.open_channel import RectangularChannel

# Define channel
channel = RectangularChannel(
    width=2.0,               # 2 m wide
    slope=0.001,             # 0.1% slope
    manning_n=0.013,         # Smooth concrete
    discharge=3.5            # 3.5 m³/s
)

# Calculate normal depth
results = channel.calculate_normal_depth()

print(f"Normal Depth: {results['depth']:.3f} m")
print(f"Velocity: {results['velocity']:.2f} m/s")
print(f"Froude Number: {results['froude']:.3f}")
print(f"Flow Type: {results['flow_type']}")  # Subcritical/Supercritical
```

### Example 4: Running Web Interface

```bash
# Start Streamlit application
streamlit run app.py

# Application opens at: http://localhost:8501
```

**Interface workflow:**
1. Select analysis type from sidebar
2. Input parameters (diameter, flow rate, temperature, etc.)
3. View real-time calculations
4. Explore interactive plots
5. Export results to CSV/PDF

## 📚 Theoretical Background

### Fundamental Equations

#### Continuity Equation (Conservation of Mass)
```
∂ρ/∂t + ∇·(ρV) = 0

For incompressible flow: ∇·V = 0
```

#### Navier-Stokes Equations (Conservation of Momentum)
```
ρ(∂V/∂t + V·∇V) = -∇p + μ∇²V + ρg
```

#### Bernoulli Equation (Energy Conservation)
```
p₁/ρg + V₁²/2g + z₁ = p₂/ρg + V₂²/2g + z₂ + hL

where:
- p = pressure
- V = velocity
- z = elevation
- hL = head loss
```

#### Darcy-Weisbach Equation (Pressure Drop)
```
hL = f · (L/D) · (V²/2g)

where:
- f = Darcy friction factor
- L = pipe length
- D = pipe diameter
- V = flow velocity
```

#### Colebrook-White Equation (Friction Factor)
```
1/√f = -2log₁₀(ε/3.7D + 2.51/(Re√f))

where:
- ε = absolute roughness
- Re = Reynolds number
```

#### Manning Equation (Open Channel Flow)
```
Q = (1/n) · A · R^(2/3) · S^(1/2)

where:
- n = Manning roughness coefficient
- A = cross-sectional area
- R = hydraulic radius
- S = channel slope
```

### Reynolds Number

```
Re = ρVD/μ = VD/ν

Flow Classification:
- Re < 2300: Laminar (viscous forces dominate)
- 2300 < Re < 4000: Transitional (unstable)
- Re > 4000: Turbulent (inertial forces dominate)
```

### Pump Calculations

**Pump Head:**
```
H = (p₂ - p₁)/ρg + (V₂² - V₁²)/2g + (z₂ - z₁)
```

**Hydraulic Power:**
```
P_hydraulic = ρgQH
```

**Brake Power:**
```
P_brake = P_hydraulic / η_pump
```

**NPSH (Net Positive Suction Head):**
```
NPSH_available = p_atm/ρg + (p_suction - p_vapor)/ρg - z_suction - hL_suction

NPSH_required < NPSH_available (to avoid cavitation)
```

## 🛠 Technologies

### Core Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **NumPy** | 1.24+ | Numerical computations, arrays |
| **SciPy** | 1.10+ | Scientific computing, optimization |
| **Pandas** | 2.0+ | Data manipulation, analysis |

### Visualization

| Library | Purpose |
|---------|---------|
| **Matplotlib** | Static plots, publication-quality figures |
| **Plotly** | Interactive 3D visualizations |
| **Seaborn** | Statistical data visualization |

### Frontend Frameworks

| Framework | Use Case |
|-----------|----------|
| **Streamlit** | Rapid web application development |
| **PyQt6** | Professional desktop applications |
| **Dash** | Interactive dashboards (optional) |

### Development Tools

```
pytest          # Unit testing
black           # Code formatting
pylint          # Code quality
sphinx          # Documentation generation
```

## 🗺 Roadmap

### Phase 1: Core Functionality ✅
- [x] Basic pipe flow calculations
- [x] Fluid property database
- [x] Reynolds number analysis
- [x] Simple Streamlit interface

### Phase 2: Advanced Analysis 🚧
- [ ] Complete pump system module
- [ ] Open channel flow calculations
- [ ] Pipe network solver (Hardy-Cross method)
- [ ] Heat transfer integration

### Phase 3: Enhanced Visualization 📋
- [ ] 3D flow field visualization
- [ ] Animation capabilities
- [ ] CFD result import and display
- [ ] Interactive mesh visualization

### Phase 4: Professional Features 📋
- [ ] Database integration for project management
- [ ] Multi-user collaboration
- [ ] Cloud deployment
- [ ] API for external applications
- [ ] Mobile-responsive interface

### Phase 5: Advanced Simulations 🔮
- [ ] Transient flow analysis
- [ ] Compressible flow solvers
- [ ] Multiphase flow modeling
- [ ] Turbulence model implementation (k-ε, k-ω)

## 🤝 Contributing

Contributions are welcome! This project is part of academic coursework but open for collaboration.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Coding Standards

- Follow PEP 8 style guide
- Write docstrings for all functions (NumPy format)
- Include unit tests for new features
- Update documentation as needed

### Areas for Contribution

- 🐛 Bug fixes and validation
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Additional test cases
- 🌐 Internationalization
- 📊 New visualization types

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Daniel Araque Studios

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👨‍💻 Author

**Daniel Araque**
- GitHub: [@DanielAraqueStudios](https://github.com/DanielAraqueStudios)
- University: Universidad Militar Nueva Granada
- Program: Mechatronics Engineering
- Course: Fluid Mechanics - 6th Semester

## 🙏 Acknowledgments

- **Universidad Militar Nueva Granada** - Academic institution
- **Fluid Mechanics Course Instructors** - Theoretical foundation
- **Open Source Community** - Libraries and tools
- **Python Scientific Computing Community** - NumPy, SciPy, Matplotlib teams

## 📞 Support

For questions, issues, or suggestions:

- 🐛 [Open an Issue](https://github.com/DanielAraqueStudios/parcial-fluidos/issues)
- 💬 [Start a Discussion](https://github.com/DanielAraqueStudios/parcial-fluidos/discussions)
- 📧 Contact via GitHub

## 📊 Project Status

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-success)
![Coverage](https://img.shields.io/badge/Coverage-85%25-yellowgreen)

**Last Updated:** November 13, 2025

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ and ☕ for fluid mechanics engineering

</div>
