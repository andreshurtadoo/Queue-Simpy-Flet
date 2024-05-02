import simpy

def simulate_queue(num_servers, arrival_rate, service_rate, simulation_time):
    env = simpy.Environment()
    servers = simpy.Resource(env, capacity=num_servers)
    times_in_system = []
    server_utilization = [0] * num_servers  # Tiempo que cada servidor ha estado ocupado

    def customer(env, name, servers):
        arrival_time = env.now
        with servers.request() as request:
            yield request
            start_service_time = env.now
            yield env.timeout(1 / service_rate)
            times_in_system.append(env.now - arrival_time)
            server_index = servers.users.index(request)
            server_utilization[server_index] += env.now - start_service_time

    def customer_arrival(env, servers):
        i = 0
        while True:
            yield env.timeout(1 / arrival_rate)
            env.process(customer(env, f"Cliente {i}", servers))
            i += 1

    env.process(customer_arrival(env, servers))
    env.run(until=simulation_time)

    # Calcular métricas
    average_time_in_system = sum(times_in_system) / len(times_in_system)
    total_service_time = sum(server_utilization)
    utilization = total_service_time / (num_servers * simulation_time)
    return average_time_in_system, utilization
