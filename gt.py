import asyncio
import sys

msg = sys.argv[1]
all = []

def add_1():
    f = open("lol")
    txt = f.read()
    f.close()
    
    rep = int(txt) + 1

    f = open("lol", "w")
    f.write(str(rep))
    f.close()

c = 1
async def tcp_echo_client(message):
    global c
    global all
    reader, writer = await asyncio.open_connection(
        '0.0.0.0', 5556)


    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()
    while 1:

        data = await reader.read(200)
        #print(data)
        #print(f'Received: {data.decode()!r}')
        #print(data)
        try:
            txt = str(data).split("[")[1]
            #print(txt)
            txt = txt.split("]")[0]
            #print(txt)
            txt = "[" + txt + "]"
            #print(txt)
            c -= 1
            tab = eval(txt)
            all.append(tab)
        except:
            z = 1
            #print("error")

        #print('Close the connection')
        #writer.close()
        #await writer.wait_closed()


import time
asyncio.run(tcp_echo_client("start"))
while (1):
    asyncio.run(tcp_echo_client(""))
    time.sleep(0.1)
