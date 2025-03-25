# Funkcja implementująca algorytm LRU
def LRU(page_references, size):
    faults_list = []            #inicjalizacja listy przechowującej l. brakujących stron

    for sub_list in page_references:    #pętla iterująca przez każdy ciąg odwołań
        faults = 0
        pages = []         # Inicjalizacja listy, która będzie przechowywać strony w kolejności ich ostatniego użycia.

        for el in sub_list:     #pętla iterująca przez każdy ciąg odwołań
            if el in pages:
                pages.remove(el)    #usunięcie strony z jej aktualnej pozycji w liście
                pages.append(el)    #dodanie strony na koniec listy
            else:
                faults += 1
                if len(pages) < size:       #sprawdzanie czy pamięć jest pełna
                    pages.append(el)        #dodanie strony do pamięci
                else:
                    pages.pop(0)
                    pages.append(el)    #dodanie nowej strony na koniec listy

        faults_list.append(faults)  #dodanie liczby brakujących stron
    return faults_list