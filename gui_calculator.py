"""
GUI Calculator — Tkinter
-------------------------
A fully functional desktop calculator with a clean grid layout.
Supports arithmetic, percentage, sign toggle, and keyboard input.

Requirements:
    tkinter (included with standard Python on Windows/macOS/Linux)

Usage:
    python gui_calculator.py
"""

import tkinter as tk
from tkinter import font as tkfont


# ── Constants ─────────────────────────────────────────────────────────────────

BG         = "#1e1e2e"
DISPLAY_BG = "#181825"
BTN_NUM    = "#313244"
BTN_OP     = "#45475a"
BTN_EQ     = "#a6e3a1"
BTN_CLEAR  = "#f38ba8"
BTN_SPEC   = "#89b4fa"
FG_LIGHT   = "#cdd6f4"
FG_DARK    = "#1e1e2e"
FG_EXPR    = "#6c7086"
FONT_DISP  = ("Courier New", 32, "normal")
FONT_EXPR  = ("Courier New", 12)
FONT_BTN   = ("Segoe UI", 16, "bold")


# ── Calculator logic ──────────────────────────────────────────────────────────

class CalculatorLogic:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current   = "0"
        self.expression = ""
        self.operator  = None
        self.prev      = None
        self.just_eval = False

    def input_digit(self, d: str):
        if self.just_eval:
            self.current = d
            self.expression = ""
            self.just_eval = False
        elif self.current == "0":
            self.current = d
        elif len(self.current) < 15:
            self.current += d

    def input_decimal(self):
        if self.just_eval:
            self.current = "0."
            self.just_eval = False
        elif "." not in self.current:
            self.current += "."

    def input_operator(self, op: str):
        if self.operator and not self.just_eval:
            result = self._eval(float(self.prev), float(self.current), self.operator)
            self.expression = self._fmt(result) + f" {op} "
            self.prev = result
            self.current = self._fmt(result)
        else:
            self.prev = float(self.current)
            self.expression = self.current + f" {op} "
        self.operator  = op
        self.just_eval = True

    def calculate(self) -> str | None:
        if not self.operator or self.prev is None:
            return None
        full_expr = self.expression + self.current
        result = self._eval(float(self.prev), float(self.current), self.operator)
        if result is None:
            self.reset()
            return "Error"
        self.expression = full_expr + " ="
        self.current   = self._fmt(result)
        self.operator  = None
        self.prev      = None
        self.just_eval = True
        return self.current

    def backspace(self):
        if self.just_eval or len(self.current) <= 1:
            self.current   = "0"
            self.just_eval = False
        else:
            self.current = self.current[:-1]

    def toggle_sign(self):
        if self.current != "0":
            self.current = self.current[1:] if self.current.startswith("-") else "-" + self.current

    def percentage(self):
        self.current = self._fmt(float(self.current) / 100)

    # ── Helpers ──

    @staticmethod
    def _eval(a: float, b: float, op: str) -> float | None:
        if op == "+": return a + b
        if op == "−": return a - b
        if op == "×": return a * b
        if op == "÷": return None if b == 0 else a / b
        return b

    @staticmethod
    def _fmt(n: float) -> str:
        if isinstance(n, float) and n.is_integer() and abs(n) < 1e15:
            return str(int(n))
        s = f"{n:.10f}".rstrip("0").rstrip(".")
        return s


# ── GUI ───────────────────────────────────────────────────────────────────────

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg=BG)

        self.logic = CalculatorLogic()
        self._build_ui()
        self._bind_keys()

    # ── Display ──────────────────────────────────────────────────────────────

    def _build_ui(self):
        # Expression label
        self.expr_var = tk.StringVar(value="")
        tk.Label(self, textvariable=self.expr_var, bg=DISPLAY_BG, fg=FG_EXPR,
                 font=FONT_EXPR, anchor="e", width=20, padx=16, pady=4
                 ).grid(row=0, column=0, columnspan=4, sticky="ew")

        # Main display
        self.disp_var = tk.StringVar(value="0")
        tk.Label(self, textvariable=self.disp_var, bg=DISPLAY_BG, fg=FG_LIGHT,
                 font=FONT_DISP, anchor="e", width=12, padx=16, pady=12
                 ).grid(row=1, column=0, columnspan=4, sticky="ew")

        # Button layout: (label, row, col, colspan, style)
        buttons = [
            ("AC",  2, 0, 1, "clear"),  ("+/−", 2, 1, 1, "spec"),
            ("%",   2, 2, 1, "spec"),   ("÷",   2, 3, 1, "op"),
            ("7",   3, 0, 1, "num"),    ("8",   3, 1, 1, "num"),
            ("9",   3, 2, 1, "num"),    ("×",   3, 3, 1, "op"),
            ("4",   4, 0, 1, "num"),    ("5",   4, 1, 1, "num"),
            ("6",   4, 2, 1, "num"),    ("−",   4, 3, 1, "op"),
            ("1",   5, 0, 1, "num"),    ("2",   5, 1, 1, "num"),
            ("3",   5, 2, 1, "num"),    ("+",   5, 3, 1, "op"),
            ("0",   6, 0, 2, "num"),    (".",   6, 2, 1, "num"),
            ("=",   6, 3, 1, "eq"),
        ]

        styles = {
            "num":   (BTN_NUM, FG_LIGHT),
            "op":    (BTN_OP,  FG_LIGHT),
            "eq":    (BTN_EQ,  FG_DARK),
            "clear": (BTN_CLEAR, FG_DARK),
            "spec":  (BTN_SPEC, FG_DARK),
        }

        for (text, row, col, span, style) in buttons:
            bg, fg = styles[style]
            anchor = "w" if text == "0" and span == 2 else "center"
            padx   = (22, 0) if text == "0" and span == 2 else 0
            btn = tk.Button(
                self, text=text, bg=bg, fg=fg,
                activebackground=bg, activeforeground=fg,
                font=FONT_BTN, relief="flat", cursor="hand2",
                command=lambda t=text: self._on_button(t)
            )
            btn.grid(row=row, column=col, columnspan=span,
                     sticky="nsew", padx=2, pady=2, ipady=16)

        for r in range(2, 7):
            self.rowconfigure(r, weight=1)
        for c in range(4):
            self.columnconfigure(c, weight=1)

    # ── Keyboard ─────────────────────────────────────────────────────────────

    def _bind_keys(self):
        for d in "0123456789":
            self.bind(d, lambda e, d=d: self._on_button(d))
        self.bind(".", lambda e: self._on_button("."))
        self.bind("+", lambda e: self._on_button("+"))
        self.bind("-", lambda e: self._on_button("−"))
        self.bind("*", lambda e: self._on_button("×"))
        self.bind("/", lambda e: self._on_button("÷"))
        self.bind("<Return>",    lambda e: self._on_button("="))
        self.bind("<KP_Enter>",  lambda e: self._on_button("="))
        self.bind("<BackSpace>", lambda e: self._on_button("⌫"))
        self.bind("<Escape>",    lambda e: self._on_button("AC"))

    # ── Button handler ────────────────────────────────────────────────────────

    def _on_button(self, label: str):
        L = self.logic
        if label.isdigit():
            L.input_digit(label)
        elif label == ".":
            L.input_decimal()
        elif label in ("+", "−", "×", "÷"):
            L.input_operator(label)
        elif label == "=":
            L.calculate()
        elif label == "AC":
            L.reset()
        elif label == "+/−":
            L.toggle_sign()
        elif label == "%":
            L.percentage()
        elif label == "⌫":
            L.backspace()
        self._refresh()

    def _refresh(self):
        self.disp_var.set(self.logic.current)
        self.expr_var.set(self.logic.expression)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
