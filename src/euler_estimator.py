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
        print(point)

        for n in range(num_steps):
            print(self.step_forward(point, step_size))
            point = self.step_forward(point, step_size)

        return
