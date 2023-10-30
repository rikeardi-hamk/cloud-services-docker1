import requests
import sys
import hashlib


folder = "/clientvol"
datafile = "data.txt"
checksumfile = "checksum.txt"

def generate_checksum(data):
    # Generate checksum for data
    checksum = hashlib.md5(data.encode('utf-8')).hexdigest()
    return checksum


def main(server):
    # Get data and checksum from server
    print("Getting data from server...")
    try:
        response = requests.get(server)
    except:
        print("Failed to connect to server!")
        sys.exit(1)
    data, checksum = response.text.split("\n")
    
    # Write data and checksum to files
    print("Writing data to file...")
    file = open(folder + "/" + datafile, "w+")
    file.write(data)
    file.close()
    
    print("Writing checksum to file...")
    file = open(folder + "/" + checksumfile, "w+")
    file.write(checksum)
    file.close()
    
    print("Verifying checksum...")
    if generate_checksum(data) == checksum:
        print("Checksum verified!")
    else:
        print("Checksum verification failed!")
        sys.exit(1)
    
    print("Done!")

if __name__ == "__main__":
    main("http://" + sys.argv[1] + ":" + sys.argv[2])
