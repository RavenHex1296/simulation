import matplotlib.pyplot as plt


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
        x = {key:point[1][key] + derivatives[key] * step_size for key in point[1]}
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

    def plot(self, point, step_size, end_value):
        t_values = []
        step_values = {}
        plt.style.use('bmh')

        for key in point[1]:
            step_values[key] = []

        while True:
            if point[0] > end_value:
                break

            for key in point[1]:
                step_values[key].append(point[1][key])

            t_values.append(point[0])
            point = self.step_forward(point, step_size)

        for key in step_values:
            plt.plot(t_values, step_values[key])

        plt.savefig('Euler-plot.png')
