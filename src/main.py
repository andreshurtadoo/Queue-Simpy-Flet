import flet as ft
from simulation import simulate_queue

def main(page: ft.Page):
    page.title = "Simulador de Sistema de Colas"

    # Controles para entrada de parámetros
    num_servers_input = ft.TextField(label="Número de Servidores", value="2", width=200)
    arrival_rate_input = ft.TextField(label="Tasa de Llegada de Clientes", value="1", width=200)
    service_rate_input = ft.TextField(label="Tasa de Servicio", value="0.5", width=200)
    simulation_time_input = ft.TextField(label="Tiempo de Simulación", value="100", width=200)

    # Botón para ejecutar la simulación
    run_button = ft.TextButton(text="Ejecutar Simulación", on_click=lambda e: run_simulation(page))

    # Área de texto para mostrar resultados
    results_text = ft.TextField(label="Resultados", multiline=True, disabled=True, width=300, height=200)

    # Función para ejecutar la simulación y mostrar resultados
    def run_simulation(page):
        num_servers = int(num_servers_input.value)
        arrival_rate = float(arrival_rate_input.value)
        service_rate = float(service_rate_input.value)
        simulation_time = int(simulation_time_input.value)

        average_time, utilization = simulate_queue(num_servers, arrival_rate, service_rate, simulation_time)
        results_text.value = f"Tiempo promedio en el sistema: {average_time:.2f} unidades de tiempo\n" \
                             f"Utilización de los servidores: {utilization:.2%}"
        page.update()

    # Agregando controles a la página
    page.add(num_servers_input, arrival_rate_input, service_rate_input, simulation_time_input, run_button, results_text)

if __name__ == "__main__":
    ft.app(target=main)
