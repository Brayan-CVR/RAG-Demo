# 🚀 Getting Started

## 📦 Requirements

- Python 3.13 or higher.
- [Poetry](https://python-poetry.org/docs/#installation) installed.

## 🔌 Installation

- First check if you have Poetry in your global Python version:

```bash
poetry --version
# (Poetry (version 2.1.3)) <--- Expected result.
```

- If not installed:

```bash
pip install poetry
```

- Follow these steps to install dependencies, and run the project:

```bash
# Configure Poetry to create the virtual environment inside the project folder
poetry config virtualenvs.in-project true

# Install dependencies
poetry install
```

- This create the virtual enviroment in your project forlder. 

## ✅ Execution 

- Finally, to execute the project run:

```bash
poetry run python src/main.py 
```

## 📝 Add new libraries

```bash
poetry add pandas
```

## ❌ Remove libraries

```bash
poetry remove pandas
```