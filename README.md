# 🧮 Python Calculator Projects

A collection of **5 Python calculator projects** progressing from beginner to GUI level. Each project is self-contained in its own folder with clean, well-documented code.

---

## 📁 Project Structure

```
python-calculator-projects/
│
├── simple/
│   └── simple_calculator.py        # Beginner: basic arithmetic
│
├── advanced/
│   └── advanced_calculator.py      # Intermediate: functions + loop
│
├── scientific/
│   └── scientific_calculator.py    # Intermediate: math module
│
├── gui/
│   └── gui_calculator.py           # Advanced: Tkinter desktop app
│
├── bmi/
│   └── bmi_calculator.py           # Real-world: BMI calculation
│
└── README.md
```

---

## 🚀 Projects Overview

### 1. Simple Calculator (`simple/`)
**Level:** Beginner

Performs the four basic arithmetic operations using `if/elif` logic.

```bash
python simple/simple_calculator.py
```

**Concepts covered:** variables, `input()`, `float()`, `if/elif`, basic operators

---

### 2. Advanced Calculator (`advanced/`)
**Level:** Beginner → Intermediate

Same operations, but refactored into clean reusable functions with a menu loop.

```bash
python advanced/advanced_calculator.py
```

**Concepts covered:** functions, `def`, return values, dictionaries, loops, input validation

---

### 3. Scientific Calculator (`scientific/`)
**Level:** Intermediate

Uses Python's built-in `math` module for square roots, powers, trig, and logarithms.

```bash
python scientific/scientific_calculator.py
```

**Concepts covered:** `import math`, `math.sqrt/sin/cos/tan/log`, `math.radians()`, `try/except`

---

### 4. GUI Calculator (`gui/`)
**Level:** Advanced

A fully functional desktop calculator with:
- Dark-themed UI
- Chained operations
- Keyboard shortcut support
- Backspace and sign toggle

```bash
python gui/gui_calculator.py
```

**Concepts covered:** `tkinter`, OOP, event binding, widget layout with `.grid()`

> **Note:** `tkinter` is included with Python on Windows and macOS. On Linux, install it with:
> ```bash
> sudo apt install python3-tk
> ```

---

### 5. BMI Calculator (`bmi/`)
**Level:** Beginner → Intermediate

Calculates Body Mass Index and classifies it using WHO standard categories. Includes an ASCII progress bar visualization.

```bash
python bmi/bmi_calculator.py
```

**Formula:** `BMI = weight(kg) / height(m)²`

**Concepts covered:** formula-based computation, comparison logic, f-strings, real-world application

---

## ⚡ Getting Started

### Prerequisites

- Python 3.10+ recommended
- No third-party packages required

### Installation

```bash
git clone https://github.com/your-username/python-calculator-projects.git
cd python-calculator-projects
```

### Run any project

```bash
python simple/simple_calculator.py
python advanced/advanced_calculator.py
python scientific/scientific_calculator.py
python gui/gui_calculator.py
python bmi/bmi_calculator.py
```

---

## ⌨️ Keyboard Shortcuts (GUI Calculator)

| Key           | Action          |
|---------------|-----------------|
| `0–9`         | Input digits    |
| `.`           | Decimal point   |
| `+` `-` `*` `/` | Operators     |
| `Enter`       | Calculate `=`   |
| `Backspace`   | Delete last digit |
| `Escape`      | Clear all (AC)  |

---

## 📚 Recommended Learning Path

```
1. Simple Calculator
2. Advanced Calculator
3. BMI Calculator
4. Scientific Calculator
5. GUI Calculator
```

---

## 🛠️ Recommended Tools

| Tool | Link |
|------|------|
| VS Code | https://code.visualstudio.com |
| PyCharm | https://www.jetbrains.com/pycharm/ |
| Jupyter Notebook | https://jupyter.org |
| Replit (online) | https://replit.com |

---

## 🗺️ Roadmap

- [ ] Unit converter
- [ ] Currency converter (with live API)
- [ ] Web calculator using Flask
- [ ] Voice input support
- [ ] Calculation history with file export

---

## 📄 License

MIT — free to use, modify, and distribute.
