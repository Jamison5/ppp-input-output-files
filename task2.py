import os
import random


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


# TODO 2: Place your code here.


# TODO 3: Place your code here.


# TODO 4: Place your code here.


# TODO 5: Place your code here.

if __name__ == "__main__":

    pass
