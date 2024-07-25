import yaml

def yaml_load(dir): 
    result = yaml.load(open(dir, 'r'), Loader=yaml.FullLoader)
    return result