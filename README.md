# LRU and LFU Page Replacement Simulation

This Python project simulates two classic page replacement algorithms: **LRU (Least Recently Used)** and **LFU (Least Frequently Used)**. It generates random sequences of memory page references and evaluates how each algorithm performs in terms of page faults.

---

## 📌 Features

- Simulation of **100 randomly generated** page reference sequences
- Implementation of both **LRU** and **LFU** algorithms
- Calculates the **average number of page faults** for both algorithms
- Saves the results in a `.csv` file for further analysis

---

## 🚀 How It Works

1. Generates 100 random sequences of memory page references
2. Applies both LFU and LRU algorithms to each sequence
3. Counts page faults for each algorithm
4. Outputs:
   - Average page faults for LFU and LRU
   - A `.csv` file with detailed results

---

## 🧠 Algorithms Used

- **LRU (Least Recently Used)**: Replaces the page that was used least recently.
- **LFU (Least Frequently Used)**: Replaces the page with the lowest access frequency.

---

## 📁 Project Structure

```
LRU-and-LFU-simulation/
│
├── main.py                          # Main script to run the simulation
├── lru_alg.py                       # LRU algorithm implementation
├── lfu_alg.py                       # LFU algorithm implementation
├── page_generator.py                # Page reference sequence generator
├── page_references_and_faults.csv  # Output file with results
├── __pycache__/                    # Compiled Python files (can be ignored)
└── .idea/                          # IDE configuration (optional to keep)
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MikoMatusIndustry/LRU-and-LFU-simulation.git
cd LRU-and-LFU-simulation
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Run the simulation

```bash
python main.py
```

---

## 📊 Output Example

```text
Average number of faults (LFU): 83.42
Average number of faults (LRU): 76.31
```

Results are also saved to `page_references_and_faults.csv` in a structured format.

---

## 📎 Requirements

This project uses only built-in Python libraries, so **no external packages** are required.

---

## 🧑‍💻 Author

**Mikołaj Matusik**  
[GitHub: MikoMatusIndustry](https://github.com/MikoMatusIndustry)

---

## 📜 License

This project is open source and available under the [MIT License].
