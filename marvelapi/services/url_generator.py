import hashlib
import time

class URLGenerator:
    @staticmethod
    def generate_signed_url(base_url, valora, valorb):
        # Generar el timestamp
        timestamp = int(time.time())

        # Crear el string para el hash
        hash_input = f"{timestamp}{valora}{valorb}"

        # Generar el hash MD5
        hash_md5 = hashlib.md5(hash_input.encode()).hexdigest()

        # Construir la URL
        full_url = f"{base_url}&ts={timestamp}&hash={hash_md5}"

        return full_url