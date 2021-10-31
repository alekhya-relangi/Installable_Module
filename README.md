## About

  Installable_Module to read YAML and CFG files into flat dictionary.
  
## Features

* Reads your YAML and CFG files from your local
* Generates dictionary and flat dictionary as output
* Generates a Json file in the same folder 
* Wheel file is created to make it installable in virtual enviroments. 

## Libraries used:

YAML:
  YAML is a data serialization format designed for human readability and interaction with scripting languages. PyYAML is a YAML parser and emitter for Python.
  
JSON:
  JSON (JavaScript Object Notation) <http://json.org> is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data interchange format.
  
COLLECTIONS:
  This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.
  
CONFIGPARSER:
  Configuration file parser. A configuration file consists of sections, lead by a "[section]" header,
and followed by "name: value" entries, with continuations and such in the style of RFC 822.


### Specify your YML file path here 
``` python
with open("sample.yml",'r') as stream: 
```

### Generating a JSON file
``` python
f= open("sample.json","w")
json.dump(parsed_yaml,f)
f.close()
```
### Specify your CFG file path here
 ``` python
cfg = configparser.ConfigParser()
cfg.read('sample.cfg')
c=cfg._sections
```


