import tkinter as tk
import random

ROWS = 10
COLS = 10
DELAY = 50  # milliseconds between agent steps


class VacuumCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vacuum Cleaner Agent")

        # Instructions label
        self.instruction_label = tk.Label(root, text="Press ENTER to start cleaning", font=("Arial", 14))
        self.instruction_label.grid(row=0, column=0, columnspan=COLS)

        # Generate random grid with 0s and 1s
        self.grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
        self.labels = [[None for _ in range(COLS)] for _ in range(ROWS)]

        # Grid labels start from row=1 because row=0 is for instructions
        for i in range(ROWS):
            for j in range(COLS):
                label = tk.Label(root, text=str(self.grid[i][j]), width=4, height=2,
                                 font=('Arial', 14), borderwidth=1, relief="solid")
                label.grid(row=i+1, column=j)
                self.labels[i][j] = label

        # Text widget to show results, placed below the grid
        self.result_text = tk.Text(root, height=20, width=COLS * 6, font=("Courier", 10))
        self.result_text.grid(row=ROWS + 2, column=0, columnspan=COLS, pady=10)
        self.result_text.config(state='disabled')

        # Agent's tracking data
        self.current_row = 0
        self.current_col = 0
        self.steps = 0
        self.path = []

        # Bind Enter key to start cleaning
        self.root.bind('<Return>', self.on_enter_press)

    def on_enter_press(self, event):
        # Disable further enter presses until done
        self.root.unbind('<Return>')
        self.instruction_label.config(text="Cleaning started...")
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, "Cleaning in progress...\n")
        self.result_text.config(state='disabled')
        self.root.after(500, self.clean_cell)

    def clean_cell(self):
        i, j = self.current_row, self.current_col
        self.path.append((i, j))
        self.steps += 1

        if self.grid[i][j] == 1:
            self.grid[i][j] = 0
            self.labels[i][j].config(text='0', bg='lightgreen')  # cleaned
        else:
            self.labels[i][j].config(bg='lightblue')  # visited clean cell

        self.current_col += 1
        if self.current_col >= COLS:
            self.current_col = 0
            self.current_row += 1

        if self.current_row < ROWS:
            self.root.after(DELAY, self.clean_cell)
        else:
            self.show_result()

    def show_result(self):
        # Prepare actual path text
        result = f"✅ Cleaning complete!\n🧭 Total Steps taken: {self.steps}\n\n📍 Path taken:\n"
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

        # Compute efficiency and append
        efficiency_report = self.compute_efficiency()

        full_report = result + efficiency_report

        self.result_text.config(state='normal')
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, full_report)
        self.result_text.config(state='disabled')

    def compute_efficiency(self):
        dirty_cells = [(i, j) for i in range(ROWS) for j in range(COLS)
                       if self.labels[i][j].cget('bg') == 'lightgreen']

        if not dirty_cells:
            return "Grid was already clean.\n"

        current = (0, 0)
        unvisited = dirty_cells[:]
        traversal_distance = 0
        optimal_path = []

        while unvisited:
            nearest = min(unvisited, key=lambda pos: abs(current[0] - pos[0]) + abs(current[1] - pos[1]))
            dist = abs(current[0] - nearest[0]) + abs(current[1] - nearest[1])
            traversal_distance += dist
            optimal_path.append(nearest)
            current = nearest
            unvisited.remove(nearest)

        cleaning_actions = len(dirty_cells)
        optimal_steps = traversal_distance + cleaning_actions
        actual_steps = self.steps
        efficiency = (optimal_steps / actual_steps) * 100 if actual_steps else 0

        # Build report string
        report = (
            "--- 🔍 Efficiency Analysis ---\n"
            f"🧼 Dirty Cells: {cleaning_actions}\n"
            f"🚶 Traversal Distance (greedy): {traversal_distance}\n"
            f"🧠 Estimated Optimal Steps (clean + move): {optimal_steps}\n"
            f"🎯 Actual Steps Taken: {actual_steps}\n"
            f"⚡ Efficiency: {efficiency:.2f}%\n\n"
            f"🗺️ Greedy Optimal Path:\n" +
            " → ".join([f"({x},{y})" for x, y in optimal_path]) + "\n"
        )
        return report


# Run the app
root = tk.Tk()
app = VacuumCleanerApp(root)
root.mainloop()