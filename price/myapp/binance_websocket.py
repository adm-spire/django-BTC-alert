# binance_websocket.py

import json
import threading
import websocket
import requests

# URL of the Django view that will handle alert processing
ALERT_PROCESSING_URL = 'http://localhost:8000/alerts/process/'  # Update with your actual URL

def on_message(ws, message):
    data = json.loads(message)
    current_price = float(data['k']['c'])
    print(f"Bitcoin price: {current_price}")

    # Send the current price to the Django view
    response = requests.post(ALERT_PROCESSING_URL, json={'current_price': current_price})
    if response.status_code == 200:
        print("Alert processing completed successfully.")
    else:
        print("Failed to process alerts.")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps({
            "method": "SUBSCRIBE",
            "params": [
                "btcusdt@kline_1m"
            ],
            "id": 1
        }))
    threading.Thread(target=run).start()

def start_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@kline_1m",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    start_websocket()



