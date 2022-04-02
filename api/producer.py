import requests


if __name__ == '__main__':

    # TEST OCR
    url = 'http://localhost:5000/ocr'
    files = {'image': open("/home/piki/PycharmProjects/24sata-hackathon-2022-repo2-polupismeni/OCR/bill.png", 'rb')}
    response = requests.post(url, files=files)
    try:
        data = response.json()
        print(data)
    except requests.exceptions.RequestException:
        print(response.text)


    # TEST RECOMMENDATION SYSTEM
    url = 'http://localhost:5000/recommend'
    item = {'item': "pasta"}
    response = requests.post(url, json=item, )
    try:
        data = response.json()
        print(data)
    except requests.exceptions.RequestException:
        print(response.text)
