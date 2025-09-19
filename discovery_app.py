from flask import Flask, Response

app = Flask(__name__)

# ¡Esta es la variable que TÚ actualizas manualmente cada vez que reinicias ngrok!
CURRENT_BACKEND_URL = "https://74f2517902b9.ngrok-free.app"

@app.route('/api/get-backend-url', methods=['GET'])
def get_backend_url():
    xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<ServerUrlResponse>
    <Url>{CURRENT_BACKEND_URL}</Url>
</ServerUrlResponse>"""
    return Response(xml_response, mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
