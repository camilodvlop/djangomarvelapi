from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.url_generator import URLGenerator
import requests
# Create your views here.
class MarvelCharactersAPIView(APIView):
    def get(self, request):
        # URL del servicio REST externo
        external_service_url = "http://gateway.marvel.com/v1/public/characters"  # Cambiar por la URL real

        try:
            # Llama al servicio externo
            full_url = URLGenerator.generate_signed_url(external_service_url)
            response = requests.get(full_url)
            
            response.raise_for_status()  # Lanza excepción si ocurre un error HTTP

            # Extrae la lista de números
            data = response.json()
                        
            return Response(data, status=200)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"No se pudo conectar al servicio externo: {str(e)}"}, status=500)
        except Exception as e:
            return Response({"error": f"Ocurrió un error: {str(e)}"}, status=500)