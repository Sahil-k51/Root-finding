# import numpy as np

# def create_function_from_string(equation):
#     # Safe list of functions and constants
#     allowed_functions = {
#         'sin': np.sin,
#         'cos': np.cos,
#         'tan': np.tan,
#         'log': np.log,
#         'exp': np.exp,
#         'sqrt': np.sqrt,
#         'power': np.power,
#         'pi': np.pi,
#         'e': np.e
#     }

#     # Cleaning and checking the input
#     equation = equation.replace('^', '**')  # Replace ^ with ** for power operation

#     # Defining a function that evaluates the input equation
#     def fx_equal_0(x):
#         try:
#             # Evaluating the equation safely
#             return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
#         except Exception as e:
#             print(f"Error in evaluating the equation: {e}")
#             return None

#     return fx_equal_0

# def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
#     x = x0
#     steps = [(x, f(x))]
#     errors = []
#     for i in range(max_iter):
#         fx = f(x)
#         dfx = df(x)
#         if abs(fx) < tol:
#             return x, errors, steps
#         if dfx == 0:
#             raise ValueError("Derivative is zero. No solution found.")
#         x_new = x - fx / dfx
#         steps.append((x_new, f(x_new)))
#         errors.append(abs(x_new - x))
#         x = x_new
#     raise ValueError("Maximum iterations exceeded. No solution found.")

# def df(f, x):
#     h = 1e-6  # Small step size
#     return (f(x + h) - f(x)) / h


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def create_function_from_string(equation):
    # Safe list of functions and constants
    allowed_functions = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'power': np.power,
        'pi': np.pi,
        'e': np.e
    }

    # Cleaning and checking the input
    equation = equation.replace('^', '**')  # Replace ^ with ** for power operation

    # Defining a function that evaluates the input equation
    def fx_equal_0(x):
        try:
            # Evaluating the equation safely
            return eval(equation, {"__builtins__": None}, {**allowed_functions, 'x': x})
        except Exception as e:
            print(f"Error in evaluating the equation: {e}")
            return None

    return fx_equal_0

def newton_raphson(f, df, x0, tol=1e-8, max_iter=1000):
    x = x0
    steps = [(x, f(x))]
    errors = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, errors, steps
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        steps.append((x_new, f(x_new)))
        errors.append(abs(x_new - x))
        x = x_new
    raise ValueError("Maximum iterations exceeded. No solution found.")

def df(f, x):
    h = 1e-6  # Small step size
    return (f(x + h) - f(x)) / h

def animate_newton_raphson(f, steps):
    fig, ax = plt.subplots(figsize=(12, 8))  # Increased figure size for better visibility
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.axhline(0, color='black', linewidth=0.5)
    
    line, = ax.plot([], [], 'ro-', label='Newton-Raphson steps')
    point, = ax.plot([], [], 'bo', label='Current point')
    
    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point
    
    def update(frame):
        x_data, y_data = zip(*steps[:frame+1])
        line.set_data(x_data, y_data)
        point.set_data(x_data[-1], y_data[-1])
        return line, point
    
    ani = FuncAnimation(fig, update, frames=len(steps), init_func=init, blit=True, repeat=False)
    
    # Save the animation as a video file
    writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)  # Adjust fps for slower iteration
    video_path = "newton_raphson_animation.mp4"
    ani.save(video_path, writer=writer)
    
    return video_path
