"""
Middleware personalizado para controlar caché
"""


class NoCache(object):
    """
    Middleware inteligente que:
    - Desactiva caché para HTML (content-type text/html)
    - Permite caché para archivos estáticos (CSS, JS, imágenes)
    - Mejora performance del servidor y experiencia del usuario
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        content_type = response.get('Content-Type', '')
        
        # Solo desactivar caché para HTML
        if 'text/html' in content_type:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        else:
            # Permitir caché de 24 horas para archivos estáticos
            response['Cache-Control'] = 'public, max-age=86400'
        
        return response
