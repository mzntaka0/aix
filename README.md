# aix
Help tool for creating API of micro-serviced AI


## Install
```
git clone https://github.com/AI-dea/aix.git
cd aix
python setup.py install
```

## Usage
```
import aix

ocr = aix.get('ocr')
print(ocr)
# {'Module': {'name': 'ocr', 'interface': {'input': 'image', 'output': 'json'}, 'repo': 'gocr'}}
result = ocr(image)
```
