"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""
import heapq

def min_connection_cost(cables):
    if not cables:
        return 0
    
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined = first + second
        total_cost += combined

        heapq.heappush(cables, combined)

    return total_cost
if __name__ == "__main__":
    cables = [4, 3, 2, 6, 5, 9, 7]
    result = min_connection_cost(cables)
    print("Мінімальна вартість з'єднання кабелів:", result)
