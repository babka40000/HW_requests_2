import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        base_path = "https://cloud-api.yandex.net/"
        upload_command_path = "v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}", "Content-Type": "application/json"}

        params = {"path": "file.txt", "overwrite": "true"}
        response_json = requests.get(base_path+upload_command_path, headers=headers, params=params).json()
        href = response_json["href"]

        response = requests.put(href, data=open("temp.txt", "rb"))
        if response.status_code == 201:
            print("Файл загружен")
        else:
            print(f"Файл не загружен. Статус возврата - {str(response.status_code)}")


if __name__ == '__main__':
    path_to_local_file = "temp.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_local_file)

