#!/usr/bin/env python

import asyncio
import websockets
import csv
import time

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        data = await websocket.recv()
        with open("test.bin", 'wb') as f:
            f.write(data)

def dump_data(raw_data: list):
    with open("client_test.csv", 'w') as f:
        f.writelines(raw_data)

async def get_csv():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Ping! CSV please!")
        raw_data = await websocket.recv()
        print(raw_data)
        

async def main():
    await get_csv()
    print("Client finished")

asyncio.run(main())