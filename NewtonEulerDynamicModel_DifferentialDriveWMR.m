% Parameters
m = 5;          % mass of WMR (kg)
I = 0.1;        % moment of inertia (kg*m^2)
r = 0.05;       % radius of wheels (m)
a = 0.2;        % half of the distance between wheels (m)
dt = 0.001;      % time step (s)
t_final = 5;   % total simulation time (s)

% Initial conditions
x = 0;          %  x-position (m)
y = 0;          %  y-position (m)
theta = 0;      % orientation (rad)
v = 0;          %  linear velocity (m/s)
omega = 0;      %  angular velocity (rad/s)

% Time vector
t = 0:dt:t_final;

% Trajectory storage
x_traj = zeros(size(t));
y_traj = zeros(size(t));
theta_traj = zeros(size(t));

% Control inputs (torques)
tau_R = 1; % Right (Nm)
tau_L = .8; % Left (Nm)

% Simulation loop
for i = 1:length(t)
  
    v_dot = (1/(m*r)) * (tau_R + tau_L);  % linear acceleration
    omega_dot = (2*a/(I*r)) * (tau_R - tau_L);  % angular acceleration
    
    % Update velocities, position and orientation
    v = v + v_dot * dt;
    omega = omega + omega_dot * dt;
    
    x = x + v * cos(theta) * dt;
    y = y + v * sin(theta) * dt;
    theta = theta + omega * dt;
    
    % Store trajectory
    x_traj(i) = x;
    y_traj(i) = y;
    theta_traj(i) = theta;
end



% Animation of the WMR -- where the robot moves in a circular path with
% improving speed due to the application of torque
figure;
for i = 1:10:length(t)
    clf;
    hold on;
    % Plot the WMR as a rectangle
    WMR_width = 2*a;
    WMR_length = 0.3;
    WMR_shape = [-WMR_length/2, WMR_length/2, WMR_length/2, -WMR_length/2;
                 -WMR_width/2, -WMR_width/2, WMR_width/2, WMR_width/2];
    R = [cos(theta_traj(i)), -sin(theta_traj(i)); sin(theta_traj(i)), cos(theta_traj(i))];
    WMR_rotated = R * WMR_shape;
    fill(WMR_rotated(1,:) + x_traj(i), WMR_rotated(2,:) + y_traj(i), 'g');
    
    % Plot the trajectory
    plot(x_traj(1:i), y_traj(1:i), 'r', 'LineWidth', 1.5);
    
    % Formatting the plot
    axis equal;
    xlim([-2, 2]);
    ylim([-2, 2]);
    xlabel('X position (m)');
    ylabel('Y position (m)');
    title('WMR Animation');
    grid on;
    
    pause(0.01);
end
