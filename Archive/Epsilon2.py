import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages  # Import PdfPages

# User input
x_values = np.linspace(0.1, 0.6, 100)
Q2_values = np.linspace(1, 5, 100)

# Set values
E_values = [3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 11]  # GeV
M = 0.938272  # GeV
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'cyan']  # Colors for each E_val

# Open a PDF document
with PdfPages("Epsilon2.pdf") as pdf:
    # Combined plot for Epsilon vs. Scattering Angle
    plt.figure(figsize=(10, 6))
    for idx, E_val in enumerate(E_values):
        theta_degrees = []
        epsilon_values = []
        for x in x_values:
            for Q2 in Q2_values:
                Q2_vs_x = Q2 / x
                nu = Q2 / (2 * M * x)
                Ep = E_val - nu
                if Ep <= 0:
                    continue  # Discarding invalid Ep
                Ep_val = float(Ep)
                arg = Q2 / (4 * E_val * Ep_val)
                if 0 <= arg <= 1:
                    theta_rad = 2 * math.asin(math.sqrt(arg))
                    if 0.0872665 <= theta_rad <= 0.523599:  # Limiting theta_rad range
                        theta_deg = math.degrees(theta_rad)
                    else:
                        continue
                else:
                    continue
                epsilon = (1 + 2 * (1 + Q2 / (4 * M**2 * x**2)) * (math.tan(theta_rad / 2)**2))**(-1)
                theta_degrees.append(theta_deg)
                epsilon_values.append(epsilon)

        # Add data to the combined plot, ensuring each has a label
        plt.scatter(theta_degrees, epsilon_values, color=colors[idx], marker='o', s=5, label=f'E = {E_val} GeV')

        # Create a separate plot for each E_val
        plt.figure(figsize=(10, 6))
        plt.scatter(theta_degrees, epsilon_values, color=colors[idx], marker='o', s=5)
        plt.title(f'Epsilon vs. Scattering Angle for E = {E_val} GeV')
        plt.xlabel('Scattering Angle (degrees)')
        plt.ylabel('Epsilon')
        plt.grid()
        pdf.savefig()  # Save this plot to the PDF
        plt.close()  # Close the individual plot to avoid display overlap

    # Finalize the combined Epsilon plot
    plt.title('Epsilon vs. Scattering Angle (Combined)')
    plt.xlabel('Scattering Angle (degrees)')
    plt.ylabel('Epsilon')
    plt.grid()
    plt.legend(title="Beam Energy")  # Only call legend after plotting labeled data
    pdf.savefig()  # Save the combined plot to the PDF
    plt.close()

    # Combined plot for Q2 vs x
    plt.figure(figsize=(10, 6))
    for idx, E_val in enumerate(E_values):
        Q2_vs_x_values = []
        x_values_for_plot = []
        for x in x_values:
            for Q2 in Q2_values:
                Q2_vs_x = Q2 / x
                nu = Q2 / (2 * M * x)
                Ep = E_val - nu
                if Ep <= 0:
                    continue  # Discarding invalid Ep
                Ep_val = float(Ep)
                arg = Q2 / (4 * E_val * Ep_val)
                if 0 <= arg <= 1:
                    Q2_vs_x_values.append(Q2)
                    x_values_for_plot.append(x)

        # Add data to the combined Q2 vs x plot
        plt.scatter(Q2_vs_x_values, x_values_for_plot, color=colors[idx], marker='o', s=5, label=f'E = {E_val} GeV')

        # Create a separate plot for each E_val
        plt.figure(figsize=(10, 6))
        plt.scatter(Q2_vs_x_values, x_values_for_plot, color=colors[idx], marker='o', s=5)
        plt.title(f'Q2 vs x for E = {E_val} GeV')
        plt.xlabel('Q2')
        plt.ylabel('x')
        plt.grid()
        pdf.savefig()  # Save this plot to the PDF
        plt.close()  # Close the individual plot to avoid display overlap

    # Finalize the combined Q2 vs x plot
    plt.title('Q2 vs x (Combined)')
    plt.xlabel('Q2')
    plt.ylabel('x')
    plt.grid()
    plt.legend(title="Beam Energy")  # Only call legend after plotting labeled data
    pdf.savefig()  # Save the combined plot to the PDF
    plt.close()
