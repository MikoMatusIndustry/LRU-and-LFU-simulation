from collections import defaultdict, deque

def LFU(page_references, size):

    faults_list = []            # Inicjalizacja listy przechowującej liczbę błędów stron dla każdego ciągu

    for sub_list in page_references:        # Pętla iterująca przez każdy ciąg odwołań stron
        faults = 0                          # Zmienna przechowująca liczbę błędów stron dla aktualnego ciągu
        page_freq = defaultdict(int)        # Słownik przechowujący liczbę wystąpień każdej strony
        pages = set()                       # Zbiór przechowujący strony obecnie znajdujące się w pamięci
        page_queue = deque()                # Kolejka przechowująca strony w kolejności ich używania

        for el in sub_list:                 # Pętla iterująca przez każdą stronę w ciągu odwołań
            if el in pages:                 # Jeśli strona jest już w pamięci
                page_freq[el] += 1          # Zwiększenie licznika wystąpień strony
            else:
                faults += 1                 # Zwiększenie liczby błędów strony
                if len(pages) < size:       # Jeśli pamięć nie jest jeszcze pełna
                    pages.add(el)           # Dodanie strony do pamięci
                    page_queue.append(el)   # Dodanie strony do kolejki
                    page_freq[el] += 1      # Ustawienie licznika wystąpień strony na 1
                else:
                    # Usuwanie najmniej używanej strony z pamięci
                    while page_queue:
                        oldest_page = page_queue.popleft()  # Pobranie najstarszej strony z kolejki
                        if page_freq[oldest_page] == 1:     # Jeśli strona jest używana po raz pierwszy
                            pages.remove(oldest_page)       # Usunięcie strony z pamięci
                            del page_freq[oldest_page]      # Usunięcie licznika wystąpień strony
                            break
                        else:
                            page_freq[oldest_page] -= 1     # Zmniejszenie licznika wystąpień strony
                            page_queue.append(oldest_page)  # Dodanie strony z powrotem do kolejki

                    pages.add(el)           # Dodanie nowej strony do pamięci
                    page_queue.append(el)   # Dodanie nowej strony do kolejki
                    page_freq[el] += 1      # Ustawienie licznika wystąpień nowej strony

        faults_list.append(faults)           # Dodanie liczby błędów stron dla aktualnego ciągu do listy wynikowej

    return faults_list                      # Zwrócenie listy błędów stron dla wszystkich ciągów

