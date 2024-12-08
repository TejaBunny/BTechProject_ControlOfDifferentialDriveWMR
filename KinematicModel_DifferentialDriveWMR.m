%% Differential Drive WMR Kinematic Model Simulation

%% Parameters
r = 0.1; % Radius of the wheels
a = 0.5; % Distance between center and robot wheels - meters
v = 1; % linear velocity - m/s
R = 2; % Circular path radius - meters
phi = pi/4; % starting orientation of the robot - radians
x_Q = 0; % Initial X position of the robot - meters
y_Q = 0; % Initial Y position of the robot - meters
dt = 0.01; % Time step in seconds
t_total = 40; % Total simulation time in seconds

%% Initialize arrays for storing positions
t = 0:dt:t_total;
x_Q_arr = zeros(size(t));
y_Q_arr = zeros(size(t));
phi_arr = zeros(size(t));

%% Initial conditions
x_Q_arr(1) = x_Q;
y_Q_arr(1) = y_Q;
phi_arr(1) = phi;

%% Simulation loop
for i = 2:length(t)
    %% Calculate wheel velocities for a circular path
    v_r = v * (1 + a / R);  % Right wheel velocity
    v_l = v * (1 - a / R);  % Left wheel velocity

    %% Calculate velocities
    omega = (v_r - v_l) / (2 * a); % Angular velocity

    %% Update the robot's position
    x_dot_Q = v * cos(phi);  % Velocity in X direction
    y_dot_Q = v * sin(phi);  % Velocity in Y direction
    phi_dot = omega; % Change in orientation

    %% Integrate to get the new position and orientation
    x_Q = x_Q + x_dot_Q * dt;
    y_Q = y_Q + y_dot_Q * dt;
    phi = phi + phi_dot * dt;

    %% Store the results
    x_Q_arr(i) = x_Q;
    y_Q_arr(i) = y_Q;
    phi_arr(i) = phi;
end

%% Plot the trajectory (Circular)
figure;
plot(x_Q_arr, y_Q_arr, 'LineWidth', 2);
xlabel('X Position (m)');
ylabel('Y Position (m)');
title('Trajectory of Differential Drive WMR');
grid on;
axis equal;

%% Set the x and y axis limits
xlim([-5 5]); 
ylim([-5 5]); 

%% Animation of Differential Drive WMR Trajectory

figure;
hold on;
plot(x_Q_arr, y_Q_arr, 'r--'); % Plot the trajectory path
robot_body = plot(x_Q_arr(1), y_Q_arr(1), 'bo', 'MarkerSize', 10, 'MarkerFaceColor', 'b'); % Initial robot body
robot_direction = quiver(x_Q_arr(1), y_Q_arr(1), cos(phi_arr(1)), sin(phi_arr(1)), 0.5, 'k', 'LineWidth', 2); % Robot heading direction
xlabel('X Position (m)');
ylabel('Y Position (m)');
title('Trajectory and Animation of Differential Drive WMR');
grid on;
axis equal;

%% Set the x and y axis limits
xlim([-5 5]); 
ylim([-5 5]); 


%% Animation Loop-- where the robot moves in a circular path with constant speed as there is no force applied
for i = 1:10:length(t)
    % Update the robot's position (blue dot) and direction (quiver for arrow)
    set(robot_body, 'XData', x_Q_arr(i), 'YData', y_Q_arr(i));  % Update robot body position
    set(robot_direction, 'XData', x_Q_arr(i), 'YData', y_Q_arr(i), ...
        'UData', cos(phi_arr(i)), 'VData', sin(phi_arr(i)));    % Update heading direction

    % Pause to create animation effect
    pause(0.01);
end

hold off;

%% The end
