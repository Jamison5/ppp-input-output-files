import os
import random
from datetime import datetime, timedelta


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


# TODO 2: Place your code here.
def generate_phone_call_counts(phone_call_dict: dict) -> dict:

    phone_call_count_dict = {}

    for _, phones in phone_call_dict.items():
        for phone_number, timestamps in phones.items():
            phone_call_count_dict[phone_number] = len(timestamps)

    return phone_call_count_dict


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


def export_redials_report(phone_call_dict: dict, report_dir: str) -> None:
    """
    Create one plain-text report per area code.

    Each <area_code>.txt file lists, in ascending order of phone number
    and call time, all pairs of consecutive calls to the *same* number
    that occur less than 10 minutes apart.

    Format of each line:
        +1(000)000-0000: YYYY-MM-DD HH:MM:SS -> HH:MM:SS (MM:SS)
    """
    os.makedirs(report_dir, exist_ok=True)
    THRESHOLD = 600  # 10 minutes, in seconds

    # Iterate by area code
    for area_code, ac_data in phone_call_dict.items():
        # Sort phone numbers lexicographically
        output_lines = []

        for phone_number in sorted(ac_data):
            # Sort timestamps chronologically
            times = sorted(ac_data[phone_number])

            # Compare consecutive timestamps
            for i in range(len(times) - 1):
                t1, t2 = times[i], times[i + 1]
                diff_sec = (t2 - t1).total_seconds()

                if diff_sec < THRESHOLD:
                    # Format pieces
                    start_str = t1.strftime("%Y-%m-%d %H:%M:%S")
                    end_time = t2.strftime("%H:%M:%S")
                    mins, secs = divmod(int(diff_sec), 60)
                    dur_str = f"{mins:02d}:{secs:02d}"

                    output_lines.append(
                        f"{phone_number}: {start_str} -> {end_time} ({dur_str})\n"
                    )

        # Always create the file—even if empty
        file_path = os.path.join(report_dir, f"{area_code}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(output_lines)


if __name__ == "__main__":

    phone_call_dict = load_phone_calls_dict("toy-data")
    export_redials_report(phone_call_dict, "toy-data-reports")
    # phone_call_counts = generate_phone_call_counts(phone_call_dict)
    # top_called = most_frequently_called(phone_call_counts, 10)
    # export_phone_call_counts(top_called, "dev-data/most_frequent.txt")
