import base64

def generate_tracking_link(email, url, domain="http://localhost:8000"):
    """
    Genera un enlace de tracking único para un destinatario y un enlace destino.
    Args:
        email (str): Correo del destinatario.
        url (str): Enlace real de destino.
        domain (str): Dominio donde está corriendo el servidor de tracking.
    Returns:
        str: Enlace de tracking completo para insertar en el correo.
    """
    encoded_email = base64.urlsafe_b64encode(email.encode()).decode()
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode()
    return f"{domain}/track/{encoded_email}/{encoded_url}/"
