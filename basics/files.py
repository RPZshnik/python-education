import requests


def read_in_chunks(path):
    with open(path, "r") as file:
        for line in file.readlines():
            yield line


def read_all_text(path):
    with open(path, "r") as file:
        return file.read()


def print_file(path):
    for i, line in enumerate(read_in_chunks(path)):
        print(f"{i + 1}. {line}")


def download_png(url):
    response = requests.get(url)
    with open("test_img.png", "wb") as file:
        file.write(response.content)


def main():
    file_path = "text.txt"
    print_file(file_path)
    image_url = "https://www.imgonline.com.ua/examples/bee-on-daisy.jpg"
    download_png(image_url)


if __name__ == "__main__":
    main()
