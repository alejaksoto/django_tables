from django.urls import path
from . import views,webhooks

urlpatterns = [
    path('', views.home, name='home'),
    path('embedded-callback/', views.embedded_callback, name='embedded_callback'),
    path('login/', views.login, name='login'),
    path('whatsapp/', views.whatsapp_verify, name='whatsapp_verify'),
    path('whatsapp-message-handler/', views.whatsapp_message_handler, name='whatsapp_message_handler'),
    path('subscribe_to_webhooks', webhooks.subscribe_to_webhooks, name='subscribe_to_webhooks'),
    path('whatsapp_webhook', webhooks.whatsapp_webhook, name='whatsapp_webhook'),
    path('send-message/', views.send_message_view, name='send_message'),
    path('register/', views.register_company, name='register_company'),
    path('exchange-token/', views.exchange_token, name='exchange_token'),
    path('register-phone/', views.register_phone_number, name='register_phone_number'),
    path('obtener-datos-cliente/', views.obtener_datos_cliente, name='obtener_datos_cliente'),
    path('process_signup_event/', views.process_signup_event, name='process_signup_event'),
    path('meta-callback/', views.meta_callback, name='meta_callback'),
]
   