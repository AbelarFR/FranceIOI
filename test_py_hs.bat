@echo off
REM Vérifie si un programme Python et un programme Haskell donnent le même résultat.

if "%~2" == "" (set input=CON) else (set input=%2)

REM Exécute le programme Python.
@echo Test %1.py
py %1.py < %input% > output_py.txt

REM Exécute le programme Haskell.
@echo Test %1.hs
runghc %1.hs < %input% > output_hs.txt

REM Compare les résultats.
fc output_py.txt output_hs.txt
