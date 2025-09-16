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
    """


    Assign a phone_calls_dict variable with an empty dict.

    Implement a for loop that iterates over the phone_calls_*.txt files. HINT: The os.listdir function may be helpful here.

    For each file, open it (preferably using the with statement) and read it line by line.

    Extract the timestamp and the phone_number from each line into separate variables. HINT: Use the split method to separate a line into the two constituents.

    From the phone_number extract the area_code. HINT: Use slicing on the str which can be understood as a list of characters. You want to extract the three digits enclosed in the parentheses.

    Cast the timestamp into the datetime object. This will enable you to easily determine if the call happened after a certain hour in a day. HINT: You have done this in the preceding module.

    Check if the phone call happened between midnight (included) and 6 am (not included).

    If the phone call happened between midnight and 6 am append the timestamp to the appropriate place in the phone_calls_dict. First, you should use conditional statements to check if the necessary keys are already present in the phone_calls_dict. Finally, you would (presumably) append the timestamp to the phone_calls_dict like this:

     phone_calls_dict[area_code][phone_number].append(timestamp)


    """

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
def generate_phone_call_counts(phone_call_dict: dict = phone_call_dict) -> dict:

    phone_call_count_dict = {}

    for _, phones in phone_call_dict.items():
        for phone_number, timestamps in phones.items():
            phone_call_count_dict[phone_number] = len(timestamps)

    return phone_call_count_dict


# TODO 3: Place your code here.


# TODO 4: Place your code here.


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
    print(len(phone_call_dict["235"]["+1(235)749-3993"]))
    print(generate_phone_call_counts(toy_data))
