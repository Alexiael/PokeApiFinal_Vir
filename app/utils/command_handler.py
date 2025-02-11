# app/utils/command_handler.py

import subprocess

def run_command(command: str) -> str:
    """
    Ejecuta un comando en la terminal y devuelve su salida como string.
    Evitamos shell=True para reducir riesgos de inyección.
    """
    # Dividimos el comando en una lista para subprocess.run
    cmd_list = command.split()
    process = subprocess.run(cmd_list, capture_output=True, text=True)
    
    # Podríamos controlar errores con process.returncode, si deseamos
    if process.returncode != 0:
        raise RuntimeError(f"Error al ejecutar '{command}': {process.stderr}")
    
    return process.stdout

