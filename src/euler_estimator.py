# import matplotlib.pyplot as plt


class EulerEstimator():

    def __init__(self, derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self, point):
        derivatives = {}

        for key in self.derivative:
            derivatives[key] = self.derivative[key](point[0], point[1])

        return derivatives

    def step_forward(self, point, step_size):
        t = point[0]
        derivatives = self.calc_derivative_at_point(point)
        x = {}

        for key in point[1]:
            x[key] = point[1][key] + derivatives[key] * step_size

        new_point = (t + step_size, x)
        return new_point

    def calc_estimated_points(self, point, step_size, num_steps):
        points = []
        points.append(point)

        for n in range(num_steps):
            current_point = self.step_forward(point, step_size)
            points.append(current_point)
            point = current_point

        return points

'''
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
'''
