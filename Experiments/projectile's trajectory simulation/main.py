import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile_trajectory(initial_velocity, launch_angle_degrees, time_step=0.01):
    """
    Simulates the trajectory of a projectile launched from the origin.

    Args:
        initial_velocity (float): The initial speed of the projectile in m/s.
        launch_angle_degrees (float): The launch angle in degrees from the horizontal.
        time_step (float): The time increment for the simulation in seconds.

    Returns:
        tuple: A tuple containing two numpy arrays: (time_points, x_positions, y_positions).
               Returns (None, None, None) if the projectile never leaves the ground.
    """
    g = 9.81  # Acceleration due to gravity in m/s^2

    # Convert launch angle from degrees to radians
    launch_angle_radians = np.deg2rad(launch_angle_degrees)

    # Calculate initial velocity components
    vx0 = initial_velocity * np.cos(launch_angle_radians)
    vy0 = initial_velocity * np.sin(launch_angle_radians)

    # Initialize lists to store trajectory data
    time_points = [0]
    x_positions = [0]
    y_positions = [0]

    # Current state variables
    current_x = 0
    current_y = 0
    current_vx = vx0
    current_vy = vy0
    current_time = 0

    # Simulate until the projectile hits or goes below the ground (y <= 0)
    # or if it's launched horizontally and has no initial vertical velocity.
    if vy0 <= 0 and launch_angle_degrees < 90: # Only if launched horizontally or downwards
        print("Projectile immediately hits or remains on the ground.")
        return None, None, None

    while current_y >= 0:
        current_time += time_step

        # Update velocities (only y-component changes due to gravity)
        # Note: For simplicity, we're using Euler integration here, which is basic.
        # For more accuracy, especially with varying forces, more advanced methods
        # like Runge-Kutta would be used.
        current_vy -= g * time_step

        # Update positions
        current_x += current_vx * time_step
        current_y += current_vy * time_step

        # Append data to lists
        time_points.append(current_time)
        x_positions.append(current_x)
        # Ensure y doesn't go significantly negative due to time_step overshoot
        y_positions.append(max(0, current_y))

        # Break if it has gone significantly below ground to avoid floating point issues
        if current_y < -0.1 and len(time_points) > 1: # Some tolerance for floating point
            break


    return np.array(time_points), np.array(x_positions), np.array(y_positions)

def plot_trajectory(time_points, x_positions, y_positions, initial_velocity, launch_angle_degrees):
    """
    Plots the simulated projectile trajectory.
    """
    if x_positions is None: # Handle cases where simulation didn't run
        print("No trajectory to plot.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(x_positions, y_positions, label='Projectile Trajectory', color='blue')
    plt.scatter(0, 0, color='red', zorder=5, label='Launch Point') # Launch point

    # Add peak of trajectory
    peak_y_idx = np.argmax(y_positions)
    peak_x = x_positions[peak_y_idx]
    peak_y = y_positions[peak_y_idx]
    plt.scatter(peak_x, peak_y, color='green', zorder=5, label=f'Peak ({peak_x:.2f}m, {peak_y:.2f}m)')
    plt.text(peak_x, peak_y + 0.5, f'Max H: {peak_y:.2f}m', ha='center', va='bottom')

    # Add landing point (if it landed above 0)
    if y_positions[-1] <= 0 and len(x_positions) > 1:
        landing_x = x_positions[-1]
        plt.scatter(landing_x, 0, color='orange', zorder=5, label=f'Landing Point ({landing_x:.2f}m)')
        plt.text(landing_x, -0.5, f'Range: {landing_x:.2f}m', ha='center', va='top')


    plt.title(f'Projectile Trajectory Simulation (V0={initial_velocity} m/s, Angle={launch_angle_degrees}°)')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.8) # Ground line
    plt.axvline(0, color='black', linewidth=0.8) # Y-axis
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box') # Make scales equal for better visualization
    plt.show()

# --- Main execution ---
if __name__ == "__main__":
    # Example 1: Standard launch
    print("--- Simulation 1: Standard Launch ---")
    initial_vel1 = 50  # m/s
    launch_angle1 = 45 # degrees
    times1, xs1, ys1 = simulate_projectile_trajectory(initial_vel1, launch_angle1)
    plot_trajectory(times1, xs1, ys1, initial_vel1, launch_angle1)

    # Example 2: Higher velocity, lower angle
    print("\n--- Simulation 2: Higher Velocity, Lower Angle ---")
    initial_vel2 = 100 # m/s
    launch_angle2 = 30 # degrees
    times2, xs2, ys2 = simulate_projectile_trajectory(initial_vel2, launch_angle2)
    plot_trajectory(times2, xs2, ys2, initial_vel2, launch_angle2)

    # Example 3: Very low angle
    print("\n--- Simulation 3: Very Low Angle ---")
    initial_vel3 = 30 # m/s
    launch_angle3 = 5  # degrees
    times3, xs3, ys3 = simulate_projectile_trajectory(initial_vel3, launch_angle3)
    plot_trajectory(times3, xs3, ys3, initial_vel3, launch_angle3)

    # Example 4: Edge case - launched horizontally (should hit ground immediately)
    print("\n--- Simulation 4: Horizontal Launch (Edge Case) ---")
    initial_vel4 = 20 # m/s
    launch_angle4 = 0  # degrees
    times4, xs4, ys4 = simulate_projectile_trajectory(initial_vel4, launch_angle4)
    if xs4 is None:
        print("Simulation correctly indicated no trajectory.")
    plot_trajectory(times4, xs4, ys4, initial_vel4, launch_angle4)