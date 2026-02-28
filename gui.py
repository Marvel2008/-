import tkinter as tk
from utils import calculate_bias, interpret_bias
from analyzer import SentimentAnalyzer


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Gender Bias Detector")
        self.root.geometry("600x480")
        self.root.configure(bg="#1e1e1e")

        self.analyzer = SentimentAnalyzer()
        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Аналіз сентименту та гендерної упередженості",
            font=("Helvetica", 16, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        title.pack(pady=15)

        entry_frame = tk.Frame(self.root, bg="#2e2e2e", bd=2, relief=tk.RIDGE)
        entry_frame.pack(pady=10, padx=20, fill="x")

        self.entry = tk.Text(
            entry_frame,
            height=6,
            width=60,
            font=("Helvetica", 12),
            bg="#2e2e2e",
            fg="white",
            insertbackground="white"
        )
        self.entry.pack(padx=5, pady=5)

        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        analyze_btn = tk.Button(
            btn_frame,
            text="Аналіз сентименту",
            command=self.run_sentiment,
            bg="#6fa8ff",       
            fg="black",         
            font=("Helvetica", 12, "bold"),
            width=20,
            bd=0,
            relief=tk.RAISED,
            activebackground="#4a90e2",  
            activeforeground="black"      
        )
        analyze_btn.grid(row=0, column=0, padx=10, pady=5)

        bias_btn = tk.Button(
            btn_frame,
            text="Перевірити гендерну упередженість",
            command=self.run_bias,
            bg="#ff7fa0",       
            fg="black",         
            font=("Helvetica", 12, "bold"),
            width=28,
            bd=0,
            relief=tk.RAISED,
            activebackground="#e94e77",  
            activeforeground="black"      
        )
        bias_btn.grid(row=0, column=1, padx=10, pady=5)

        result_frame = tk.LabelFrame(
            self.root,
            text="Результати",
            font=("Helvetica", 12, "bold"),
            bg="#1e1e1e",
            fg="white",
            padx=10,
            pady=10
        )
        result_frame.pack(padx=20, pady=15, fill="both", expand=True)

        self.result_label = tk.Label(
            result_frame,
            text="Результат з’явиться тут",
            font=("Helvetica", 12),
            bg="#2e2e2e",
            fg="white",
            justify="left",
            anchor="nw",
            bd=2,
            relief=tk.SUNKEN,
            padx=5,
            pady=5
        )
        self.result_label.pack(fill="both", expand=True)

    def get_text(self):
        return self.entry.get("1.0", tk.END).strip()

    def run_sentiment(self):
        text = self.get_text()
        if not text:
            self.result_label.config(text="Введи текст 🙂")
            return
        label, score = self.analyzer.analyze(text)
        self.result_label.config(
            text=f"Sentiment: {label}\nScore: {score:.3f}"
        )

    def run_bias(self):
        text = self.get_text()
        if not text:
            self.result_label.config(text="Введи текст 🙂")
            return
        msg, bias = calculate_bias(self.analyzer, text)
        level = interpret_bias(bias)
        self.result_label.config(
            text=f"{msg}\nBias score: {bias:.3f}\nLevel: {level}"
        )
