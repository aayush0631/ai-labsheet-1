import tkinter as tk
import random

ROWS = 10
COLS = 10
DELAY = 200  # slower for goal-based clarity

class GoalBasedVacuumCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Goal-Based Vacuum Cleaner Agent (with Memory)")

        self.instruction_label = tk.Label(root, text="Press ENTER to start goal-based cleaning", font=("Arial", 14))
        self.instruction_label.grid(row=0, column=0, columnspan=COLS)

        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.labels = [[None for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                label = tk.Label(root, text=str(self.grid[i][j]), width=4, height=2,
                                 font=('Arial', 14), borderwidth=1, relief="solid")
                label.grid(row=i+1, column=j)
                self.labels[i][j] = label

        self.result_text = tk.Text(root, height=20, width=COLS * 6, font=("Courier", 10))
        self.result_text.grid(row=ROWS + 2, column=0, columnspan=COLS, pady=10)
        self.result_text.config(state='disabled')

        self.agent_pos = (0, 0)
        self.steps = 0
        self.path = []
        self.memory = set()

        self.dirty_cells = {(i, j) for i in range(ROWS) for j in range(COLS) if self.grid[i][j] == 1}

        self.root.bind('<Return>', self.on_enter_press)

    def on_enter_press(self, event):
        self.root.unbind('<Return>')
        self.instruction_label.config(text="Goal-based cleaning started...")
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, "Cleaning in progress (Goal-Based Agent)...\n")
        self.result_text.config(state='disabled')
        self.root.after(500, self.goal_clean)

    def goal_clean(self):
        if not self.dirty_cells:
            self.show_result()
            return

        # Find the nearest dirty cell from current position
        current = self.agent_pos
        target = min(self.dirty_cells, key=lambda cell: abs(cell[0] - current[0]) + abs(cell[1] - current[1]))

        # Move toward the target
        if current != target:
            r1, c1 = current
            r2, c2 = target
            if r1 != r2:
                r1 += 1 if r2 > r1 else -1
            elif c1 != c2:
                c1 += 1 if c2 > c1 else -1
            self.agent_pos = (r1, c1)
        else:
            # At dirty cell: clean
            r, c = current
            self.grid[r][c] = 0
            self.labels[r][c].config(text='0', bg='lightgreen')
            self.dirty_cells.remove((r, c))

        self.steps += 1
        self.path.append(self.agent_pos)
        if self.grid[self.agent_pos[0]][self.agent_pos[1]] == 0 and self.agent_pos not in self.dirty_cells:
            self.labels[self.agent_pos[0]][self.agent_pos[1]].config(bg='lightblue')

        self.root.after(DELAY, self.goal_clean)

    def show_result(self):
        result = f"✅ Goal-based cleaning complete!\n🧭 Total Steps taken: {self.steps}\n\n📍 Path taken:\n"
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

        report = f"🧠 Memory Used: {len(self.memory)} cells (not explicitly tracked here)\n"
        report += f"🧼 Initial Dirty Cells: {len(self.path)}\n"
        report += "--- Goal-Based Agent focused only on dirty cells using memory + greedy strategy ---"

        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result + report)
        self.result_text.config(state='disabled')


# Run the app
root = tk.Tk()
app = GoalBasedVacuumCleaner(root)
root.mainloop()
import tkinter as tk
import random

ROWS = 10
COLS = 10
DELAY = 200  # slower for goal-based clarity

class GoalBasedVacuumCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Goal-Based Vacuum Cleaner Agent (with Memory)")

        self.instruction_label = tk.Label(root, text="Press ENTER to start goal-based cleaning", font=("Arial", 14))
        self.instruction_label.grid(row=0, column=0, columnspan=COLS)

        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.labels = [[None for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                label = tk.Label(root, text=str(self.grid[i][j]), width=4, height=2,
                                 font=('Arial', 14), borderwidth=1, relief="solid")
                label.grid(row=i+1, column=j)
                self.labels[i][j] = label

        self.result_text = tk.Text(root, height=20, width=COLS * 6, font=("Courier", 10))
        self.result_text.grid(row=ROWS + 2, column=0, columnspan=COLS, pady=10)
        self.result_text.config(state='disabled')

        self.agent_pos = (0, 0)
        self.steps = 0
        self.path = []
        self.memory = set()

        self.dirty_cells = {(i, j) for i in range(ROWS) for j in range(COLS) if self.grid[i][j] == 1}

        self.root.bind('<Return>', self.on_enter_press)

    def on_enter_press(self, event):
        self.root.unbind('<Return>')
        self.instruction_label.config(text="Goal-based cleaning started...")
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, "Cleaning in progress (Goal-Based Agent)...\n")
        self.result_text.config(state='disabled')
        self.root.after(500, self.goal_clean)

    def goal_clean(self):
        if not self.dirty_cells:
            self.show_result()
            return

        # Find the nearest dirty cell from current position
        current = self.agent_pos
        target = min(self.dirty_cells, key=lambda cell: abs(cell[0] - current[0]) + abs(cell[1] - current[1]))

        # Move toward the target
        if current != target:
            r1, c1 = current
            r2, c2 = target
            if r1 != r2:
                r1 += 1 if r2 > r1 else -1
            elif c1 != c2:
                c1 += 1 if c2 > c1 else -1
            self.agent_pos = (r1, c1)
        else:
            # At dirty cell: clean
            r, c = current
            self.grid[r][c] = 0
            self.labels[r][c].config(text='0', bg='lightgreen')
            self.dirty_cells.remove((r, c))

        self.steps += 1
        self.path.append(self.agent_pos)
        if self.grid[self.agent_pos[0]][self.agent_pos[1]] == 0 and self.agent_pos not in self.dirty_cells:
            self.labels[self.agent_pos[0]][self.agent_pos[1]].config(bg='lightblue')

        self.root.after(DELAY, self.goal_clean)

    def show_result(self):
        result = f"✅ Goal-based cleaning complete!\n🧭 Total Steps taken: {self.steps}\n\n📍 Path taken:\n"
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

        report = f"🧠 Memory Used: {len(self.memory)} cells (not explicitly tracked here)\n"
        report += f"🧼 Initial Dirty Cells: {len(self.path)}\n"
        report += "--- Goal-Based Agent focused only on dirty cells using memory + greedy strategy ---"

        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, result + report)
        self.result_text.config(state='disabled')


# Run the app
root = tk.Tk()
app = GoalBasedVacuumCleaner(root)
root.mainloop()