from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1] 

from utils import yaml_load


config_dict = {
    "tiny-llama": "./config/tiny_llama.yaml"
}

def config_distribution(name:str="tiny-llama"): 
    try: 
        return yaml_load(dir=config_dict[name])

    except ValueError: 
        raise ValueError(f"{name} is not supported, please try another model!")