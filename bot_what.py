from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def whatsapp_bot():
    mensaje_entrante = request.values.get("Body", "")
    print(f"Mensaje crudo: '{mensaje_entrante}'")  # 👈 Depuración

    mensaje_entrante = mensaje_entrante.lower().strip()

    respuesta = MessagingResponse()
    msg = respuesta.message()

    if "hola" in mensaje_entrante:
        msg.body("¡Hola! soy un bot inteligente creado en Python por un aprendiz SENA. ¿En qué te puedo ayudar hoy?")
    elif "servicios" in mensaje_entrante:
        msg.body("Ofrecemos:\n1. Desarrollo web\n2. Automatización con Python\n3. Análisis de datos")
    elif "adios" in mensaje_entrante:
        msg.body("¡Hasta luego! Que tengas un excelente día.")
    else:
        msg.body("Lo siento, aún estoy aprendiendo. Escribe HOLA o SERVICIOS para ayudarte o ADIOS para despedirte.")

    return str(respuesta)


if __name__=="__main__":
    app.run(port=5000)