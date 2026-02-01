# 🚀 Galactic Scavenger - Resource Extraction Sim

A strategic space-mining simulation where you balance ship integrity against the lure of rare minerals. Navigate between three distinct sectors of space, each with varying levels of risk and reward. Your goal is to accumulate 1,000 credits through smart trading before your ship's hull is destroyed.

This project focuses on teaching:
* **Probability-Based Hazards:** Using randomized "Danger" thresholds to trigger negative events.
* **Economic Loop Design:** Implementing a "Gather -> Store -> Sell" cycle.
* **Data-Driven Navigation:** Mapping game locations to a dictionary for easy world expansion.
* **Multiple Win/Loss Conditions:** Managing a loop that monitors two critical variables (Hull and Credits) simultaneously.

---

## ✨ Features

* **Sector Difficulty:** Choose between "Alpha Belt" (Safe/Low-value), "Nebula Core" (Moderate), and "The Void" (High-risk/High-reward).
* **Cargo Management:** Store extracted minerals in your ship's hold until you return to base to sell.
* **Dynamic Hull Damage:** Collisions in high-danger zones result in randomized damage percentages.
* **Scaling Economy:** Different minerals (Iron vs. Void Crystals) have significantly different market values.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `scavenger.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python scavenger.py
    ```

### 3. Gameplay Instructions
1.  **Select a Sector:** Enter 1, 2, or 3 to begin mining.
2.  **Watch the Hull:** If your hull reaches 0%, the mission fails.
3.  **Sell Cargo:** Return to the station by typing **"S"** to convert your minerals into credits.
4.  **Win Condition:** Reach 1,000 credits to successfully retire.



---

## 🧠 Code Structure Highlights

### The Danger Logic
The game uses a "Dice Roll" mechanic to determine if a collision occurs. If a random number from 1–100 is less than or equal to the area's danger rating, the ship takes damage.

```python
if random.randint(1, 100) <= loc['danger']:
    # Trigger collision event

