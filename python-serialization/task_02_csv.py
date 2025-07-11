import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        data_list = []

        # CSV faylını açırıq
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        # JSON faylını yazırıq
        with open('data.json', mode='w') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
