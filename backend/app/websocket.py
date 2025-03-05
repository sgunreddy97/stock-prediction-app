import asyncio
import websockets
import json
import random

connected_clients = set()

async def stock_price_simulator():
    """Simulates real-time stock price updates."""
    while True:
        stock_data = {
            "ticker": "AAPL",
            "price": round(random.uniform(140, 160), 2),
            "timestamp": asyncio.get_event_loop().time()
        }
        message = json.dumps(stock_data)
        await asyncio.gather(*[client.send(message) for client in connected_clients])
        await asyncio.sleep(1)

async def websocket_handler(websocket, path):
    """Handles new WebSocket connections."""
    connected_clients.add(websocket)
    try:
        async for _ in websocket:
            pass
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(websocket_handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(stock_price_simulator())
asyncio.get_event_loop().run_forever()
