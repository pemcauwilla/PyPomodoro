# PyPomodoro

A desktop Pomodoro timer and task manager built with Python and PyQt6.

> **Note:** This project was created for educational purposes to learn the fundamentals of **PyQt** and to practice implementing the **Model-View-Controller (MVC)** and **Observer** design patterns in a desktop application.

---

## Features

- **Pomodoro Timer**: Classic 25-minute work intervals alternating with 5-minute short breaks and 15-minute long breaks (every 4 cycles).
- **Task Management**: Create tasks with estimated durations, select an active task, and track completed Pomodoro cycles.
- **Task History & Filtering**: Browse past tasks, toggle sort order, and filter by month, day of the week, or specific date.
- **Custom Theming**: Modular QSS styling system with centralized color palettes and font sizes.

---

## How It Works

PyPomodoro is structured around the **MVC** pattern combined with the **Observer** pattern to decouple data storage, business logic, and UI rendering:

### 1. Model (`models/task_model.py`)
- Manages an embedded **SQLite** database (`pomodoro.db`) to store tasks (`id`, `name`, `date`, `duration`).
- Extends the `Subject` class in the Observer pattern.
- Whenever tasks are added or deleted, it invokes `self.notify()`, notifying all registered observers.

### 2. View (`views/`)
- Built using **PyQt6** widgets and layouts.
- Divided into main screens managed by a `QStackedWidget`:
  - `PomodoroView`: Displays the timer, state cards (*Pomodoro*, *Small Break*, *Long Break*), current task status, and task list.
  - `HistoryView`: Displays the task archive with search and date filtering options.
  - `AddTaskDialog`: Modal dialog to input task details.
- Views implement the `Observer` interface (`refresh_data()`) and register with `TaskModel`. When the model updates, views automatically refresh their UI elements.

### 3. Controller (`controllers/`)
- **`MainViewController`**: Orchestrates navigation between the timer view and history view.
- **`PomodoroController`**: Drives the timer loop using `QTimer`, manages the timer state machine (`WORK` ➔ `SHORT_BREAK` / `LONG_BREAK`), tracks elapsed time, and handles user interactions (start/pause, task selection, deletion).
- **`HistoryController`**: Handles filter interactions (month, weekday, specific date) and sorting logic for the history screen.

---

## Project Structure

```text
PyPomodoro/
├── app.py                      # Application entry point
├── assets/                     # QSS stylesheets and StyleManager
├── controllers/                # MVC Controllers (Pomodoro, History, Main)
│   ├── history_controller.py
│   ├── main_controller.py
│   └── pomodoro_controller.py
├── core/                       # Observer pattern base classes (Subject, Observer)
│   ├── observer.py
│   └── subject.py
├── models/                     # SQLite model and database file
│   ├── pomodoro.db
│   └── task_model.py
├── views/                      # PyQt6 Views and UI components
│   ├── add_task_dialog.py
│   ├── history_view.py
│   ├── main_window.py
│   ├── pomodoro_view.py
│   └── components/
└── readme.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pemcauwilla/PyPomodoro.git
   cd PyPomodoro
   ```

2. Install dependencies:
   ```bash
   pip install PyQt6 qtawesome
   ```

3. Launch the application:
   ```bash
   python app.py
   ```

---

*This README was generated with AI.*