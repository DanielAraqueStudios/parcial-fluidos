"""
Main Window for Pump System Analysis Application
Professional PyQt6 UI with embedded Matplotlib visualizations
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QGroupBox, QSplitter, QTabWidget, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPalette, QColor, QIcon
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

# Import backend
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.backend.pump_system import PumpSystemAnalyzer


class MatplotlibCanvas(FigureCanvas):
    """Custom Matplotlib canvas for PyQt6 integration"""
    
    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)
        
        # Set figure background
        self.fig.patch.set_facecolor('#2b2b2b')
        
    def plot_system_curves(self, curves_data, operating_point, plot_type='velocity'):
        """
        Plot system and pump curves.
        
        Args:
            curves_data: Dictionary with curve arrays
            operating_point: Operating point data
            plot_type: 'velocity' or 'flowrate'
        """
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        
        # Set dark theme colors
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white', which='both')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')
        
        if plot_type == 'velocity':
            x_data = curves_data['velocities']
            x_label = 'Velocidad (v) [m/s]'
            x_op = operating_point['velocity']
            annotation_text = f'v = {x_op:.4f} m/s\nh = {operating_point["head"]:.4f} m'
            annotation_pos = (x_op + 0.15, operating_point["head"] + 2)
        else:  # flowrate
            x_data = curves_data['flow_rates']
            x_label = 'Caudal (Q) [m³/s]'
            x_op = operating_point['flow_rate_m3s']
            annotation_text = f'Q = {x_op:.6f} m³/s\n({operating_point["flow_rate_ls"]:.4f} L/s)\nh = {operating_point["head"]:.4f} m'
            annotation_pos = (x_op + 0.00005, operating_point["head"] + 2)
        
        # Plot curves
        ax.plot(x_data, curves_data['system_head'], 'b-', linewidth=2.5, 
                label='ha (System Required Curve)', color='#3498db')
        ax.plot(x_data, curves_data['pump_head'], 'r-', linewidth=2.5, 
                label='Ha (Pump Available Head)', color='#e74c3c')
        
        # Plot operating point
        if operating_point['success']:
            ax.plot(x_op, operating_point["head"], 'o', markersize=12, 
                   color='#2ecc71', markeredgecolor='white', markeredgewidth=2,
                   label='Operating Point', zorder=5)
            
            # Add crosshairs
            ax.axvline(x=x_op, color='#2ecc71', linestyle='--', alpha=0.5, linewidth=1.5)
            ax.axhline(y=operating_point["head"], color='#2ecc71', linestyle='--', 
                      alpha=0.5, linewidth=1.5)
            
            # Annotation
            ax.annotate(annotation_text,
                       xy=(x_op, operating_point["head"]),
                       xytext=annotation_pos,
                       fontsize=9,
                       color='black',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='#f39c12', 
                                alpha=0.9, edgecolor='white', linewidth=2),
                       arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2',
                                     color='white', lw=2))
        
        # Labels and title
        ax.set_xlabel(x_label, fontsize=12, color='white', fontweight='bold')
        ax.set_ylabel('Altura (h) [m]', fontsize=12, color='white', fontweight='bold')
        
        title = 'Ha y ha vs Velocidad' if plot_type == 'velocity' else 'Ha y ha vs Caudal'
        ax.set_title(title, fontsize=14, color='white', fontweight='bold', pad=20)
        
        # Legend
        legend = ax.legend(fontsize=10, loc='best', facecolor='#2b2b2b', 
                          edgecolor='white', framealpha=0.9)
        for text in legend.get_texts():
            text.set_color('white')
        
        # Grid
        ax.grid(True, alpha=0.2, color='white', linestyle='--')
        
        self.fig.tight_layout()
        self.draw()


class PumpSystemWindow(QMainWindow):
    """Main application window for pump system analysis"""
    
    def __init__(self):
        super().__init__()
        self.analyzer = PumpSystemAnalyzer()
        self.setup_ui()
        self.apply_dark_theme()
        self.calculate_and_update()
        
    def setup_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("🌊 Pump System Analysis - Fluid Mechanics Suite")
        self.setGeometry(100, 100, 1600, 900)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Controls and Results
        left_panel = self.create_left_panel()
        splitter.addWidget(left_panel)
        
        # Right panel - Visualizations
        right_panel = self.create_right_panel()
        splitter.addWidget(right_panel)
        
        # Set initial sizes (30% left, 70% right)
        splitter.setSizes([480, 1120])
        
        main_layout.addWidget(splitter)
        
    def create_left_panel(self):
        """Create left control panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setSpacing(15)
        
        # Title
        title = QLabel("⚙️ SYSTEM PARAMETERS")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Input group
        input_group = self.create_input_group()
        layout.addWidget(input_group)
        
        # Calculate button
        calc_btn = QPushButton("🔄 CALCULATE OPERATING POINT")
        calc_btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        calc_btn.setMinimumHeight(50)
        calc_btn.clicked.connect(self.calculate_and_update)
        calc_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(calc_btn)
        
        # Results table
        results_group = self.create_results_group()
        layout.addWidget(results_group)
        
        # System info
        system_info_group = self.create_system_info_group()
        layout.addWidget(system_info_group)
        
        layout.addStretch()
        
        return panel
    
    def create_input_group(self):
        """Create input parameter group"""
        group = QGroupBox("📊 Input Parameters")
        group.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Diameter input
        diameter_layout = QHBoxLayout()
        diameter_label = QLabel("Pipe Diameter (m):")
        diameter_label.setMinimumWidth(150)
        self.diameter_input = QLineEdit("0.0203")
        self.diameter_input.setFont(QFont("Arial", 10))
        diameter_layout.addWidget(diameter_label)
        diameter_layout.addWidget(self.diameter_input)
        layout.addLayout(diameter_layout)
        
        # Velocity range
        v_min_layout = QHBoxLayout()
        v_min_label = QLabel("Min Velocity (m/s):")
        v_min_label.setMinimumWidth(150)
        self.v_min_input = QLineEdit("0.1")
        self.v_min_input.setFont(QFont("Arial", 10))
        v_min_layout.addWidget(v_min_label)
        v_min_layout.addWidget(self.v_min_input)
        layout.addLayout(v_min_layout)
        
        v_max_layout = QHBoxLayout()
        v_max_label = QLabel("Max Velocity (m/s):")
        v_max_label.setMinimumWidth(150)
        self.v_max_input = QLineEdit("2.0")
        self.v_max_input.setFont(QFont("Arial", 10))
        v_max_layout.addWidget(v_max_label)
        v_max_layout.addWidget(self.v_max_input)
        layout.addLayout(v_max_layout)
        
        group.setLayout(layout)
        return group
    
    def create_results_group(self):
        """Create results display group"""
        group = QGroupBox("📈 Operating Point Results")
        group.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        layout = QVBoxLayout()
        
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(["Parameter", "Value"])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setFont(QFont("Consolas", 9))
        self.results_table.setAlternatingRowColors(True)
        
        layout.addWidget(self.results_table)
        group.setLayout(layout)
        
        return group
    
    def create_system_info_group(self):
        """Create system information group"""
        group = QGroupBox("ℹ️ System Information")
        group.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        layout = QVBoxLayout()
        
        self.system_table = QTableWidget()
        self.system_table.setColumnCount(2)
        self.system_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.system_table.horizontalHeader().setStretchLastSection(True)
        self.system_table.setFont(QFont("Consolas", 9))
        self.system_table.setAlternatingRowColors(True)
        
        layout.addWidget(self.system_table)
        group.setLayout(layout)
        
        return group
    
    def create_right_panel(self):
        """Create right visualization panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Title
        title = QLabel("📊 SYSTEM ANALYSIS VISUALIZATION")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Tab widget for different plots
        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 10))
        
        # Velocity plot tab
        velocity_tab = QWidget()
        velocity_layout = QVBoxLayout(velocity_tab)
        self.velocity_canvas = MatplotlibCanvas(self, width=8, height=6, dpi=100)
        velocity_toolbar = NavigationToolbar(self.velocity_canvas, self)
        velocity_layout.addWidget(velocity_toolbar)
        velocity_layout.addWidget(self.velocity_canvas)
        self.tab_widget.addTab(velocity_tab, "📉 Head vs Velocity")
        
        # Flow rate plot tab
        flowrate_tab = QWidget()
        flowrate_layout = QVBoxLayout(flowrate_tab)
        self.flowrate_canvas = MatplotlibCanvas(self, width=8, height=6, dpi=100)
        flowrate_toolbar = NavigationToolbar(self.flowrate_canvas, self)
        flowrate_layout.addWidget(flowrate_toolbar)
        flowrate_layout.addWidget(self.flowrate_canvas)
        self.tab_widget.addTab(flowrate_tab, "📉 Head vs Flow Rate")
        
        layout.addWidget(self.tab_widget)
        
        return panel
    
    def calculate_and_update(self):
        """Calculate system and update all displays"""
        try:
            # Get input values
            diameter = float(self.diameter_input.text())
            v_min = float(self.v_min_input.text())
            v_max = float(self.v_max_input.text())
            
            # Update analyzer
            self.analyzer = PumpSystemAnalyzer(diameter)
            
            # Perform analysis
            analysis = self.analyzer.analyze_complete_system(v_min, v_max, 500)
            
            # Update results table
            self.update_results_table(analysis['operating_point'])
            
            # Update system info table
            self.update_system_table(analysis['system_info'])
            
            # Update plots
            self.velocity_canvas.plot_system_curves(
                analysis['curves'], 
                analysis['operating_point'], 
                'velocity'
            )
            
            self.flowrate_canvas.plot_system_curves(
                analysis['curves'], 
                analysis['operating_point'], 
                'flowrate'
            )
            
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", 
                              f"Please enter valid numeric values.\n{str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Calculation Error", 
                               f"An error occurred during calculation:\n{str(e)}")
    
    def update_results_table(self, operating_point):
        """Update results table with operating point data"""
        if not operating_point['success']:
            self.results_table.setRowCount(1)
            self.results_table.setItem(0, 0, QTableWidgetItem("Error"))
            self.results_table.setItem(0, 1, QTableWidgetItem(operating_point.get('error', 'Unknown error')))
            return
        
        results = [
            ("Velocity (v)", f"{operating_point['velocity']:.4f} m/s"),
            ("Flow Rate (Q)", f"{operating_point['flow_rate_m3s']:.6f} m³/s"),
            ("Flow Rate (Q)", f"{operating_point['flow_rate_ls']:.4f} L/s"),
            ("Operating Head (h)", f"{operating_point['head']:.4f} m"),
            ("Pump Head (Ha)", f"{operating_point['head_pump']:.4f} m"),
            ("Friction Factor (F)", f"{operating_point['friction_factor']:.6f}"),
            ("Reynolds (partial)", f"{operating_point['reynolds_partial']:.2f}"),
            ("Head Difference", f"{operating_point['difference']:.6f} m"),
        ]
        
        self.results_table.setRowCount(len(results))
        
        for i, (param, value) in enumerate(results):
            param_item = QTableWidgetItem(param)
            param_item.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            value_item = QTableWidgetItem(value)
            value_item.setFont(QFont("Consolas", 10))
            
            self.results_table.setItem(i, 0, param_item)
            self.results_table.setItem(i, 1, value_item)
        
        self.results_table.resizeColumnsToContents()
    
    def update_system_table(self, system_info):
        """Update system information table"""
        info = [
            ("Pipe Diameter", f"{system_info['diameter']:.4f} m"),
            ("Cross-sectional Area", f"{system_info['area']:.6f} m²"),
            ("Static Head", f"{system_info['static_head']:.2f} m"),
            ("Pump Max Head", f"{system_info['pump_max_head']:.2f} m"),
            ("Roughness Factor", f"{system_info['roughness_factor']:.2f}"),
        ]
        
        self.system_table.setRowCount(len(info))
        
        for i, (prop, value) in enumerate(info):
            prop_item = QTableWidgetItem(prop)
            prop_item.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            value_item = QTableWidgetItem(value)
            value_item.setFont(QFont("Consolas", 10))
            
            self.system_table.setItem(i, 0, prop_item)
            self.system_table.setItem(i, 1, value_item)
        
        self.system_table.resizeColumnsToContents()
    
    def apply_dark_theme(self):
        """Apply professional dark theme"""
        dark_palette = QPalette()
        
        # Colors
        dark_color = QColor(30, 30, 30)
        darker_color = QColor(20, 20, 20)
        text_color = QColor(255, 255, 255)
        highlight_color = QColor(52, 152, 219)
        
        dark_palette.setColor(QPalette.ColorRole.Window, dark_color)
        dark_palette.setColor(QPalette.ColorRole.WindowText, text_color)
        dark_palette.setColor(QPalette.ColorRole.Base, darker_color)
        dark_palette.setColor(QPalette.ColorRole.AlternateBase, dark_color)
        dark_palette.setColor(QPalette.ColorRole.Text, text_color)
        dark_palette.setColor(QPalette.ColorRole.Button, dark_color)
        dark_palette.setColor(QPalette.ColorRole.ButtonText, text_color)
        dark_palette.setColor(QPalette.ColorRole.Highlight, highlight_color)
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, text_color)
        
        self.setPalette(dark_palette)
        
        # Additional styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QGroupBox {
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                background-color: #2b2b2b;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 10px;
                color: #3498db;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
            QLineEdit {
                background-color: #2b2b2b;
                color: white;
                border: 2px solid #555;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            QTableWidget {
                background-color: #2b2b2b;
                alternate-background-color: #333;
                gridline-color: #555;
                border: 1px solid #555;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: 2px solid #3498db;
                border-radius: 5px;
                background-color: #2b2b2b;
            }
            QTabBar::tab {
                background-color: #2b2b2b;
                color: white;
                padding: 10px 20px;
                border: 1px solid #555;
                border-bottom: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
            }
            QTabBar::tab:hover {
                background-color: #34495e;
            }
        """)


def main():
    """Application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Pump System Analysis")
    app.setOrganizationName("Fluid Mechanics Suite")
    
    window = PumpSystemWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
