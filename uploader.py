import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

# def create_folder(path):
#     """Создание папки. \n path: Путь к создаваемой папке."""
#     requests.put(f'{URL}?path={path}',headers = headers)


# create_folder('hello world')
# create_folder('hello world/api')

def upload_file(loadfile, savefile, replace=False):
    """Загрузка файла.
    savefile: Путь к файлу на Яндекс Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

upload_file(r'HappyBirthday.txt', '/HappyBirthday.txt', replace=True)



# uploader = yadisk.YaDisk(token = 'y0_AgAAAAAo3kLXAADLWwAAAADdX0lZc3Nj_GVfSsCWiweZYbcIZ7DteHE')
# # pprint(list(uploader.listdir("/")))
# print('Содержимое корневой папки:\n')
# for item in uploader.listdir('/'):
#     print(f"Название: {item['name']}")
#     print(f'Размер: {item["size"]} байт')
#     print(f"Тип файла: {item['type']}")
#     print(f"Тип документа: {item['media_type']}")
#     print(f"Дата создания: {item['created']}\n")
