@echo off
REM Quick Start Script for ChatBot Project

echo.
echo ========================================
echo   ChatBot - Full Stack Setup
echo ========================================
echo.

REM Check if running in correct directory
if not exist "chatbotapi" (
    echo Error: chatbotapi directory not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

if not exist "chatbotfrontend" (
    echo Error: chatbotfrontend directory not found!
    echo Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Backend Setup
echo.
echo [1/4] Setting up Backend...
echo.

cd chatbotapi

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

cd ..

echo.
echo [2/4] Backend setup complete!
echo.

REM Frontend Setup
echo [3/4] Setting up Frontend...
echo.

cd chatbotfrontend

echo Installing npm dependencies...
if not exist "node_modules" (
    npm install
)

cd ..

echo.
echo [4/4] Frontend setup complete!
echo.

echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   cd chatbotapi
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
echo Terminal 2 (Frontend):
echo   cd chatbotfrontend
echo   npm run dev
echo.
echo Frontend will be available at: http://localhost:5173
echo Backend API will be at: http://localhost:8000
echo.
pause
