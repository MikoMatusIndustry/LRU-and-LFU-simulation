import random

def generate_100_seq(lower_bound=0, upper_bound=20, num_elements=100):

    main_list = []          # Inicjalizacja listy przechowującej 100 ciągów odwołań stron
    random.seed(1)          # Ustawienie seeda, aby wygenerowane liczby były powtarzalne
    for i in range(100):    # Pętla generująca 100 różnych ciągów odwołań do stron
        sub_list = [random.randint(lower_bound, upper_bound) for _ in range(num_elements)]  # Generowanie pojedynczego ciągu odwołań
        main_list.append(sub_list)  # Dodanie ciągu do głównej listy
    return main_list        # Zwrócenie wygenerowanej listy

