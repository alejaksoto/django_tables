import json
from multiprocessing import util
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import logging
from dotenv import load_dotenv
from rest_framework import generics, status, response
from django.views.decorators.csrf import csrf_exempt
import requests
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

# Validar que API_TOKEN esté configurado
if not API_TOKEN:
    raise ValueError("La variable de entorno 'API_TOKEN' no está configurada.")

# Vista para suscibir el webhook
def subscribe_to_webhooks(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Método no permitido. Solo se permite GET.'}, status=405)

    business_token = request.GET.get('business_token')  # Token del negocio
    waba_id = request.GET.get('waba_id')  # ID de la cuenta WABA

    if not business_token or not waba_id:
        return JsonResponse({'error': 'Se requieren "business_token" y "waba_id".'}, status=400)

    url = f'https://graph.facebook.com/v21.0/{waba_id}/subscribed_apps'
    headers = {
        'Authorization': f'Bearer {business_token}',
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 2xx
        return JsonResponse({'success': True})
    except requests.RequestException as e:
        logging.error(f"Error al suscribir el webhook: {e}")
        return JsonResponse({'error': 'Error al suscribir el webhook.'}, status=500)

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            object_type = body.get("object")

            if object_type == "whatsapp_business_account":
                for entry in body.get("entry", []):
                    changes = entry.get("changes", [])
                    for change in changes:
                        if change.get("field") == "messages":
                            messages = change.get("value", {}).get("messages", [])
                            if messages and messages[0].get("type") == "text":
                                from_number = messages[0].get("from")
                                phone_id = change.get("value", {}).get("metadata", {}).get("phone_number_id")

                                # Enviar mensaje de bienvenida
                                try:
                                    response = requests.post(
                                        f"https://graph.facebook.com/v21.0/{phone_id}/messages",
                                        json={
                                            "messaging_product": "whatsapp",
                                            "to": from_number,
                                            "text": {"body": "¡Hola! Bienvenido a nuestro servicio de pruebas de WhatsApp."}
                                        },
                                        headers={
                                            "Authorization": f"Bearer {API_TOKEN}",
                                            "Content-Type": "application/json"
                                        }
                                    )
                                    response.raise_for_status()  # Lanza una excepción si el código de estado no es 2xx
                                    logging.info("Mensaje de bienvenida enviado: %s", response.json())
                                except requests.RequestException as e:
                                    logging.error("Error al enviar el mensaje: %s", e)
                                    return JsonResponse({"error": "Error al enviar el mensaje."}, status=500)

            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            logging.error("Error al decodificar el JSON del cuerpo de la solicitud.")
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            return JsonResponse({"error": "Error interno del servidor."}, status=500)

    return HttpResponse("Método no permitido", status=405)
