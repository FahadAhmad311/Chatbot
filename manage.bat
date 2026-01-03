@echo off
REM ChatBot Project Management Script

setlocal enabledelayedexpansion

if "%1"=="" (
    echo Usage: manage.bat [command]
    echo.
    echo Commands:
    echo   install   - Install all dependencies
    echo   backend   - Start backend server
    echo   frontend  - Start frontend server
    echo   migrate   - Run database migrations
    echo   clean     - Clean temporary files
    echo.
    exit /b 0
)

if "%1"=="install" (
    echo Installing dependencies...
    cd chatbotapi
    pip install -r requirements.txt
    cd ..\chatbotfrontend
    npm install
    cd ..
    echo Installation complete!
    goto end
)

if "%1"=="backend" (
    echo Starting backend server...
    cd chatbotapi
    python manage.py runserver
    goto end
)

if "%1"=="frontend" (
    echo Starting frontend server...
    cd chatbotfrontend
    npm run dev
    goto end
)

if "%1"=="migrate" (
    echo Running migrations...
    cd chatbotapi
    python manage.py makemigrations
    python manage.py migrate
    cd ..
    echo Migrations complete!
    goto end
)

if "%1"=="clean" (
    echo Cleaning temporary files...
    cd chatbotapi
    for /d %%D in (__pycache__ .pytest_cache) do (
        if exist %%D rmdir /s /q %%D
    )
    cd ..\chatbotfrontend
    if exist node_modules rmdir /s /q node_modules
    if exist dist rmdir /s /q dist
    cd ..
    echo Cleanup complete!
    goto end
)

echo Unknown command: %1
echo Run 'manage.bat' without arguments for help

:end
