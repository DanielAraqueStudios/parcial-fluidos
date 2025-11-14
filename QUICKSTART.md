# 🚀 Quick Start Guide - Pump System Analysis GUI

## Installation Complete! ✅

All dependencies have been installed:
- ✅ NumPy (numerical computing)
- ✅ SciPy (scientific computing)
- ✅ Matplotlib (plotting)
- ✅ PyQt6 (GUI framework)

## 📁 Project Structure

```
parcial-fluidos/
├── app_gui.py                  # 👈 RUN THIS FILE!
├── main.py                     # Original console-based script
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
│
└── src/
    ├── backend/
    │   └── pump_system.py      # Calculation engine
    └── frontend/
        └── main_window.py      # PyQt6 UI
```

## 🎯 How to Run

### Option 1: Using VS Code Terminal (PowerShell)

```powershell
# Make sure you're in the project directory
cd "c:\Users\danie\OneDrive - unimilitar.edu.co\Documentos\UNIVERSIDADDDDDDDDDDDDDDDDDDDDDDDDDD\MECATRÓNICA\SEXTO SEMESTRE\fluidos\parcial-fluidos"

# Run the GUI application
python app_gui.py
```

### Option 2: Direct Python Execution

```powershell
"C:/Users/danie/OneDrive - unimilitar.edu.co/Documentos/UNIVERSIDADDDDDDDDDDDDDDDDDDDDDDDDDD/MECATRÓNICA/SEXTO SEMESTRE/fluidos/parcial-fluidos/.venv/Scripts/python.exe" app_gui.py
```

## 🎨 Application Features

### Left Panel - Controls
- **Input Parameters**: Adjust pipe diameter, velocity range
- **Calculate Button**: Compute operating point
- **Results Table**: Shows velocity, flow rate, head, friction factor
- **System Info**: Displays pipe and pump properties

### Right Panel - Visualizations
- **Tab 1**: Head vs Velocity plot
- **Tab 2**: Head vs Flow Rate plot
- **Interactive Tools**: Zoom, pan, save plots
- **Operating Point**: Marked with green dot and annotation

## 📊 What the Application Shows

### System Curves
- **Blue Line (ha)**: System Required Curve - head needed by piping system
- **Red Line (Ha)**: Pump Available Head - head provided by pump
- **Green Point**: Operating Point where curves intersect

### Results Display
- Operating velocity (m/s)
- Flow rate (m³/s and L/s)
- Operating head (m)
- Friction factor
- Reynolds number (partial)
- Head difference (verification)

## 🎛️ How to Use

1. **Launch Application**: Run `python app_gui.py`
2. **Review Default Parameters**: Pipe diameter = 0.0203 m
3. **Click "CALCULATE"**: Computes operating point automatically
4. **View Results**: Check left panel tables
5. **Explore Plots**: Switch between tabs, use toolbar to zoom/pan
6. **Modify Parameters**: Change diameter or velocity range, recalculate

## 🔧 Customization

### Change Pipe Diameter
Enter new value in "Pipe Diameter (m)" field and click Calculate.

### Adjust Velocity Range
Modify "Min Velocity" and "Max Velocity" for different plot ranges.

### Modify System Parameters
Edit `src/backend/pump_system.py` to change:
- Static head
- Pump characteristics
- Roughness factors
- Loss coefficients

## 📸 Expected Output

The GUI displays:
- **Operating Point**: v ≈ 0.xxxx m/s, Q ≈ x.xxxx L/s, h ≈ xx.xx m
- **Two Beautiful Plots**: Dark-themed professional engineering graphs
- **Complete Data Tables**: All parameters formatted and organized

## 🎓 Theory Behind the Calculations

### System Curve (ha)
```
ha = H_static + H_losses
ha = 7.85 + (8694.6*F + 23.65) * (v²/19.62)
```

### Pump Curve (Ha)
```
Ha = H_max - C * Q²
Ha = 24.4 - 0.0678 * (19.42*v)²
```

### Operating Point
Point where: **ha = Ha** (system matches pump)

## 🐛 Troubleshooting

### Application doesn't start
```powershell
# Verify Python environment
python --version

# Reinstall dependencies
pip install -r requirements.txt
```

### Import errors
Make sure you're running from the project root directory.

### Plots don't show
Ensure Matplotlib backend is correctly configured (already set to Qt5Agg).

## 💡 Tips

- **Dark Theme**: Professional dark mode applied automatically
- **Resizable Panels**: Drag splitter between left and right panels
- **Export Plots**: Use toolbar save button on each plot
- **Multiple Calculations**: Change parameters and recalculate anytime

## 🌟 Key Features

✨ **Professional UI/UX Design**
- Modern dark theme
- Color-coded curves (blue/red/green)
- Smooth animations and interactions

✨ **Complete Analysis**
- Automatic operating point calculation
- System and pump curve generation
- Friction factor computation
- Reynolds number evaluation

✨ **Interactive Visualization**
- Two plot tabs (velocity and flow rate views)
- Zoom, pan, save functionality
- Crosshairs at operating point
- Annotated intersection

✨ **Comprehensive Results**
- Formatted data tables
- System information display
- Real-time parameter updates

## 📞 Need Help?

Check the main README.md for detailed documentation on:
- Theoretical background
- Equation derivations
- Advanced customization
- Contributing guidelines

---

**Ready to explore fluid mechanics? Run the application now! 🚀**

```powershell
python app_gui.py
```
