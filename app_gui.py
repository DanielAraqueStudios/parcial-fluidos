"""
PyQt6 Application Launcher for Pump System Analysis
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.frontend.main_window import main

if __name__ == '__main__':
    main()
