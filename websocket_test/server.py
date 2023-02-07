#!/usr/bin/env python
import asyncio
import websockets
#from pywinauto.application import Application
        
async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message)

# async def run_ramen(websocket):
#     raman = Application(backend="uia").start("C:\Program Files\HAMAMATSU Photonics\C13560\C13560_OperationSoftware\C13560_OperationSoftware.exe")
#     password = raman.C13560OperationSoftware.child_window(auto_id="textBox1", control_type="Edit").wrapper_object()
#     password.type_keys("test")
#     raman.C13560OperationSoftware.child_window(title="OK", auto_id="button1", control_type="Button").wrapper_object().click()
#     await websocket.send("Finshed running")

async def simulate_ramen(websocket):
    print("Simulating opening ramen app")
    with open('../small/people.csv', 'r') as f:
        await websocket.send(f.read())
    
    print("Finished")

async def main():
    print("Sever started")
    async with websockets.serve(simulate_ramen, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())