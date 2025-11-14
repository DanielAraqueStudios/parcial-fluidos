# 🚀 Building Executable with PyInstaller

## 📦 Build Instructions

### Method 1: Using the Spec File (Recommended)
```powershell
pyinstaller PumpSystemAnalysis.spec --clean
```

### Method 2: Direct Command
```powershell
pyinstaller --onefile --windowed --name "PumpSystemAnalysis" `
  --add-data "src;src" `
  --hidden-import "PyQt6.QtCore" `
  --hidden-import "PyQt6.QtGui" `
  --hidden-import "PyQt6.QtWidgets" `
  --hidden-import "matplotlib.backends.backend_qt5agg" `
  --hidden-import "scipy.optimize" `
  --exclude-module "tkinter" `
  app_gui.py
```

## 📋 Build Options Explained

- `--onefile`: Creates a single executable file
- `--windowed`: No console window (GUI only)
- `--name`: Name of the executable
- `--add-data`: Include source code folders
- `--hidden-import`: Explicitly include modules
- `--exclude-module`: Exclude unnecessary modules
- `--clean`: Clean cache before building

## 📁 Output Location

After building, find your executable at:
```
dist/PumpSystemAnalysis.exe
```

## 📊 Expected File Size

- **Executable**: ~150-200 MB (includes Python runtime + all libraries)
- **Build time**: 2-5 minutes

## ✅ Post-Build Testing

1. Navigate to `dist/` folder
2. Run `PumpSystemAnalysis.exe`
3. Verify all features work:
   - [ ] Application launches
   - [ ] Plots display correctly
   - [ ] Calculations work
   - [ ] Tables populate
   - [ ] Input changes update results

## 🎯 Distribution

The executable is **standalone** and can be:
- ✅ Copied to any Windows computer
- ✅ Run without Python installation
- ✅ Shared via USB/email/cloud
- ✅ Used for presentations

## 🔧 Troubleshooting

### Issue: "Module not found" error
**Solution**: Add missing module to `hiddenimports` in spec file

### Issue: Large file size
**Solution**: This is normal - includes entire Python runtime

### Issue: Slow startup
**Solution**: First launch extracts files (temporary delay)

### Issue: Antivirus warning
**Solution**: PyInstaller executables sometimes trigger false positives

## 📦 Advanced: Creating Installer

To create a proper installer (optional):

### Using Inno Setup:
1. Download Inno Setup
2. Create installer script
3. Include executable and dependencies

### Using NSIS:
1. Download NSIS
2. Create installation script
3. Build installer package

## 🎨 Adding Icon (Optional)

1. Create or download a `.ico` file
2. Place in project root (e.g., `icon.ico`)
3. Update spec file:
   ```python
   icon='icon.ico'
   ```
4. Rebuild

## 📝 Notes

- Build on same OS as target (Windows for Windows)
- Executable includes all dependencies
- No need to ship `requirements.txt`
- Source code is bundled but compiled
