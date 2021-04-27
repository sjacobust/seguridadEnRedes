import hashlib, sympy, requests, json, time, multiprocessing


# url = "http://localhost:3002/mineBlock" If you have localhost as a peer setup
url = "http://34.70.94.162:8080/mineBlock"

def start_mining():
    i = 10303 # Last Prime number mined
    j = 0
    headers = {'Content-type': 'application/json'}
    while True:

        if sympy.isprime(i):
            hash_number = hashlib.sha256(bytes('{}'.format(i), encoding='utf8')).hexdigest()
            payload = {"data": {
            "id": "is699367",
            "prime": "{}".format(hash_number.upper())}
            }
            json_object = json.dumps(payload)
            r = requests.post(url, data=json_object, headers=headers)
            print(i, " : ", r.status_code, r.json())
            j += 1
            if j % 10000 == 0:
                print("Starting sleep.")
                # Halts for 5 seconds the program after 10,000
                # prime numbers have been found (a little breathing air for the server).
                time.sleep(5)
                print("Ended sleep, cointinuing.")
        i += 1


if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=start_mining, name="SartMining")
    p.start()

    # Wait 10 seconds for foo
    time.sleep(2400)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()

