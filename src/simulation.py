import simpy


def simulate_queue(num_servers, arrival_rate, service_rate, simulation_time):
    """ Simula un sistema de colas con múltiples servidores.

    Args:x
        num_servers (int): Número de servidores en el sistema.
        arrival_rate (float): Tasa de llegada de clientes.
        service_rate (float): Tasa de servicio por servidor.
        simulation_time (int): Tiempo total de simulación.

        customers_waiting: Almacena los clientes que están esperando servicio.
        customers_in_service: Almacena los clientes que están siendo atendidos.
        customers_done: Almacena los clientes que han sido atendidos.
    """
    env = simpy.Environment()
    servers = simpy.Resource(env, capacity=num_servers)
    customers_in_service = []
    customers_waiting = []
    customers_done = []

    def print_status():
        print(f"Tiempo {env.now:.2f}: "
              f"En Espera - {[c for c in customers_waiting]}, "
              f"Atendiendo - {[c for c in customers_in_service]}, "
              f"Ya Atendidos - {[c for c in customers_done]}")

    def customer_arrival(env, servers):
        i = 0
        while True:
            yield env.timeout(1 / arrival_rate)
            customer_name = f"Cliente {i}"
            customers_waiting.append(customer_name)
            env.process(customer_service(env, servers, customer_name))
            print_status()
            i += 1

    def customer_service(env, servers, name):
        with servers.request() as request:
            yield request
            customers_in_service.append(name)
            customers_waiting.remove(name)  # direct removal by name
            yield env.timeout(1 / service_rate)
            customers_in_service.remove(name)
            customers_done.append(name)
            print_status()

    env.process(customer_arrival(env, servers))
    env.run(until=simulation_time)


# Ejemplo de uso
if __name__ == "__main__":
    simulate_queue(num_servers=2, arrival_rate=1, service_rate=0.5, simulation_time=10)
