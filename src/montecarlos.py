from simulation import simulate_queue
import numpy as np


def montecarlo_simulation(runs, num_servers, arrival_rate, service_rate, simulation_time):
    times = []
    utilisations = []
    for _ in range(runs):
        time_in_system, util = simulate_queue(num_servers, arrival_rate, service_rate, simulation_time)
        times.append(time_in_system)
        utilisations.append(util)

    mean_time = np.mean(times)
    mean_utilisation = np.mean(utilisations)

    return mean_time, mean_utilisation
