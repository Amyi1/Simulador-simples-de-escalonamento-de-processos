# Trabalho 2 — Simulador simples de escalonamento de processos

**Faculdade Serra Dourada**  
**Disciplina:** Sistemas Operacionais

**Integrantes:** Atos Gomes, Amy Galvão Pereira e Dmylle Charis.

O programa foi desenvolvido em Python e compara FCFS, SJF, Prioridade e Round Robin nos três cenários da atividade. Todos os processos chegam no instante 0, e o Round Robin usa quantum 2.

## Como executar

Com o Python instalado, abra o terminal na pasta do projeto e execute:

```bash
python simulador.py
```


O programa mostra a sequência de execução, o tempo de espera e o turnaround de cada processo, além das médias. Para alterar o quantum, mude a variável `QUANTUM` no início do código.

## Arquivos

- `simulador.py`: código do simulador.
- `results.txt`: saída das 12 execuções, com quatro algoritmos em cada cenário.
- `conferencia-manual-e-analise.pdf`: relatório com integrantes, resultados, conferência manual e análise.
- `referência`: : https://github.com/Ronix-arch/Operating-Systems-CPU-Scheduling-Policies

