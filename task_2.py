import json  # TODO импортировать необходимые молули
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_file:  # TODO считать содержимое csv файла
        csv_data = [data for data in csv.DictReader(input_file)]
    with open(OUTPUT_FILENAME, 'w') as output_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(csv_data, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
