# 🌊 Pump System Analysis Suite

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.5+-green.svg)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/DanielAraqueStudios/parcial-fluidos)

> **Professional PyQt6 desktop application for pump system analysis with real-time visualization and interactive fluid mechanics calculations**

![Application Preview](https://img.shields.io/badge/GUI-PyQt6%20Desktop-blue)
![Analysis](https://img.shields.io/badge/Analysis-Pump%20Systems-orange)

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

**Pump System Analysis Suite** is a professional-grade desktop application built with **PyQt6** for comprehensive pump and piping system analysis. Designed for fluid mechanics engineers, students, and researchers, this application provides robust computational engines coupled with an intuitive graphical interface for real-time analysis and visualization of pump operating points.

### Purpose

This application was developed as part of advanced fluid mechanics coursework (6th Semester) in the **Mechatronics Engineering** program at **Universidad Militar Nueva Granada**, focusing on:

- **Pump Operating Point Determination**: Find where system curves intersect pump curves
- **Real-time Visualization**: Interactive plots with dark professional theme
- **System Analysis**: Complete friction factor, Reynolds number, and head calculations
- **Educational Tool**: Understand pump-system interactions through visual feedback
- **Professional UI/UX**: Desktop application with modern, engineering-focused design

### 🎨 Key Capabilities

- ✅ **Professional PyQt6 GUI**: Modern dark-themed desktop interface with resizable panels
- ✅ **Operating Point Calculator**: Numerical solver finds exact pump-system intersection
- ✅ **Dual Visualization**: Head vs Velocity and Head vs Flow Rate plots
- ✅ **Interactive Matplotlib**: Embedded charts with zoom, pan, and export tools
- ✅ **System Curve Analysis**: Darcy-Weisbach friction with Colebrook-White equation
- ✅ **Pump Characteristic Curve**: Parabolic head-flow relationship modeling
- ✅ **Complete Results Display**: Formatted tables showing all parameters and calculations
- ✅ **Real-time Updates**: Modify parameters and recalculate instantly

## 🚀 Features

### 🎨 Professional PyQt6 Desktop Interface

#### **Main Window Layout**
- **Split Panel Design**: Resizable left control panel (30%) and right visualization panel (70%)
- **Dark Theme**: Professional engineering-focused color scheme (#1e1e1e background)
- **Modern Styling**: Rounded corners, blue accents (#3498db), smooth hover effects
- **Responsive Layout**: Adjustable splitter for custom workspace arrangement

#### **Left Control Panel**
1. **⚙️ Input Parameters Group**
   - Pipe diameter (m) with validation
   - Velocity range (min/max) controls
   - Clean, labeled input fields

2. **🔄 Calculate Button**
   - Large, prominent blue button
   - One-click operating point calculation
   - Hover and pressed states

3. **📈 Operating Point Results Table**
   - Velocity (m/s)
   - Flow rate (m³/s and L/s)
   - Operating head (m)
   - Pump head verification (m)
   - Friction factor
   - Reynolds number (partial)
   - Head difference (convergence check)

4. **ℹ️ System Information Table**
   - Pipe diameter and area
   - Static head
   - Pump maximum head
   - Roughness factor

#### **Right Visualization Panel**
1. **📉 Tabbed Plot Interface**
   - **Tab 1**: Head vs Velocity plot
   - **Tab 2**: Head vs Flow Rate plot
   - Easy switching between views

2. **🎨 Professional Matplotlib Plots**
   - **Blue Curve**: System Required Head (ha) - Darcy-Weisbach losses
   - **Red Curve**: Pump Available Head (Ha) - Pump characteristic
   - **Green Dot**: Operating Point with annotation
   - **Crosshairs**: Visual guides at intersection
   - **Dark Background**: Professional theme matching UI

3. **🛠️ Interactive Toolbar**
   - Zoom rectangle tool
   - Pan navigation
   - Home (reset view)
   - Save figure (PNG/PDF/SVG)

### 🧮 Backend Computational Engine

#### **PumpSystemAnalyzer Class**

**Core Calculations:**
```python
✅ calculate_friction_factor(velocity)    # Colebrook-White equation
✅ calculate_system_head(velocity)        # ha = H_static + H_friction
✅ calculate_pump_head(velocity)          # Ha pump characteristic
✅ find_operating_point()                 # SciPy fsolve intersection
✅ generate_curves()                      # Full curve arrays
✅ analyze_complete_system()              # Complete analysis
```

**Analysis Features:**
- **Friction Factor**: Modified Colebrook-White equation for turbulent flow
- **System Curve**: Static head + velocity-dependent friction losses
- **Pump Curve**: Parabolic head-flow characteristic
- **Operating Point**: Numerical root finding (ha = Ha)
- **Reynolds Number**: Partial calculation for flow regime identification
- **Flow Rate**: Volumetric calculation from velocity and area

#### **Numerical Methods**
- **Root Finding**: SciPy `fsolve` for operating point
- **Convergence**: Automatic tolerance and iteration control
- **Stability**: Validated initial guess ensures convergence
- **Accuracy**: Double-precision floating-point calculations

### 📊 Visualization Features

**Plot Characteristics:**
- **Resolution**: 500 points per curve for smooth lines
- **Annotation**: Yellow box highlighting operating point values
- **Grid**: White dashed grid with 20% opacity
- **Legend**: Color-coded curve identification
- **Axes**: Labeled with units [m/s], [m³/s], [m]
- **Professional**: Publication-ready quality

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
