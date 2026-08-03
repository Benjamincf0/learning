import numpy as np
from ax.api.client import Client
from ax.api.configs import RangeParameterConfig


client = Client()

# Define six float parameters x1, x2, x3, ... for the Hartmann6 function, which is typically evaluated on the unit hypercube
parameters = [
    RangeParameterConfig(
        name="x1", parameter_type="float", bounds=(0, 1)
    ),
    RangeParameterConfig(
        name="x2", parameter_type="float", bounds=(0, 1)
    ),
    RangeParameterConfig(
        name="x3", parameter_type="float", bounds=(0, 1)
    ),
    RangeParameterConfig(
        name="x4", parameter_type="float", bounds=(0, 1)
    ),
    RangeParameterConfig(
        name="x5", parameter_type="float", bounds=(0, 1)
    ),
    RangeParameterConfig(
        name="x6", parameter_type="float", bounds=(0, 1)
    ),
]

client.configure_experiment(parameters=parameters)

metric_name = "hartmann6" # this name is used during the optimization loop in Step 5
objective = f"-{metric_name}" # minimization is specified by the negative sign

client.configure_optimization(objective=objective)

# Hartmann6 function
def hartmann6(x1, x2, x3, x4, x5, x6):
    alpha = np.array([1.0, 1.2, 3.0, 3.2])
    A = np.array([
        [10, 3, 17, 3.5, 1.7, 8],
        [0.05, 10, 17, 0.1, 8, 14],
        [3, 3.5, 1.7, 10, 17, 8],
        [17, 8, 0.05, 10, 0.1, 14]
    ])
    P = 10**-4 * np.array([
        [1312, 1696, 5569, 124, 8283, 5886],
        [2329, 4135, 8307, 3736, 1004, 9991],
        [2348, 1451, 3522, 2883, 3047, 6650],
        [4047, 8828, 8732, 5743, 1091, 381]
    ])

    outer = 0.0
    for i in range(4):
        inner = 0.0
        for j, x in enumerate([x1, x2, x3, x4, x5, x6]):
            inner += A[i, j] * (x - P[i, j])**2
        outer += alpha[i] * np.exp(-inner)
    return -outer

hartmann6(0.1, 0.45, 0.8, 0.25, 0.552, 1.0)

for _ in range(10): # Run 10 rounds of trials
    # We will request three trials at a time in this example
    trials = client.get_next_trials(max_trials=3)

    for trial_index, parameters in trials.items():
        x1 = parameters["x1"]
        x2 = parameters["x2"]
        x3 = parameters["x3"]
        x4 = parameters["x4"]
        x5 = parameters["x5"]
        x6 = parameters["x6"]

        result = hartmann6(x1, x2, x3, x4, x5, x6)

        # Set raw_data as a dictionary with metric names as keys and results as values
        raw_data = {metric_name: result}

        # Complete the trial with the result
        client.complete_trial(trial_index=trial_index, raw_data=raw_data)

best_parameters, prediction, index, name = client.get_best_parameterization()
print("Best Parameters:", best_parameters)
print("Prediction (mean, variance):", prediction)

# display=True instructs Ax to sort then render the resulting analyses
cards = client.compute_analyses(display=True)
