import sys
import os
# Añade la raíz del proyecto al path para importar tracker.utils correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import smtplib
from email.message import EmailMessage
from tracker.utils import generate_tracking_link

# Configuración del servidor SMTP (ejemplo con Gmail)
SMTP_SERVER = 'smtp.gmail.com'  # Servidor SMTP de Gmail
SMTP_PORT = 587                 # Puerto para TLS
SMTP_USER = 'brayanvillamizar14@gmail.com'      # Tu correo de envío
SMTP_PASSWORD = 'brayanvillamizar'              # Tu contraseña de aplicación (NO la normal)

def enviar_correo(destinatario, enlaces):
    """
    Envía un correo electrónico con enlaces de tracking personalizados.
    Args:
        destinatario (str): Correo del destinatario.
        enlaces (list): Lista de tuplas (texto, url_tracking) para incluir en el cuerpo del mensaje.
    """
    msg = EmailMessage()
    msg['Subject'] = '¡Descubre Elementalab!'
    msg['From'] = SMTP_USER
    msg['To'] = destinatario

    # Cuerpo del mensaje con los enlaces de tracking
    cuerpo = "Hola, haz clic en los siguientes enlaces:\n\n"
    for texto, url in enlaces:
        cuerpo += f"{texto}: {url}\n"
    msg.set_content(cuerpo)

    # Enviar el correo usando SMTP con TLS
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Inicia conexión segura
        server.login(SMTP_USER, SMTP_PASSWORD)  # Autenticación
        server.send_message(msg)  # Envía el mensaje
        print(f"Correo enviado a {destinatario}")

if __name__ == "__main__":
    # Lista de destinatarios
    correos = [
        "brayan.acevedo@utp.edu.co",
        "posiblecliente23@gmail.com",
        "posiblecliente50@gmail.com"
    ]
    # Lista de enlaces reales a trackear
    enlaces_reales = [
        ("Sitio principal", "https://elementalab.com/"),
        ("Landing", "https://elementalab.com/landing/")
    ]
    # Para cada destinatario, genera enlaces de tracking y envía el correo
    for correo in correos:
        enlaces_tracking = []
        for texto, url in enlaces_reales:
            # Genera el enlace de tracking único para cada destinatario y enlace
            tracking_url = generate_tracking_link(correo, url, domain="http://localhost:8000")
            enlaces_tracking.append((texto, tracking_url))
        enviar_correo(correo, enlaces_tracking)