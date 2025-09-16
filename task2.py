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

    From the phone_number extract the area_code. HINT: Use slicing on the str which can be understood as a list of characters. You want to extract the three digits
    enclosed in the parentheses.

    Cast the timestamp into the datetime object. This will enable you to easily determine if the call happened after a certain hour in a day. HINT: You have done this
    in the preceding module.

    Check if the phone call happened between midnight (included) and 6 am (not included).

    If the phone call happened between midnight and 6 am append the timestamp to the appropriate place in the phone_calls_dict. First, you should use conditional
    statements to check if the necessary keys are already present in the phone_calls_dict. Finally, you would (presumably) append the timestamp to the phone_calls_dict like
    this:

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
def generate_phone_call_counts(phone_call_dict: dict) -> dict:

    phone_call_count_dict = {}

    for _, phones in phone_call_dict.items():
        for phone_number, timestamps in phones.items():
            phone_call_count_dict[phone_number] = len(timestamps)

    return phone_call_count_dict


phone_call_counts = generate_phone_call_counts(phone_call_dict)


# TODO 3: Place your code here.
def most_frequently_called(phone_call_counts: dict, top_n: int):
    """
    In TODO 3, you will implement the most_frequently_called function that utilizes the output of the generate_phone_call_counts function to generate a sorted list of the
    most frequently called phone numbers. The function has the following two parameters:

    phone_call_counts: The output of the generate_phone_call_counts function, i.e., a dict that maps phone numbers (key) to an int corresponding to the number of calls.

    top_n: An int indicating how many top entries should be returned. For example, setting the parameter to 10 would result in the top 10 most frequently called numbers
    being returned.

    The most_frequently_called function outputs a list with the following structure:

        [
            ('<Phone number>', 00)
            ...
        ]

    For example, consider this toy data set:

        2020-01-01 00:00:09: +1(892)532-9243
        2020-01-02 00:03:05: +1(761)823-1060
        2020-05-15 00:00:10: +1(547)945-6891
        2020-06-05 00:01:20: +1(892)532-9243
        2020-08-09 00:05:10: +1(892)532-9243
        2020-08-30 00:01:36: +1(761)823-1060
        2020-09-15 00:03:18: +1(892)532-9243
        2020-10-01 00:06:28: +1(547)945-6891
        2020-12-02 00:02:55: +1(761)823-1060
        2020-12-15 00:02:45: +1(892)532-9243

    Assuming the dataset has been first processed by the load_phone_calls_dict and generate_phone_call_counts functions, resulting in the phone_call_counts dictionary,
    the output of the most_frequently_called(phone_call_counts, 2) would look like this:

        [
            ('+1(892)532-9243', 5),
            ('+1(761)823-1060', 3)
        ]

    This means that there will be a list of tuples with two elements - a phone number (str) and the number of calls directed to that phone number (int).

    The phone numbers have to be ordered per the number of calls they received in the decreasing order. In case of a tie, use the phone numbers themselves in
    the ascending order.

    Suggested logic for the most_frequently_called function:

        Cast the phone_call_counts dictionary into the list of tuples with phone numbers and the number of calls.

        Order the list per the number of calls (descending) and the phone numbers themselves (ascending).

        Return the top_n first elements from the resulting list.

    """

    calls_list = []

    for phone_number, number_calls in phone_call_counts.items():

        calls_list.append((phone_number, number_calls))

    return sorted(calls_list, key=lambda item: item[1], reverse=True)[:top_n]


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
    # phone_call_counts = generate_phone_call_counts(toy_data)
    # print(most_frequently_called(phone_call_counts, 1))
    phone_call_counts = generate_phone_call_counts(phone_call_dict)
    top_called = most_frequently_called(phone_call_counts, 10)
    print(top_called)
