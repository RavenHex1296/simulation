import matplotlib.pyplot as plt


class EulerEstimator():

    def __init__(self, derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self, point):
        return self.derivative(point[0])

    def step_forward(self, point, step_size):
        x = point[0]
        y = point[1]

        return (x + step_size, y + self.calc_derivative_at_point(point) * step_size)

    def calc_estimated_points(self, point, step_size, num_steps):
        estimated_point_list = [point]
        current_point = point

        for n in range(num_steps):
            current_point = self.step_forward(current_point, step_size)
            estimated_point_list.append(current_point)

        return estimated_point_list

    def plot(self, point, step_size, num_steps):
        x_values = [point[0]]
        y_values = [point[1]]

        for n in range(num_steps):
            point = self.step_forward(point, step_size)
            x_values.append(point[0])
            y_values.append(point[1])

        plt.style.use('bmh')
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('Euler-plot.png')
