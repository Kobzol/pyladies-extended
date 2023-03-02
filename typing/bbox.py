import dataclasses
from typing import Union


@dataclasses.dataclass
class BBox:
    left: float
    top: float
    width: float
    height: float

    def normalize(self, width: float, height: float) -> "NormalizedBBox":
        raise NotImplementedError


@dataclasses.dataclass
class NormalizedBBox(BBox):
    def normalize(self, width: float, height: float) -> "NormalizedBBox":
        return self

    @staticmethod
    def from_top_left_width_height(x: float, y: float, width: float,
                                   height: float) -> "NormalizedBBox":
        return NormalizedBBox(
            left=x,
            top=y,
            width=width,
            height=height
        )

    @staticmethod
    def from_top_left_bottom_right(x: float, y: float, right: float,
                                   bottom: float) -> "NormalizedBBox":
        return NormalizedBBox(
            left=x,
            top=y,
            width=width,
            height=height
        )

    def __post_init__(self):
        assert 0.0 <= self.left <= 1.0
        assert 0.0 <= self.top <= 1.0
        assert 0.0 <= self.width <= 1.0
        assert 0.0 <= self.height <= 1.0

    def denormalize(self, width: float, height: float) -> "DenormalizedBBox":
        return DenormalizedBBox(
            left=self.left * width,
            top=self.top * height,
            width=self.width * width,
            height=self.height * height,
        )


@dataclasses.dataclass
class DenormalizedBBox(BBox):
    def normalize(self, width: float, height: float) -> NormalizedBBox:
        return NormalizedBBox(
            left=self.left / width,
            top=self.top / height,
            width=self.width / width,
            height=self.height / height,
        )


BBoxEnum = Union[NormalizedBBox, DenormalizedBBox]


def normalize(bbox: BBoxEnum, width: float, height: float) -> NormalizedBBox:
    if isinstance(bbox, NormalizedBBox):
        return bbox
    elif isinstance(bbox, DenormalizedBBox):
        return bbox.normalize(width, height)
    else:
        assert False


bbox = NormalizedBBox.from_top_left_width_height(0.1, 0.2, 0.3, 0.3)
b = bbox.normalize(128, 128)
