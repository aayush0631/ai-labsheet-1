# 🧹 Vacuum Cleaner Agent (Python)

This project simulates a **Vacuum Cleaner Agent** using three different AI paradigms:
- ✅ Reflex-based Agent
- 🎯 Goal-based Agent
- 📈 Utility-based Agent

Each agent interacts with a grid-like environment containing clean and dirty tiles, attempting to maximize performance and efficiency.

---

## 📌 Features

- 🧠 Three types of intelligent agents:
  - **Reflex Agent**
  - **Goal-Based Agent**
  - **Utility-Based Agent**
  
- 🔄 Environment setup with customizable grid sizes and dirt placement.
- 📊 Performance tracking (steps taken, efficiency).
- 🖥️ Simple CLI interface with visualization using print-based grid.

---

## 🧠 Agent Types Explained

### 🔁 Reflex-Based Agent
- Acts based **only on current perception**.
- It checks if the current tile is dirty — if yes, it cleans. Otherwise, it moves randomly.
- No memory or learning — simple but effective for small environments.
---![reflex_initial](https://github.com/user-attachments/assets/9be109fa-e990-4ed8-88a5-b8b6651f6117)
  ![reflex_mid](https://github.com/user-attachments/assets/ae1fccab-04c7-4ac7-abf1-9a433cba891b)
  ![reflex_output](https://github.com/user-attachments/assets/fbab62b7-572c-4df1-a5a9-89a5a4c98ee7)


  
### 🎯 Goal-Based Agent
- Has a **defined goal** (e.g., "clean all dirty tiles").
- Uses internal representation and simple planning to decide the next move.
- More efficient than reflex agents in larger or structured environments.
- ![goal_initial](https://github.com/user-attachments/assets/f02e98cd-990a-4250-ae8a-80202c4f7d9a)
- ![goal_mid](https://github.com/user-attachments/assets/de4034ab-3148-43f3-8b4b-c7ab69c527a0)
![goal_output](https://github.com/user-attachments/assets/987ccc7a-43d2-4657-9047-4c1aa80f983f)



### 📈 Utility-Based Agent
- Makes decisions based on a **utility function** that scores possible outcomes.
- Chooses actions that **maximize overall cleanliness and minimize effort**.
- Can compare and prioritize between multiple goals or states.
![utility_initial](https://github.com/user-attachments/assets/d0846088-f4e6-4103-bbb8-b298ad90228f)
![utility_output](https://github.com/user-attachments/assets/8c79fc22-ed36-4659-b7a9-04922650ab80)
![utility_mid](https://github.com/user-attachments/assets/06a15b79-8ad2-464c-b4ee-6d9a3271ba3b)


## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/vacuum-cleaner-agent.git
   cd vacuum-cleaner-agent
