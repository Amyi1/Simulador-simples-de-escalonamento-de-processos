QUANTUM = 2

CENARIOS = [
    ("1 - Processos curtos", [
        {"nome": "P1", "cpu": 3, "prioridade": 1},
        {"nome": "P2", "cpu": 1, "prioridade": 1},
        {"nome": "P3", "cpu": 2, "prioridade": 1},
    ]),
    ("2 - Curtos e longos", [
        {"nome": "P1", "cpu": 8, "prioridade": 1},
        {"nome": "P2", "cpu": 2, "prioridade": 1},
        {"nome": "P3", "cpu": 1, "prioridade": 1},
    ]),
    ("3 - Prioridades diferentes", [
        {"nome": "P1", "cpu": 4, "prioridade": 3},
        {"nome": "P2", "cpu": 2, "prioridade": 1},
        {"nome": "P3", "cpu": 3, "prioridade": 2},
    ]),
]


def fcfs(processos):
    """Executa os processos na ordem recebida, ate cada um terminar."""
    tempo = 0
    sequencia = []
    terminos = {}

    for processo in processos:
        inicio = tempo
        tempo += processo["cpu"]
        nome = processo["nome"]
        sequencia.append((nome, inicio, tempo))
        terminos[nome] = tempo

    return sequencia, terminos


def sjf(processos):
    ordenados = sorted(processos, key=lambda processo: processo["cpu"])
    return fcfs(ordenados)


def prioridade(processos):
    ordenados = sorted(processos, key=lambda processo: processo["prioridade"])
    return fcfs(ordenados)


def round_robin(processos, quantum):
    tempo = 0
    sequencia = []
    terminos = {}
    fila = processos.copy()
    restante = {}

    for processo in processos:
        restante[processo["nome"]] = processo["cpu"]

    while fila:
        processo = fila.pop(0)
        nome = processo["nome"]
        duracao = min(quantum, restante[nome])

        inicio = tempo
        tempo += duracao
        restante[nome] -= duracao
        sequencia.append((nome, inicio, tempo))

        if restante[nome] > 0:
            fila.append(processo)
        else:
            terminos[nome] = tempo

    return sequencia, terminos


def mostrar_resultados(algoritmo, processos, resultado):
    sequencia, terminos = resultado
    soma_espera = 0
    soma_turnaround = 0

    print(f"\nAlgoritmo: {algoritmo}")
    trechos = []
    for nome, inicio, fim in sequencia:
        trechos.append(f"{nome} de {inicio} a {fim}")
    print("Sequencia: " + "; ".join(trechos))

    print(f"{'Processo':<10} {'CPU':>5} {'Prioridade':>12} {'Espera':>8} {'Turnaround':>12}")

    for processo in processos:
        nome = processo["nome"]
        cpu = processo["cpu"]
        turnaround = terminos[nome]
        espera = turnaround - cpu

        soma_espera += espera
        soma_turnaround += turnaround
        print(f"{nome:<10} {cpu:>5} {processo['prioridade']:>12} {espera:>8} {turnaround:>12}")

    quantidade = len(processos)
    espera_media = f"{soma_espera / quantidade:.2f}".replace(".", ",")
    turnaround_medio = f"{soma_turnaround / quantidade:.2f}".replace(".", ",")
    print(f"Espera media: {espera_media}")
    print(f"Turnaround medio: {turnaround_medio}")


def main():
    for nome_cenario, processos in CENARIOS:
        print("\n" + "=" * 60)
        print(f"Cenario {nome_cenario}")

        mostrar_resultados("FCFS", processos, fcfs(processos))
        mostrar_resultados("SJF", processos, sjf(processos))
        mostrar_resultados("Prioridade", processos, prioridade(processos))
        mostrar_resultados(
            f"Round Robin (quantum {QUANTUM})",
            processos,
            round_robin(processos, QUANTUM),
        )


if __name__ == "__main__":
    main()
