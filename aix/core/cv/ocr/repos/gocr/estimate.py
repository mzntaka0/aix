# -*- coding: utf-8 -*-
"""
"""
import io
import json
import pathlib

from dotenv import load_dotenv
from google.cloud import vision
from google.cloud.vision import types

load_dotenv()


class Estimate:

    def __init__(self):
        pass

    def __call__(self, img_path):
        if not isinstance(img_path, pathlib.Path):
            img_path = pathlib.Path(img_path)
        client = vision.ImageAnnotatorClient()
        image = self.load_image(img_path)
        response = client.text_detection(image)
        return response

    def load_image(self, img_path):
        with io.open(str(img_path.resolve()), 'rb') as f:
            content = f.read()
        image = types.Image(content=content)
        return image

    # TODO: refactor to make this method be more smart.
    @staticmethod
    def parse(response):
        labels = response.text_annotations

        response = dict()
        response['responses'] = list()
        response['responses'].append(dict())
        response['responses'][0]['locale'] = 'ja'
        response['responses'][0]['textAnnotations'] = list()

        for label in labels:
            content_dict = dict()
            content_dict['description'] = label.description
            content_dict['boundingPoly'] = dict()
            content_dict['boundingPoly']['vertices'] = list()
            for coord in label.bounding_poly.vertices:
                content_dict['boundingPoly']['vertices'].append({'x': coord.x, 'y': coord.y})

            response['responses'][0]['textAnnotations'].append(content_dict)
        return response

    @staticmethod
    def save(img_path, content):
        image_name = img_path.stem
        with open(image_name + '.json', 'w') as f:
            json.dump(content, f)
