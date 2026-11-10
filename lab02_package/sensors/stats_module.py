# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників
import statistics


def get_average(data_dict):
    """Обчислює середнє арифметичне значення."""
    if not data_dict:
        return None
    return sum(data_dict.values()) / len(data_dict)


def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None
    return min(data_dict.values())


def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None
    return max(data_dict.values())


def get_median(data_dict):
    """Обчислює медіану."""
    if not data_dict:
        return None
    return statistics.median(data_dict.values())


def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями, що перевищують threshold."""
    if not data_dict or len(data_dict) < 2:
        return []

    items = list(data_dict.items())
    jumps = []

    for i in range(len(items) - 1):
        t1, v1 = items[i]
        t2, v2 = items[i + 1]
        diff = abs(v2 - v1)
        if diff > threshold:
            jumps.append((t1, t2, round(diff, 2)))

    return jumps


def show_table(data_dict, title):
    """Виводить відформатовану таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<12} | {'Значення':<10}")
    print("-" * 27)
    for time_label, val in data_dict.items():
        print(f"{time_label:<12} | {val:<10}")