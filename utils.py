rho = 1.225

def calculate_drag(v, A, Cd):
    return 0.5 * rho * v**2 * A * Cd

def calculate_lift(v, A, Cl):
    return 0.5 * rho * v**2 * A * Cl

def get_cl_from_angle(angle):
    if angle <= 12:
        return 0.1 * angle
    else:
        return 1.2 - 0.1 * (angle - 12)
