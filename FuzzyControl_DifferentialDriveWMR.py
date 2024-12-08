import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pygame

# Define fuzzy variables
angle_error = ctrl.Antecedent(np.arange(-1, 1, 0.1), 'angle_error')
distance_error = ctrl.Antecedent(np.arange(0, 7, 0.5), 'distance_error')
left_velocity = ctrl.Consequent(np.arange(0, 8, 1), 'left_velocity')
right_velocity = ctrl.Consequent(np.arange(0, 8, 1), 'right_velocity')

# Define membership functions for angle_error
angle_error['SN'] = fuzz.trimf(angle_error.universe, [-1, -1, -0.5])
angle_error['N'] = fuzz.trimf(angle_error.universe, [-1, -0.5, 0])
angle_error['Z'] = fuzz.trimf(angle_error.universe, [-0.5, 0, 0.5])
angle_error['P'] = fuzz.trimf(angle_error.universe, [0, 0.5, 1])
angle_error['BP'] = fuzz.trimf(angle_error.universe, [0.5, 1, 1])

# Define membership functions for distance_error
distance_error['Z'] = fuzz.trimf(distance_error.universe, [0, 0, 1.75])
distance_error['N'] = fuzz.trimf(distance_error.universe, [0, 1.75, 3.5])
distance_error['M'] = fuzz.trimf(distance_error.universe, [1.75, 3.5, 5.25])
distance_error['F'] = fuzz.trimf(distance_error.universe, [3.5, 5.25, 7])
distance_error['VF'] = fuzz.trimf(distance_error.universe, [5.25, 7, 7])





left_velocity['VS'] = fuzz.trimf(left_velocity.universe, [0,0,2])
left_velocity['S'] = fuzz.trimf(left_velocity.universe, [0,2,4])
left_velocity['M'] = fuzz.trimf(left_velocity.universe, [2,4,6])
left_velocity['F'] = fuzz.trimf(left_velocity.universe, [4,6,8])
left_velocity['VF'] = fuzz.trimf(left_velocity.universe, [6,8,8])

right_velocity['VS'] = fuzz.trimf(right_velocity.universe, [0,0,2])
right_velocity['S'] = fuzz.trimf(right_velocity.universe, [0,2,4])
right_velocity['M'] = fuzz.trimf(right_velocity.universe, [2,4,6])
right_velocity['F'] = fuzz.trimf(right_velocity.universe, [4,6,8])
right_velocity['VF'] = fuzz.trimf(right_velocity.universe, [6,8,8])

# Define fuzzy rules based on the table for right_velocity
right_rules = [
    ctrl.Rule(angle_error['SN'] & distance_error['VF'], right_velocity['M']),
    ctrl.Rule(angle_error['SN'] & distance_error['F'], right_velocity['S']),
    ctrl.Rule(angle_error['SN'] & distance_error['M'], right_velocity['VS']),
    ctrl.Rule(angle_error['SN'] & distance_error['N'], right_velocity['VS']),
    ctrl.Rule(angle_error['SN'] & distance_error['Z'], right_velocity['VS']),
    ctrl.Rule(angle_error['N'] & distance_error['VF'], right_velocity['F']),
    ctrl.Rule(angle_error['N'] & distance_error['F'], right_velocity['M']),
    ctrl.Rule(angle_error['N'] & distance_error['M'], right_velocity['S']),
    ctrl.Rule(angle_error['N'] & distance_error['N'], right_velocity['VS']),
    ctrl.Rule(angle_error['N'] & distance_error['Z'], right_velocity['VS']),
    ctrl.Rule(angle_error['Z'] & distance_error['VF'], right_velocity['VF']),
    ctrl.Rule(angle_error['Z'] & distance_error['F'], right_velocity['F']),
    ctrl.Rule(angle_error['Z'] & distance_error['M'], right_velocity['M']),
    ctrl.Rule(angle_error['Z'] & distance_error['N'], right_velocity['S']),
    ctrl.Rule(angle_error['Z'] & distance_error['Z'], right_velocity['VS']),
    ctrl.Rule(angle_error['P'] & distance_error['VF'], right_velocity['VF']),
    ctrl.Rule(angle_error['P'] & distance_error['F'], right_velocity['F']),
    ctrl.Rule(angle_error['P'] & distance_error['M'], right_velocity['M']),
    ctrl.Rule(angle_error['P'] & distance_error['N'], right_velocity['S']),
    ctrl.Rule(angle_error['P'] & distance_error['Z'], right_velocity['S']),
    ctrl.Rule(angle_error['BP'] & distance_error['VF'], right_velocity['VF']),
    ctrl.Rule(angle_error['BP'] & distance_error['F'], right_velocity['F']),
    ctrl.Rule(angle_error['BP'] & distance_error['M'], right_velocity['M']),
    ctrl.Rule(angle_error['BP'] & distance_error['N'], right_velocity['M']),
    ctrl.Rule(angle_error['BP'] & distance_error['Z'], right_velocity['M']),
]

# Mirror rules for left_velocity to simulate symmetric behavior
left_rules = [
    ctrl.Rule(angle_error['SN'] & distance_error['VF'], left_velocity['VF']),
    ctrl.Rule(angle_error['SN'] & distance_error['F'], left_velocity['F']),
    ctrl.Rule(angle_error['SN'] & distance_error['M'], left_velocity['M']),
    ctrl.Rule(angle_error['SN'] & distance_error['N'], left_velocity['M']),
    ctrl.Rule(angle_error['SN'] & distance_error['Z'], left_velocity['M']),
    ctrl.Rule(angle_error['N'] & distance_error['VF'], left_velocity['VF']),
    ctrl.Rule(angle_error['N'] & distance_error['F'], left_velocity['F']),
    ctrl.Rule(angle_error['N'] & distance_error['M'], left_velocity['M']),
    ctrl.Rule(angle_error['N'] & distance_error['N'], left_velocity['S']),
    ctrl.Rule(angle_error['N'] & distance_error['Z'], left_velocity['VS']),
    ctrl.Rule(angle_error['Z'] & distance_error['VF'], left_velocity['VF']),
    ctrl.Rule(angle_error['Z'] & distance_error['F'], left_velocity['F']),
    ctrl.Rule(angle_error['Z'] & distance_error['M'], left_velocity['M']),
    ctrl.Rule(angle_error['Z'] & distance_error['N'], left_velocity['S']),
    ctrl.Rule(angle_error['Z'] & distance_error['Z'], left_velocity['VS']),
    ctrl.Rule(angle_error['P'] & distance_error['VF'], left_velocity['F']),
    ctrl.Rule(angle_error['P'] & distance_error['F'], left_velocity['S']),
    ctrl.Rule(angle_error['P'] & distance_error['M'], left_velocity['VS']),
    ctrl.Rule(angle_error['P'] & distance_error['N'], left_velocity['VS']),
    ctrl.Rule(angle_error['P'] & distance_error['Z'], left_velocity['VS']),
    ctrl.Rule(angle_error['BP'] & distance_error['VF'], left_velocity['M']),
    ctrl.Rule(angle_error['BP'] & distance_error['F'], left_velocity['S']),
    ctrl.Rule(angle_error['BP'] & distance_error['M'], left_velocity['VS']),
    ctrl.Rule(angle_error['BP'] & distance_error['N'], left_velocity['VS']),
    ctrl.Rule(angle_error['BP'] & distance_error['Z'], left_velocity['VS']),
]

# Define control systems and create simulations
control_system = ctrl.ControlSystem(right_rules + left_rules)
fuzzy_controller = ctrl.ControlSystemSimulation(control_system)

# Simulation with grid
def run_robot_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Wheeled Mobile Robot Simulation with Moving Target and Grid')
    clock = pygame.time.Clock()

    # Initial robot and target positions
    robot_pos = np.array([100.0, 100.0])
    target_center = np.array([400.0, 300.0])
    target_radius = 150.0
    angle = 0.0
    max_speed = 7.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        target_pos = target_center + target_radius * np.array([np.cos(angle), np.sin(angle)])
        angle += 0.015

        distance = np.linalg.norm(target_pos - robot_pos)
        angle_to_target = np.arctan2(target_pos[1] - robot_pos[1], target_pos[0] - robot_pos[0])

        angle_error_input = np.clip((angle_to_target - np.pi/4) / (np.pi/2), -1, 1)
        distance_error_input = np.clip(distance / 10, 0, 7)
        
        fuzzy_controller.input['angle_error'] = angle_error_input
        fuzzy_controller.input['distance_error'] = distance_error_input
        fuzzy_controller.compute()

        left_speed = fuzzy_controller.output.get('left_velocity', 0)
        right_speed = fuzzy_controller.output.get('right_velocity', 0)
        
        speed = (left_speed + right_speed) / 2
        angle_change = (right_speed - left_speed) / max_speed

        robot_pos += np.array([np.cos(angle_to_target) * speed, np.sin(angle_to_target) * speed])

        if distance < 10:
            print("Target reached!")
            break

        screen.fill((255, 255, 255))

        # Draw grid
        for x in range(0, 800, 20):
            pygame.draw.line(screen, (220, 220, 220), (x, 0), (x, 600))
        for y in range(0, 600, 20):
            pygame.draw.line(screen, (220, 220, 220), (0, y), (800, y))

        # Draw robot and target
        pygame.draw.circle(screen, (0, 255, 0), target_pos.astype(int), 10)
        pygame.draw.circle(screen, (0, 0, 255), robot_pos.astype(int), 10)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

run_robot_simulation()
