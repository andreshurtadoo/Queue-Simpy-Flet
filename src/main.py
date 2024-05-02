from src.simulation import simulate_queue

# Configuración de parámetros de la simulación
NUM_SERVERS = 2  # Número de servidores
ARRIVAL_RATE = 1  # Cliente cada 1 unidad de tiempo
SERVICE_RATE = 0.5  # Cada servidor atiende 2 clientes por unidad de tiempo
SIMULATION_TIME = 10  # Durar 10 unidades de tiempo

if __name__ == "__main__":
    simulate_queue(NUM_SERVERS, ARRIVAL_RATE, SERVICE_RATE, SIMULATION_TIME)
