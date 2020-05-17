import json

getProperty = None
desired_capabilities = None

def load_setting():
    global getProperty
    global desired_capabilities
    with open("D:\\PythonProjects\\SeleniumPython-PageObjectModel\\resources\\testData.json", "r") as fp:
        getProperty = json.load(fp)

    with open("D:\\PythonProjects\\SeleniumPython-PageObjectModel\\resources\\remoteDriverPlatform.json", "r") as fp2:
        desired_capabilities= json.load(fp2)


load_setting()
