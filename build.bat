@echo off
:: Définir le répertoire du script Python
set SCRIPT_DIR=%~dp0

:: Afficher le répertoire du script pour vérification
echo Répertoire du script : %SCRIPT_DIR%

:: Exécuter le script Python
python "%SCRIPT_DIR%ZENITHS Tools.py"

:: Pauser pour voir les messages de sortie
pause

