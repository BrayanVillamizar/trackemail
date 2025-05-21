from django.http import HttpResponseRedirect
import base64
import os

# Ruta del archivo donde se guardarán los clics
CLICKS_FILE = os.path.join(os.path.dirname(__file__), 'clicks.txt')

def track_click(request, encoded_email, encoded_url):
    """
    Vista de Django para trackear clics en enlaces enviados por correo.
    Decodifica el correo y la URL desde la URL, registra el clic en un archivo y redirige al enlace real.
    Args:
        request: Objeto HttpRequest de Django.
        encoded_email (str): Email codificado en base64 urlsafe.
        encoded_url (str): URL codificada en base64 urlsafe.
    Returns:
        HttpResponseRedirect: Redirección al enlace real o a la home si hay error.
    """
    try:
        # Decodifica el email y la URL
        email = base64.urlsafe_b64decode(encoded_email.encode()).decode()
        url = base64.urlsafe_b64decode(encoded_url.encode()).decode()
    except Exception:
        # Si hay error de decodificación, redirige a la home
        return HttpResponseRedirect('/')
    # Registra el clic en el archivo clicks.txt
    with open(CLICKS_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{email} - {url}\n")
    # Redirige al enlace real
    return HttpResponseRedirect(url)