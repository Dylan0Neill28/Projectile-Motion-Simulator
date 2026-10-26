
Projectile Motion Tracker with Dynamic Gravity

A Python-based 2D projectile motion simulation that calculates and visualizes trajectories using explicit numerical step integration.
Unlike standard ideal kinematic simulators that assume a constant acceleration, this implementation dynamically evaluates Newton's Law of Universal Gravitation at every discrete altitude step along the flight path.

🚀 Features

• Dynamic Gravity Field Calculation: Recomputes local gravitational acceleration (\(g\)) at every time step based on the projectile's instantaneous altitude relative to the Earth's center.
• Numerical Integration Loop: Utilizes a custom time-step iterator (\(\Delta t = 10^{-5}\text{ s}\)) to track coordinate variations until ground impact (\(y \le 0\)).
• Vector Component Resolution: Automatically breaks down the user's initial launch speed and angle into independent orthogonal horizontal (\(x\)) and vertical (\(y\)) telemetry arrays.
• Visual Telemetry Plotting: Generates a high-fidelity position graph using Matplotlib to inspect the geometric path.

📊 Physical Parameters Modelled

The script initializes with real-world geophysical constants alongside customizable kinematic launch states:

Parameter	Symbol	Baseline Script Value	Description
Gravitational Constant	\(G\)	\(6.6743 \times 10^{-11} \text{ m}^3\text{kg}^{-1}\text{s}^{-2}\)	Universal constant of attraction
Earth Mass	\(M\)	\(5.9722 \times 10^{24} \text{ kg}\)	Mass of the attracting planetary body
Earth Radius	\(R\)	\(6.371 \times 10^6 \text{ m}\)	Planetary boundary distance from center
Launch Speed	\(v_{0}\)	\(7 \text{ m/s}\)	Initial absolute velocity magnitude
Initial Elevation	\(y_{0}\)	\(6 \text{ m}\)	Starting altitude above sea level
Launch Angle	\(d\)	\(45^{\circ }\)	Elevation angle relative to the horizontal plain


🛠️ Code Architecture

The simulator structure uses specialized subroutines to resolve position points:
• gravity(h, G, M, R): Evaluates \(\frac{G\cdot M}{(h+R)^{2}}\) to determine local acceleration at altitude \(h\).
• x_start_velocity(r) / y_start_velocity(r): Resolves initial velocity vectors using trigonometric projections.
• x_t(vx0, t) / y_t(y0, vy0, t, G): Kinematic state equations executed across compiled scalar and array data sets.
• while True loop: Core conditional integration structure that monitors ground proximity constraints and records time step markers.

💻 Setup & Execution


Prerequisites

Ensure your local Python ecosystem has NumPy and Matplotlib installed:
bash
pip install numpy matplotlib
Use code with caution.

Running the Simulator

Execute the script from your development terminal or within an IDE:
bash
python simulation.py
Use code with caution.
Would you like to extend this README by adding a Contributions / Issues section, or should we include a "Known Limitations" note regarding how the script uses real-world planetary gravity for small, low-velocity scale bounds (\(7\text{ m/s}\) at \(6\text{ m}\))?
