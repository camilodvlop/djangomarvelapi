from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
# Create your views here.
class MarvelCharactersAPIView(APIView):
    def get(self, request):
        # URL del servicio REST externo
        external_service_url = "https://api.example.com/numbers"  # Cambiar por la URL real

        try:
            # Llama al servicio externo
            response = requests.get(external_service_url)
            response.raise_for_status()  # Lanza excepción si ocurre un error HTTP

            # Extrae la lista de números
            data = response.json()
            numbers = data.get("numbers", [])

            if not numbers or not isinstance(numbers, list):
                return Response({"error": "La lista de números no es válida o está vacía"}, status=400)

            # Calcula el menor valor
            min_value = min(numbers)

            return Response({"min_value": min_value}, status=200)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"No se pudo conectar al servicio externo: {str(e)}"}, status=500)
        except Exception as e:
            return Response({"error": f"Ocurrió un error: {str(e)}"}, status=500)