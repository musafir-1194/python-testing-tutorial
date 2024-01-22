import pytest
import math

import source.shape as shape

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shape.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle # it will auto do this but for complex this teardown method will be useful

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected 