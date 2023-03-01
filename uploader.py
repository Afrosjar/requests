import os
import yadisk

p = os.path.abspath('HappyBirthday.txt')
name = os.path.basename(r'HappyBirthday.txt')

def make_upload(path, new_name):
    uploader = yadisk.YaDisk(token = '**********************************')
    if uploader.is_file(new_name) :
        uploader.remove(new_name, permanently = True)
        print("Предыдущий файл с таким названием удален, далее записывается новый файл с таким же названием")
        uploader.upload(path,new_name)
        print('Файл записан')
    else:
        uploader.upload(path,new_name)
        print('Файл записан')


if __name__ == '__main__':
    make_upload(p, name)




# uploader = yadisk.YaDisk(token = 'y0_AgAAAAAo3kLXAADLWwAAAADdX0lZc3Nj_GVfSsCWiweZYbcIZ7DteHE')
# # pprint(list(uploader.listdir("/")))
# print('Содержимое корневой папки:\n')
# for item in uploader.listdir('/'):
#     print(f"Название: {item['name']}")
#     print(f'Размер: {item["size"]} байт')
#     print(f"Тип файла: {item['type']}")
#     print(f"Тип документа: {item['media_type']}")
#     print(f"Дата создания: {item['created']}\n")