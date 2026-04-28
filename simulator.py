from utils import calculate_drag, calculate_lift, get_cl_from_angle

print("=== Aerodynamics Simulator ===")

velocity = float(input("Velocity (m/s): "))
wing_area = float(input("Wing Area: "))
Cd = float(input("Drag Coefficient: "))
angle = float(input("Angle of Attack (degrees): "))

Cl = get_cl_from_angle(angle)

drag = calculate_drag(velocity, wing_area, Cd)
lift = calculate_lift(velocity, wing_area, Cl)

print("\nResults:")
print(f"Lift: {lift:.2f} N")
print(f"Drag: {drag:.2f} N")

if lift > drag:
    print("Efficient Flight Condition")
else:
    print("Inefficient Design")
from utils import calculate_drag, calculate_lift

print("=== Aerodynamics Simulator ===")

velocity = float(input("Velocity (m/s): "))
wing_area = float(input("Wing Area: "))
Cd = float(input("Drag Coefficient: "))
Cl = float(input("Lift Coefficient: "))

drag = calculate_drag(velocity, wing_area, Cd)
lift = calculate_lift(velocity, wing_area, Cl)

print("\nResults:")
print(f"Lift: {lift:.2f} N")
print(f"Drag: {drag:.2f} N")
