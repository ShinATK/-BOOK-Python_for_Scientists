import numpy as np
from scipy.integrate import odeint
output_result = odeint(lambda y, t:y, 1, [0, 1])
print(output_result)