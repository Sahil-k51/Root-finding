# # import streamlit as st
# # import numpy as np
# # from functions import create_function_from_string, newton_raphson, df

# # # Title of the app
# # st.title('Newton-Raphson Root Finder')

# # # Text box for the user to input the equation
# # equation = st.text_input('Enter your equation f(x) = 0 in terms of x. Example: x**2 - 4*x + 4', 'x**2 - 4*x + 4')

# # # Text box for the user to input the initial guess
# # x0 = st.text_input('Enter initial guess for the root', '2.0')

# # # Button to trigger the root finding process
# # if st.button('Find Root'):
# #     try:
# #         # Convert initial guess to float
# #         x0 = float(x0)
        
# #         # Create the function from the equation string
# #         f = create_function_from_string(equation)
        
# #         # Find the root using Newton-Raphson method
# #         root, errors, steps = newton_raphson(f, lambda x: df(f, x), x0)
        
# #         # Display the root
# #         st.write(f"Root found: x = {root:.6f}")
        
# #         # Provide option to download the root
# #         st.download_button('Download Root', data=str(root), file_name='root.txt')
        
# #     except ValueError as e:
# #         st.error(f"Error: {e}")


# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from io import BytesIO
# from functions import create_function_from_string, newton_raphson, df

# # Title of the app
# st.title('Newton-Raphson Root Finder')

# # Text box for the user to input the equation
# equation = st.text_input('Enter your equation f(x) = 0 in terms of x. Example: x**2 - 4*x + 4', 'x**2 - 4*x + 4')

# # Text box for the user to input the initial guess
# x0 = st.text_input('Enter initial guess for the root', '2.0')

# # Button to trigger the root finding process
# if st.button('Find Root'):
#     try:
#         # Convert initial guess to float
#         x0 = float(x0)
        
#         # Create the function from the equation string
#         f = create_function_from_string(equation)
        
#         # Find the root using Newton-Raphson method
#         root, errors, steps = newton_raphson(f, lambda x: df(f, x), x0)
        
#         # Display the root
#         st.write(f"Root found: x = {root:.6f}")
        
#         # Plot the function and the root
#         x_vals = np.linspace(root - 10, root + 10, 400)
#         y_vals = f(x_vals)
        
#         fig, ax = plt.subplots()
#         ax.plot(x_vals, y_vals, label='f(x)')
#         ax.axhline(0, color='black', linewidth=0.5)
#         ax.axvline(root, color='red', linestyle='--', label=f'Root at x = {root:.6f}')
#         ax.set_title('Graph of the function and its Newton-Raphson Root')
#         ax.set_xlabel('x')
#         ax.set_ylabel('f(x)')
#         ax.legend()
#         ax.grid(True)
        
#         # Display the plot
#         st.pyplot(fig)
        
#         # Save the plot to a buffer
#         buf = BytesIO()
#         fig.savefig(buf, format='png')
#         buf.seek(0)
        
#         # Provide option to download the plot
#         st.download_button('Download Plot', data=buf, file_name='function_plot.png', mime='image/png')
        
#         # Provide option to download the root
#         st.download_button('Download Root', data=str(root), file_name='root.txt')
        
#     except ValueError as e:
#         st.error(f"Error: {e}")


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from functions import create_function_from_string, newton_raphson, df, animate_newton_raphson

# Title of the app
st.title('Newton-Raphson Root Finder')

# Text box for the user to input the equation
equation = st.text_input('Enter your equation f(x) = 0 in terms of x. Example: x**2 - 4*x + 4', 'x**2 - 4*x + 4')

# Text box for the user to input the initial guess
x0 = st.text_input('Enter initial guess for the root', '2.0')

# Button to trigger the root finding process
if st.button('Find Root'):
    try:
        # Convert initial guess to float
        x0 = float(x0)
        
        # Create the function from the equation string
        f = create_function_from_string(equation)
        
        # Find the root using Newton-Raphson method
        root, errors, steps = newton_raphson(f, lambda x: df(f, x), x0)
        
        # Display the root
        st.write(f"Root found: x = {root:.6f}")
        
        # Plot the function and the root
        x_vals = np.linspace(root - 10, root + 10, 400)
        y_vals = f(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='f(x)')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(root, color='red', linestyle='--', label=f'Root at x = {root:.6f}')
        ax.set_title('Graph of the function and its Newton-Raphson Root')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)
        
        # Display the plot
        st.pyplot(fig)
        
        # Save the plot to a buffer
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        
        # Provide option to download the plot
        st.download_button('Download Plot', data=buf, file_name='function_plot.png', mime='image/png')
        
        # Provide option to download the root
        st.download_button('Download Root', data=str(root), file_name='root.txt')

        # Create and display the animation
        video_path = animate_newton_raphson(f, steps)
        
        # Display the video in the app
        video_file = open(video_path, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
        # Provide option to download the video
        st.download_button('Download Video', data=video_bytes, file_name='newton_raphson_animation.mp4', mime='video/mp4')
        
    except ValueError as e:
        st.error(f"Error: {e}")
