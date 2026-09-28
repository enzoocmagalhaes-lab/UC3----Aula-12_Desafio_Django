@echo off
setlocal
cd /d "%~dp0"
echo THE WITCHER - Catalogo Django
if exist ".venv\Scripts\python.exe" goto dependencias
where py >nul 2>nul
if errorlevel 1 goto usar_python
py -3 -m venv .venv
if errorlevel 1 goto erro
goto dependencias
:usar_python
where python >nul 2>nul
if errorlevel 1 goto sem_python
python -m venv .venv
if errorlevel 1 goto erro
:dependencias
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto erro
".venv\Scripts\python.exe" manage.py migrate
if errorlevel 1 goto erro
".venv\Scripts\python.exe" manage.py shell -c "from django.contrib.auth import get_user_model; import sys; sys.exit(0 if get_user_model().objects.filter(is_active=True).exists() else 1)"
if not errorlevel 1 goto iniciar
echo Crie um usuario para editar o catalogo. A senha nao aparece ao digitar.
".venv\Scripts\python.exe" manage.py createsuperuser
if errorlevel 1 goto erro
:iniciar
echo.
echo Abra http://127.0.0.1:8000/ no navegador depois que o servidor iniciar.
echo Para encerrar, pressione Ctrl+C.
".venv\Scripts\python.exe" manage.py runserver
if errorlevel 1 goto erro
goto fim
:sem_python
echo Python nao encontrado. Instale Python 3.10 ou superior e tente novamente.
goto erro
:erro
echo.
echo Nao foi possivel concluir. Confira o erro acima e o README.md.
pause
exit /b 1
:fim
endlocal
