import numpy as np
import matplotlib.pyplot as plt
from math import log10
from scipy.optimize import fsolve

# Definir las funciones
def calcular_F(v):
    """Calcula el factor de fricción F"""
    return 0.25 / (log10(1 / (3.7 * 81.2) + 5.74 / (22706.9 * v)**0.9))**2

def calcular_ha(v):
    """Calcula ha en función de la velocidad"""
    F = calcular_F(v)
    return 7.85 + (8694.6 * F + 23.65) * (v**2 / 19.62)

def calcular_Ha(v):
    """Calcula Ha en función de la velocidad"""
    return 24.4 - 0.0678 * (19.42 * v)**2

def diferencia(v):
    """Función para encontrar el punto de intersección"""
    return calcular_Ha(v) - calcular_ha(v)

# Definir parámetros del sistema
diametro = 0.0203  # Diámetro de la tubería en metros
area = np.pi * (diametro / 2)**2  # Área de la sección transversal

# Generar rango de velocidades
v_min = 0.1  # Velocidad mínima (evitar división por cero)
v_max = 2.0  # Velocidad máxima
velocidades = np.linspace(v_min, v_max, 500)

# Calcular valores de ha y Ha para cada velocidad
ha_valores = [calcular_ha(v) for v in velocidades]
Ha_valores = [calcular_Ha(v) for v in velocidades]

# Calcular caudales correspondientes a cada velocidad
caudales = velocidades * area  # Q = V * A

# Encontrar el punto de intersección
try:
    v_interseccion = fsolve(diferencia, 0.5)[0]  # Estimación inicial en v=0.5
    ha_interseccion = calcular_ha(v_interseccion)
    Ha_interseccion = calcular_Ha(v_interseccion)
    
    Q_interseccion = v_interseccion * area  # Caudal en el punto de intersección
    
    print(f"Punto de intersección encontrado:")
    print(f"Velocidad (v): {v_interseccion:.4f} m/s")
    print(f"Caudal (Q): {Q_interseccion:.6f} m³/s = {Q_interseccion*1000:.4f} L/s")
    print(f"ha = Ha = {ha_interseccion:.4f} m")
    print(f"Verificación - Ha: {Ha_interseccion:.4f} m")
    print(f"Diferencia: {abs(ha_interseccion - Ha_interseccion):.6f} m")
except:
    print("No se pudo encontrar un punto de intersección en el rango especificado")
    v_interseccion = None

# Crear figura con dos subgráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# ========== GRÁFICA 1: ha y Ha vs Velocidad ==========
ax1.plot(velocidades, ha_valores, 'b-', linewidth=2, label='SRC')
ax1.plot(velocidades, Ha_valores, 'r-', linewidth=2, label='Ha (Head available)')

# Marcar el punto de intersección si existe
if v_interseccion is not None:
    ax1.plot(v_interseccion, ha_interseccion, 'go', markersize=12, 
             label=f'Intersección (v={v_interseccion:.4f} m/s, h={ha_interseccion:.4f} m)')
    
    # Agregar líneas punteadas al punto de intersección
    ax1.axvline(x=v_interseccion, color='g', linestyle='--', alpha=0.5)
    ax1.axhline(y=ha_interseccion, color='g', linestyle='--', alpha=0.5)
    
    # Anotar el punto
    ax1.annotate(f'v = {v_interseccion:.4f} m/s\nh = {ha_interseccion:.4f} m',
                xy=(v_interseccion, ha_interseccion),
                xytext=(v_interseccion + 0.15, ha_interseccion + 2),
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Configurar la primera gráfica
ax1.set_xlabel('Velocidad (v) [m/s]', fontsize=11)
ax1.set_ylabel('Altura (h) [m]', fontsize=11)
ax1.set_title('Ha y ha vs Velocidad', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9, loc='best')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(v_min, v_max)

# Ajustar el rango del eje y para mejor visualización
y_min = min(min(ha_valores), min(Ha_valores)) - 2
y_max = max(max(ha_valores), max(Ha_valores)) + 2
ax1.set_ylim(y_min, y_max)

# ========== GRÁFICA 2: ha vs Caudal ==========
ax2.plot(caudales, ha_valores, 'b-', linewidth=2, label='SRC')
ax2.plot(caudales, Ha_valores, 'r-', linewidth=2, label='Ha (Head available)')

# Marcar el punto de intersección si existe
if v_interseccion is not None:
    Q_interseccion = v_interseccion * area
    ax2.plot(Q_interseccion, ha_interseccion, 'go', markersize=12, 
             label=f'Intersección (Q={Q_interseccion:.6f} m³/s, h={ha_interseccion:.4f} m)')
    
    # Agregar líneas punteadas al punto de intersección
    ax2.axvline(x=Q_interseccion, color='g', linestyle='--', alpha=0.5)
    ax2.axhline(y=ha_interseccion, color='g', linestyle='--', alpha=0.5)
    
    # Anotar el punto
    ax2.annotate(f'Q = {Q_interseccion:.6f} m³/s\n({Q_interseccion*1000:.4f} L/s)\nh = {ha_interseccion:.4f} m',
                xy=(Q_interseccion, ha_interseccion),
                xytext=(Q_interseccion + 0.00005, ha_interseccion + 2),
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# Configurar la segunda gráfica
ax2.set_xlabel('Caudal (Q) [m³/s]', fontsize=11)
ax2.set_ylabel('Altura (h) [m]', fontsize=11)
ax2.set_title('Ha y ha vs Caudal', fontsize=12, fontweight='bold')
ax2.legend(fontsize=9, loc='best')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(caudales[0], caudales[-1])
ax2.set_ylim(y_min, y_max)

plt.tight_layout()
plt.show()

# Mostrar información adicional
print("\n" + "="*60)
print("INFORMACIÓN DEL SISTEMA")
print("="*60)
print(f"Diámetro de la tubería: {diametro} m")
print(f"Área de la sección transversal: {area:.6f} m²")
if v_interseccion is not None:
    F_interseccion = calcular_F(v_interseccion)
    print(f"\nFactor de fricción (F) en la intersección: {F_interseccion:.6f}")
    print(f"Reynolds parcial (22706.9 * v): {22706.9 * v_interseccion:.2f}")
