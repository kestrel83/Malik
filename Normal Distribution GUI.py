import tkinter as tk
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.data_label = tk.Label(self, text="Enter data:")
        self.data_label.pack()

        self.data_entry = tk.Entry(self)
        self.data_entry.pack()

        self.mean_label = tk.Label(self, text="Enter mean:")
        self.mean_label.pack()

        self.mean_entry = tk.Entry(self)
        self.mean_entry.pack()

        self.sd_label = tk.Label(self, text="Enter standard deviation:")
        self.sd_label.pack()

        self.sd_entry = tk.Entry(self)
        self.sd_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    def calculate(self):
        data = [float(x) for x in self.data_entry.get().split(",")]
        mean = float(self.mean_entry.get())
        sd = float(self.sd_entry.get())

        total_prob = 0
        for d in data:
            prob = norm.pdf(d, mean, sd)
            total_prob += prob

        x = list(range(int(mean-4*sd), int(mean+4*sd)))
        y = [norm.pdf(i, mean, sd) for i in x]

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title('Normal Distribution of Data')
        self.canvas.draw()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
