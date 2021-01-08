import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

'''
def derivative(t):
    return t + 1

euler = EulerEstimator(derivative)
print("Asserting class 'EulerEstimator' with x'(t) = t + 1")

print("Asserting method 'calc_derivative_at_point' on (1, 4)")
assert euler.calc_derivative_at_point((1, 4)) == 2
print("PASSED")

print("Asserting method 'step_forward' on (1, 4) with step size 0.5")
assert euler.step_forward((1, 4), 0.5) == (1.5, 5)
print("PASSED")

print("First 4 steps with initial point (1, 4) and step size 0.5: ")
print(euler.calc_estimated_points((1, 4), 0.5, 4))

euler.plot((-5, 10), 0.1, 100)
'''

derivatives = {
        'A': (lambda t, x: x['A'] + 1),
        'B': (lambda t, x: x['A'] + x['B']),
        'C': (lambda t, x: 2 * x['B'])
    }
euler = EulerEstimator(derivatives)
initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)

print("Asserting 'calc_derivative_at_point'")
assert euler.calc_derivative_at_point(initial_point) == {'A': 1, 'B': 0, 'C': 0}, "Incorrect ouput"
print("PASSED")

point_2 = euler.step_forward(initial_point, 0.1)

print("Asserting 'step_forward'")
assert point_2 == (0.1, {'A': 0.1, 'B': 0, 'C': 0}), "Incorrect ouput"
print("PASSED")

print("Asserting 'calc_derivative_at_point'")
assert euler.calc_derivative_at_point(point_2) == {'A': 1.1, 'B': 0.1, 'C': 0}, "Incorrect ouput"
print("PASSED")

point_3 = euler.step_forward(point_2, -0.5)
for key in point_3[1]:
    point_3[1][key] = round(point_3[1][key], 2)

print("Asserting 'step_forward'")
assert point_3 == (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}), "Incorrect ouput"
print("PASSED")

estimated_points = euler.calc_estimated_points(point_3, 2, 3)
for point in estimated_points:
    for key in point[1]:
        point[1][key] = round(point[1][key], 6)

print("Asserting 'calc_estimated_points'")
assert estimated_points == [
   (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}),
   (1.6, {'A': 0.65, 'B': -1.05, 'C': -0.2}),
   (3.6, {'A': 3.95, 'B': -1.85, 'C': -4.4}),
   (5.6, {'A': 13.85, 'B': 2.35, 'C': -11.8})
], "Incorrect ouput"
print("PASSED")


euler.plot(initial_point, 0.01, 5)