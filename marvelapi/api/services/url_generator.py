import hashlib
import time
from decouple import config

class URLGenerator:
    @staticmethod
    def generate_signed_url(base_url):
        # Generar el timestamp
        timestamp = int(time.time())
        valora = config('MYSECRETKEY', default='default_valora')
        valorb = config('MYPUBLICKEY', default='default_valorb')

        # Crear el string para el hash
        hash_input = f"{timestamp}{valora}{valorb}"

        # Generar el hash MD5
        hash_md5 = hashlib.md5(hash_input.encode()).hexdigest()

        # Construir la URL
        full_url = f"{base_url}?apikey={valorb}&ts={timestamp}&hash={hash_md5}"

        return full_url