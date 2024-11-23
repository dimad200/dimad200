import requests

def zapros_slowa():
    a = 'http://free-generator.ru/generator.php?action=word&type=1'
    # response = requests.get(a)
    output = requests.get(a).json()
    # output = response.json()
    b = output["word"]
    return b["word"]


for i in range(10):
    a=zapros_slowa()
    print(a)


# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')