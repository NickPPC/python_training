import requests
import hashlib

blue_seed = 'blue_seed'
red_seed = 'red_seed'
blue_url = 'http://blue:5000'
red_url = 'http://red:5000'

def check_content(seed, filename, content):
    if str(hashlib.sha224((seed + filename).encode()).hexdigest()) == content:
        return 1
    return 0

def check_round():
    blue = 0
    red = 0

    #Hello
    req = requests.get(blue_url + '/hello')
    if req.status_code == 200:
        blue += 1
    req = requests.get(red_url + '/hello')
    if req.status_code == 200:
        red += 1

    # tmpX.txt, 0 to 8
    for i in range(9):
        req = requests.get(blue_url + '/file', json={"file" : "tmp{}.txt".format(i)})
        if req.status_code == 200:
            content = req.json()['content']
            blue =+ check_content(blue_seed, 'tmp{}.txt'.format(i), content)
        req = requests.get(red_url, json={"file" : "tmp{}.txt".format(i)})
        if req.status_code == 200:
            content = req.json()['content']
            red =+ check_content(red_seed + '/file', 'tmp{}.txt'.format(i), content)

    # Secrets

    for i in range(5):
        req = requests.get(blue_url + '/secrets', json={"id" : i})
        if req.status_code == 200:
            content = req.json()['content']
            blue =+ check_content(blue_seed, 'secrets/secret{}'.format(i), content)
        req = requests.get(red_url + '/secrets', json={"id" : i})
        if req.status_code == 200:
            content = req.json()['content']
            red =+ check_content(red_seed, 'secrets/secret{}'.format(i), content)
    
    return (blue, red)

def secret5():
    secret_filename = 'secrets/secret5'
    red_content = red_seed + secret_filename
    with open('red_' + secret_filename, 'w') as f:
            f.write(str(hashlib.sha224(red_content.encode()).hexdigest()))
    blue_content = blue_seed + secret_filename
    with open('blue_' + secret_filename, 'w') as f:
            f.write(str(hashlib.sha224(blue_content.encode()).hexdigest()))

if __name__ == '__main__':
    blue_score = 0
    red_score = 0

    secret5()

    while True:
        (blue, red) = check_round()
        print("Round: Bleu +{}, Rouge +{}".format(blue, red))
        blue_score += blue
        red_score += red
        print('Score total: \nBleu {}\nRouge {}'.format(blue_score, red_score))