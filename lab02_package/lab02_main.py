# lab02_main.py для Завдання №2
import sensors as sm # Імпорт із пакета sensors


def parse_input(input_str):
    """Перетворює введений рядок у список чисел з перехопленням ValueError."""
    tokens = input_str.strip().split()
    numbers = []
    for token in tokens:
        try:
            val = float(token)
            numbers.append(val)
        except ValueError:
            print(f"Попередження: '{token}' не є числом та буде проігноровано.")
    return numbers


def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник із часовими мітками T1, T2, ..."""
    data = {"temperature": {}, "humidity": {}, "pressure": {}}
    min_len = min(len(temp_list), len(hum_list), len(pres_list))

    for i in range(min_len):
        label = f"T{i + 1}"
        data["temperature"][label] = temp_list[i]
        data["humidity"][label] = hum_list[i]
        data["pressure"][label] = pres_list[i]

    return data


def process_measurements(title, data_dict, threshold, unit=""):
    """Виводить таблицю та розраховані статистичні показники."""
    sm.show_table(data_dict, title)

    avg_val = sm.get_average(data_dict)
    min_val = sm.get_min(data_dict)
    max_val = sm.get_max(data_dict)
    med_val = sm.get_median(data_dict)
    jumps = sm.find_jumps(data_dict, threshold)

    print(f"\nСереднє значення: {avg_val:.2f}{unit}")
    print(f"Мінімум: {min_val:.1f}{unit}")
    print(f"Максимум: {max_val:.1f}{unit}")
    print(f"Медіана: {med_val:.1f}{unit}")

    if jumps:
        jumps_str = ", ".join([f"між {t1} → {t2} ({d}{unit})" for t1, t2, d in jumps])
        print(f"Різкі перепади: {jumps_str}")
    else:
        print("Різких перепадів не виявлено.")


def main():
    print("=== Обробка показів системи 'Розумний будинок' ===")

    temp_raw = input("Введіть температури (°C): ")
    hum_raw = input("Введіть вологість (%): ")
    pres_raw = input("Введіть тиск (Па): ")

    temp_list = parse_input(temp_raw)
    hum_list = parse_input(hum_raw)
    pres_list = parse_input(pres_raw)

    if not (len(temp_list) == len(hum_list) == len(pres_list)):
        print("\nУвага: Кількість елементів у рядах відрізняється!")
        print(f"Temp={len(temp_list)}, Hum={len(hum_list)}, Pres={len(pres_list)}")
        print("Розрахунок буде проведено за найменшою спільною кількістю замірів.")

    if not temp_list or not hum_list or not pres_list:
        print("Помилка: Недостатньо числових даних для обробки.")
        return

    data = create_data_dict(temp_list, hum_list, pres_list)

    process_measurements("Temperature", data["temperature"], threshold=7.0, unit="°C")
    process_measurements("Humidity", data["humidity"], threshold=20.0, unit="%")
    process_measurements("Pressure", data["pressure"], threshold=5000.0, unit=" Па")


if __name__ == "__main__":
    main()