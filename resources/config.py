import json

settings = None


def load_setting():
    global settings
    with open("C:\\Users\\sudha_000\\PycharmProjects\\testng\\resources\\settings.json", "r") as fp:

        settings = json.load(fp)


load_setting()
