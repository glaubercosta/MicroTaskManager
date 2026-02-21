# PowerShell script to setup the local development environment

Write-Host "--- Initializing MicroTaskManager Environment ---" -ForegroundColor Cyan

# 1. Create Virtual Environment
if (-Not (Test-Path ".venv")) {
    Write-Host "[1/3] Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
} else {
    Write-Host "[1/3] Virtual environment already exists." -ForegroundColor Gray
}

# 2. Upgrade pip and install dependencies
Write-Host "[2/3] Installing dependencies..." -ForegroundColor Yellow
& ".\.venv\Scripts\pip" install --upgrade pip
& ".\.venv\Scripts\pip" install -r requirements-dev.txt

# 3. Setup .env file
if (-Not (Test-Path ".env")) {
    Write-Host "[3/3] Creating .env from .env.example..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
} else {
    Write-Host "[3/3] .env file already exists." -ForegroundColor Gray
}

Write-Host "--- Setup Complete! ---" -ForegroundColor Green
Write-Host "To activate the environment, run: .\.venv\Scripts\Activate.ps1" -ForegroundColor Cyan
