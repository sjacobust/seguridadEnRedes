import hashlib, sympy, requests, json, time


url = "http://localhost:3002/mineBlock" #url = "http://34.70.94.162:8080/mineBlock" If you have localhost as a peer setup

def start_mining():
    i = 1063039 # Last Prime number mined
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
                time.sleep(5) # Halts for 5 seconds the program after 10,000 prime numbers have been found (a little breathing air por the server).
                print("Ended sleep, cointinuing.")
        i += 1

start_mining()


