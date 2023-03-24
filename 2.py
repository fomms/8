import requests
import os

TOKEN = ""


class YaUploader:
    def __init__(self, TOKEN: str):
        self.token = TOKEN

    def upload(self, file_path: str):
        """Метод загружает файлы из file_path на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Authorization': f'OAuth {TOKEN}'}
        for file in os.listdir(file_path):
            params = {"path": f'/netology/{file}', "overwrite": "True"}
            response = requests.get(url, headers=headers, params=params)
            requests.put(response.json()["href"], data=open(file_path + '\\' + file, "rb"), headers=headers)


if __name__ == '__main__':
    path_to_file = r'C:\Users\fomms\Desktop\request\files_to_Ydisk'
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)

path = r'C:\Users\fomms\Desktop\request\files_to_Ydisk'
print(os.listdir(path))