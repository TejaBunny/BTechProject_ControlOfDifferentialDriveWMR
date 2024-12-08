# Currently working on my final year project which involves controlling a non-holonomic robot in different scenarios
## Developed Kinematic and Dynamic model for a Differential Drive Wheeled Mobile Robot (Non-holonomic)
### Kinematic model
This model is executed when there is no forces around the robot. We give left and right wheel angular velocities as input to the model. 
We get linear and angular velocities of the robot as output, with the help of Jacobian method.
### Dynamic model (Newton-Euler Dynamic Model)
This model is executed when there are forces around the robot. Here, we consider left and right wheel torques as input. We get linear and angular acceleration of the robot as output using Newton-Euler Dynamic Model Equations.
## Developed Fuzzy rule control in Python, by executing 25 fuzzy rules for each wheel
The main objective is for the robot to reach a moving target in a free environment. Robot maintains it's wheel velocities according to the relative position of target in every minute time step, by considering fuzzy rules. After finally reaching the target, the movement loop gets terminated.
