import random
import string
import hashlib
import sys
import os
import uvicorn


listen = "0.0.0.0"
folder = "/servervol"
datafile = "data.txt"
checksumfile = "checksum.txt"

async def server(scope, receive, send):
    # Server
    while True:
        event = await receive()
        if event['type'] == 'http.request':
            # Read data and checksum from files
            data = open(folder + "/" + datafile, "r").read()
            checksum = open(folder + "/" + checksumfile, "r").read()
            
            # Send data and checksum
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [
                    [b'content-type', b'text/plain'],
                ]
            })
            await send({
                'type': 'http.response.body',
                'body': (data + "\n" + checksum).encode('utf-8'),
            })
        else:
            print("Unknown event type: " + event['type'])
            break

def generate_data(size=1024):
    # Generate random data
    data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
    return data


def generate_checksum(data):
    # Generate checksum for data
    checksum = hashlib.md5(data.encode('utf-8')).hexdigest()
    return checksum
    
    
def main(port = 8000):
    print("Generating data...")
    data = generate_data()
    file = open(folder + "/" + datafile, "w+")
    file.write(data)
    file.close()
    
    print("Calculating checksum...")
    checksum = generate_checksum(data)
    file = open(folder + "/" + checksumfile, "w+")
    file.write(checksum)
    file.close()
    
    print("Data and checksum generated, starting server...")
    
    config = uvicorn.Config('server:server', host=listen, port=port, log_level="debug")
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main(sys.argv[1])
