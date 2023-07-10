import json

from qqlabel.utils import get_base64

class Convert:
    def __init__(self, data):
        self.data = data
        self.dict = {}
        self.prefix = 'nerve_'

    def create(self):
        self.dict['version'] = '5.2.1'
        self.dict['flags'] = {}
        self.dict['shapes'] = self.shapes()
        self.dict['imagePath'] = self.data.path
        self.dict['imageData'] = get_base64(self.data.path)
        self.dict['imageHeight'] = self.data.height
        self.dict['imageWidth'] = self.data.width


    def save(self, path=None):
        with open(path if path else f'./results/result.json', 'w') as file:
            json.dump(self.dict, file, indent=2)

    def shapes(self):
        raw_shapes = list(self.data.shapes)
        shapes = []
        for i in range(len(raw_shapes)):
            shapes.append({
                "label": f"{self.prefix}{i}",
                "points": [list(map(float, e)) for e in list(raw_shapes)[i]],
                "group_id": None,
                "description": "",
                "shape_type": "polygon",
                "flags": {}
            })
        return shapes











