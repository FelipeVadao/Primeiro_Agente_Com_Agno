# 1 - IMPORTS =======================================================================
import requests
import json
from pprint import pprint

AGENT_ID = "agente-de-pdf"
ENDPOINT = f'http://localhost:7777/agents/{AGENT_ID}/runs'


# 2 - Conexão com o Agno (SERVER) ===================================================

def get_response_stream(message: str):
    response = requests.post(
        url=ENDPOINT,
        data={
            "message": message,
            "stream": True,
        },
        stream=True
    )
    
# 2.1 - Streaming (processamento) =====================================================
    for line in response.iter_lines():
        if line:
            # Parse Server-Sent Events
            if line.startswith(b'data: '):
                data = line[6:]  # Remove the 'data: ' prefix
                try:
                    event = json.loads(data)
                    yield event
                except json.JSONDecodeError:
                    continue

# 3 - Printa a resposta =============================================================

# 4 - RUN (loop) ====================================================================
if __name__ == "__main__":
    message = input("Digite uma mensagem: ")

    response = get_response_stream(message)

    for event in response:
        print(event)
