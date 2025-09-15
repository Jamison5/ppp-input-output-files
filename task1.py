from datetime import datetime


# TODO: Place your code here.
def filter_phone_calls(
    area_code: int, start_hour: int, end_hour: int, input_path: str, output_path: str
) -> object:
    """
    As the first step, implement a function that reads the file and prints it to the terminal one line at a time. Start your work by creating the filter_phone_calls function with the following parameters:

        area_code: An int indicating the focused area code.

        start_hour: An int between 0 and 24 indicating the starting hour of the focused time span.

        end_hour: An int between 0 and 24 indicating the finishing hour of the focused time span.

        input_path: A str identifying the file from which the input should be read.

        output_path: A str identifying the file to which the output should be written.

    Within the function, open the input_path file for reading, preferably using the with statement. Read the file line by line and print the lines to your terminal.
    """

    file_path = input_path

    with open(file_path, "r") as file, open(output_path, "w") as output:

        lines = file.readlines()

        area_code_filtered_list = []

        filtered_hours = range(start_hour, end_hour)

        for line in lines:

            date_time, phone_number = line.split(": ")

            dtg = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

            if int(phone_number[3:6]) == area_code and dtg.hour in filtered_hours:

                filtered_line = date_time + ": " + phone_number

                area_code_filtered_list.append(filtered_line)

        for line in area_code_filtered_list:

            output.write(line)


if __name__ == "__main__":

    filter_phone_calls(
        area_code=412,
        start_hour=0,
        end_hour=6,
        input_path="data/phone_calls.txt",
        output_path="data/phone_calls_filtered.txt",
    )
