import asyncio
import websockets
import escpos

domain  = 'localhost'
port    = 8765
printer = '/dev/usb/lp0'

async def hello(websocket, path):
    while(True):
        data = await websocket.recv()
        recipe = escpos.json_to_escpos(data)

        file = open(printer, 'wb')
        file.write(b''.join(recipe))
        file.close()
        # print(b''.join(recipe))


start_server = websockets.serve(hello, domain, port)
asyncio.get_event_loop().run_until_complete(start_server)
print(f"Running on {domain}:{port}")
asyncio.get_event_loop().run_forever()
