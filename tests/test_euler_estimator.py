import sys
sys.path.append('src')
from euler_estimator import EulerEstimator


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
