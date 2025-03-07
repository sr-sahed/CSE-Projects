import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://example.com/socket") as websocket:
        await websocket.send("Hello!")
        response = await websocket.recv()
        print(response)

asyncio.run(hello())
