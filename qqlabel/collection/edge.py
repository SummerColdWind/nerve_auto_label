import cv2
import numpy as np

from collections import namedtuple


MIN_LENGTH = 50
KERNEL = np.ones((3, 3), np.uint8)
Output = namedtuple('Output', 'shapes path height width')

class EdgeDetect:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path)[:384, :]
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.binary = None
        self.edges = []

    def detect(self):
        self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
        edges = cv2.Canny(self.gray, 50, 255)
        _, self.gray = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # self.gray = cv2.morphologyEx(self.gray, cv2.MORPH_CLOSE, KERNEL, iterations=1)
        contours, _ = cv2.findContours(self.gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            length = cv2.arcLength(contour, True)
            if length > MIN_LENGTH:
                self.edges.append(contour)

        filtered_image = np.zeros_like(self.image)
        cv2.drawContours(self.image, self.edges, -1, (0, 0, 255), 1)
        cv2.drawContours(filtered_image, self.edges, -1, (255, 255, 255), 1)
        self.binary = filtered_image

    def show(self, color=True):
        cv2.imshow('Show', self.image if color else (self.binary if self.binary else self.gray))
        cv2.waitKey(0)

    def shapes(self):
        if self.binary is not None:
            for edge in self.edges:
                yield [tuple(e[0]) for e in edge]
        else:
            raise RuntimeError('Please detect first!')

    def output(self):
        return Output(
            shapes=self.shapes(),
            path=self.path,
            height=self.image.shape[0],
            width=self.image.shape[1]
        )

    def save(self, path):
        cv2.imwrite(path if path else './result/result.png', self.image)



