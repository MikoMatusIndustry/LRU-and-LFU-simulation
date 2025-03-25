import os
import csv
import subprocess
from page_generator import generate_100_seq
from lfu_alg import LFU
from lru_alg import LRU

size = 4

# Generowanie 100 różnych ciągów odwołań do stron
main_list = generate_100_seq()

# Testowanie algorytmu LFU
lfu_faults_list = LFU(main_list, size)

# Testowanie algorytmu LRU
lru_faults_list = LRU(main_list, size)

# Obliczanie średniej liczby brakujących stron dla LFU
average_lfu_faults = sum(lfu_faults_list) / len(lfu_faults_list)
print(f"Average number of faults (LFU): {average_lfu_faults}")

# Obliczanie średniej liczby brakujących stron dla LRU
average_lru_faults = sum(lru_faults_list) / len(lru_faults_list)
print(f"Average number of faults (LRU): {average_lru_faults}")

# Zapisanie wyników do pliku CSV
results_file_path = os.path.join(os.getcwd(), 'page_references_and_faults.csv')
with open(results_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')

    # Nagłówek dla stron
    headers = ['Sequence'] + [f'Page Reference {i + 1}' for i in range(100)] + ['LFU Faults', 'LRU Faults']
    writer.writerow(headers)

    for i in range(len(main_list)):
        row = [f'Seq{i + 1}'] + main_list[i] + [lfu_faults_list[i], lru_faults_list[i]]
        writer.writerow(row)

    # Dodanie wiersza przerwy
    writer.writerow([])

    # Dodanie wyników ogólnych
    writer.writerow(["Overall Averages"])
    writer.writerow(["LFU Average Faults", average_lfu_faults])
    writer.writerow(["LRU Average Faults", average_lru_faults])

print("Data has been written to page_references_and_faults.csv")

# Otwieranie pliku wynikowego
directory = os.getcwd()
print(directory)
subprocess.Popen(['explorer', results_file_path])
subprocess.Popen(f'explorer "{directory}"')