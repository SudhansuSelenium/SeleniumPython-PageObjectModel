import json

settings = None


def load_setting():
    global settings
    with open("D:\\PythonProjects\\SeleniumPython-PageObjectModel\\resources\\settings.json", "r") as fp:

        settings = json.load(fp)


load_setting()
