import tkinter as tk
import random

ROWS = 10
COLS = 10
DELAY = 200  # milliseconds between steps


class UtilityBasedVacuumCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Utility-Based Vacuum Cleaner Agent")

        self.instruction_label = tk.Label(root, text="Press ENTER to start utility-based cleaning", font=("Arial", 14))
        self.instruction_label.grid(row=0, column=0, columnspan=COLS)

        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.labels = [[None for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                label = tk.Label(root, text=str(self.grid[i][j]), width=4, height=2,
                                 font=('Arial', 14), borderwidth=1, relief="solid")
                label.grid(row=i + 1, column=j)
                self.labels[i][j] = label

        self.result_text = tk.Text(root, height=20, width=COLS * 6, font=("Courier", 10))
        self.result_text.grid(row=ROWS + 2, column=0, columnspan=COLS, pady=10)
        self.result_text.config(state='disabled')

        self.agent_pos = (0, 0)
        self.steps = 0
        self.path = []

        self.root.bind('<Return>', self.on_enter_press)

    def on_enter_press(self, event):
        self.root.unbind('<Return>')
        self.instruction_label.config(text="Utility-based cleaning started...")
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, "Cleaning in progress (Utility-Based Agent)...\n")
        self.result_text.config(state='disabled')
        self.root.after(500, self.clean_next)

    def utility(self, cell):
        r, c = cell
        if self.grid[r][c] != 1:
            return -1  # Already clean, no utility

        # Local dirtiness: count dirty neighbors
        dirty_neighbors = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr == 0 and dc == 0) or not (0 <= r + dr < ROWS and 0 <= c + dc < COLS):
                    continue
                if self.grid[r + dr][c + dc] == 1:
                    dirty_neighbors += 1

        # Utility = (weight on proximity) - (distance) + (weight on surrounding dirtiness)
        distance = abs(self.agent_pos[0] - r) + abs(self.agent_pos[1] - c)
        return 10 - distance + dirty_neighbors * 2

    def find_best_cell(self):
        candidates = [(r, c) for r in range(ROWS) for c in range(COLS) if self.grid[r][c] == 1]
        if not candidates:
            return None
        return max(candidates, key=self.utility)

    def move_toward(self, target):
        r1, c1 = self.agent_pos
        r2, c2 = target
        if r1 != r2:
            r1 += 1 if r2 > r1 else -1
        elif c1 != c2:
            c1 += 1 if c2 > c1 else -1
        self.agent_pos = (r1, c1)

    def clean_next(self):
        best_cell = self.find_best_cell()
        if not best_cell:
            self.show_result()
            return

        if self.agent_pos != best_cell:
            self.move_toward(best_cell)
        else:
            r, c = self.agent_pos
            self.grid[r][c] = 0
            self.labels[r][c].config(text='0', bg='lightgreen')  # cleaned

        self.steps += 1
        self.path.append(self.agent_pos)

        # Mark visited cell
        r, c = self.agent_pos
        if self.labels[r][c].cget('bg') != 'lightgreen':
            self.labels[r][c].config(bg='lightblue')

        self.root.after(DELAY, self.clean_next)

    def show_result(self):
        result = f"✅ Utility-based cleaning complete!\n🧭 Total Steps taken: {self.steps}\n\n📍 Path taken:\n"
        lines = []
        line = []
        for idx, (r, c) in enumerate(self.path, start=1):
            line.append(f"({r},{c})")
            if idx % 10 == 0:
                lines.append(' → '.join(line))
                line = []
        if line:
            lines.append(' → '.join(line))
        result += '\n'.join(lines) + '\n\n'

        report = (
            "--- 🧮 Utility-Based Strategy ---\n"
            "Prioritized dirty cells based on:\n"
            "- Proximity to current position\n"
            "- Surrounding local dirtiness\n"
            "Used greedy utility maximization to choose targets.\n"
        )

        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result + report)
        self.result_text.config(state='disabled')


# Run the app
root = tk.Tk()
app = UtilityBasedVacuumCleaner(root)
root.mainloop()
