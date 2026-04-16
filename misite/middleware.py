"""
Middleware personalizado para controlar caché
"""


class NoCache(object):
    """
    Middleware que desactiva el caché de todas las páginas
    Agrega headers para asegurar que no se cacheen datos
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Headers para desactivar caché completo
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
