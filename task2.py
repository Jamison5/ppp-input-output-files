import os
import random
from datetime import datetime


def create_dev_set(full_data_dir, dev_data_dir, ratio=10):
    os.makedirs(dev_data_dir, exist_ok=True)
    for file_name in sorted(os.listdir(full_data_dir)):
        with open(f"{full_data_dir}/{file_name}") as file_full, open(
            f"{dev_data_dir}/{file_name}", "w"
        ) as file_dev:
            for line in file_full:
                rand_num = random.randint(0, 100)
                if rand_num < ratio:
                    file_dev.write(line)


# TODO 1: Place your code here.
def load_phone_calls_dict(data_dir: str) -> dict:

    phone_call_dict = {}

    for file_name in sorted(os.listdir(data_dir)):
        with open(f"{data_dir}/{file_name}") as full_data:
            for line in full_data:
                time, phone_number = line.split(": ")
                area_code = phone_number[3:6]
                date_time_object = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                if area_code not in phone_call_dict:
                    phone_call_dict[area_code] = {}
                if phone_number.strip() not in phone_call_dict[area_code]:
                    phone_call_dict[area_code][phone_number.strip()] = []
                phone_call_dict[area_code][phone_number.strip()].append(
                    date_time_object
                )

    return phone_call_dict


phone_call_dict = load_phone_calls_dict("dev-data")


# TODO 2: Place your code here.
def generate_phone_call_counts(phone_call_dict: dict) -> dict:

    phone_call_count_dict = {}

    for _, phones in phone_call_dict.items():
        for phone_number, timestamps in phones.items():
            phone_call_count_dict[phone_number] = len(timestamps)

    return phone_call_count_dict


phone_call_counts = generate_phone_call_counts(phone_call_dict)


# TODO 3: Place your code here.
def most_frequently_called(phone_call_counts: dict, top_n: int) -> list:
    calls_list = []

    for phone_number, number_calls in phone_call_counts.items():

        calls_list.append((phone_number, number_calls))

    return sorted(calls_list, key=lambda item: item[1], reverse=True)[:top_n]


# TODO 4: Place your code here.


def export_phone_call_counts(top_call_list: list, out_file_path: str) -> None:
    with open(out_file_path, "w") as output:
        for phone_number, call_number in top_call_list:
            output.write(f"{phone_number}: {call_number}\n")


# TODO 5: Place your code here.

if __name__ == "__main__":

    toy_data = {
        "761": {
            "+1(761)823-1060": [
                datetime(2020, 1, 2, 0, 3, 5),
                datetime(2020, 5, 15, 0, 0, 10),
                datetime(2020, 8, 30, 0, 1, 36),
                datetime(2020, 10, 1, 0, 6, 28),
                datetime(2020, 12, 2, 0, 2, 55),
            ]
        },
        "892": {
            "+1(892)532-9243": [
                datetime(2020, 1, 1, 0, 0, 9),
                datetime(2020, 6, 5, 0, 1, 20),
                datetime(2020, 8, 9, 0, 5, 10),
                datetime(2020, 9, 15, 0, 3, 18),
                datetime(2020, 12, 15, 0, 2, 45),
            ]
        },
    }

    phone_call_dict = load_phone_calls_dict("dev-data")
    # phone_call_counts = generate_phone_call_counts(toy_data)
    # print(most_frequently_called(phone_call_counts, 1))
    phone_call_counts = generate_phone_call_counts(phone_call_dict)
    top_called = most_frequently_called(phone_call_counts, 10)
    export_phone_call_counts(top_called, "dev-data/most_frequent.txt")
