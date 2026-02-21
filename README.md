# MicroTaskManager

A simple micro task manager pilot project. Professional structure with FastAPI, SQLite, and SEprocess.

## Getting Started

### 1. Prerequisities
- Python 3.10+

### 2. Setup Environment
Run the automatic setup script (Windows PowerShell):
```powershell
.\setup.ps1
```
This will create a `.venv`, install dependencies, and setup your `.env` file.

### 3. Activate Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Run the API
```powershell
uvicorn main:app --reload
```

## Quality Gates
We enforce high quality standards via:
- **Linting**: `ruff check .`
- **Testing**: `python -m pytest`
- **Typing**: `mypy .`
- **Similiarity**: `pylint --disable=all --enable=similarities .`
