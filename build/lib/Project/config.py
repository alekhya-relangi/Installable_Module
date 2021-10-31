#Libraries to import
import yaml
import configparser
import collections
import json

#converting dictionary to flat dictionary

def flatten(dictionary, parent_key=False, separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = str(parent_key) + separator + key if parent_key else key
        if isinstance(value, collections.abc.MutableMapping):
            items.extend(flatten(value, new_key, separator).items())
        elif isinstance(value, list):
            for k, v in enumerate(value):
                items.extend(flatten({str(k): v}, new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)

#Reading Yaml file to generate dictionary

#Specify the path to the Yaml file

with open("sample.yml",'r') as stream: 
    try: 
        parsed_yaml=yaml.safe_load(stream)
        
    except yaml.YAMLError as exc:
        print(exc)
        
#Generating a Json file 

f= open("sample.json","w")
json.dump(parsed_yaml,f)
f.close()

#Print flat dictionary from yaml file 

print(flatten(parsed_yaml))

#Reading cfg file to generate a dictionary

cfg = configparser.ConfigParser()
cfg.read('sample.cfg')
c=cfg._sections

#Print flat dictionary from cfg file

print(flatten(c))


