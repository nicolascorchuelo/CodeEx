import yaml

__config = None

def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r', encoding='utf8') as stream:
            __config = yaml.safe_load(stream)

    return __config