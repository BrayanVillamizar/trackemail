import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tracker.utils import generate_tracking_link

# Ejemplo de uso para generar enlaces de tracking para varios destinatarios y enlaces
if __name__ == "__main__":
    correos = [
        "posiblecliente1@gmail.com",
        "posiblecliente23@gmail.com",
        "posiblecliente50@gmail.com"
    ]
    enlaces = [
        "https://elementalab.com/",
        "https://elementalab.com/landing/"
    ]
    for correo in correos:
        for enlace in enlaces:
            tracking = generate_tracking_link(correo, enlace, domain="http://localhost:8000")
            print(f"Para {correo}: {tracking}")
