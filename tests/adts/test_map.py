#
# Author: Rohtash Lakra
#
from adts.map.map import Map
from tests._abstract import AbstractTest


class MapTest(AbstractTest):
    """Unit-tests for Map"""

    def test_map(self):
        print("test_map")
        map = Map()
        print(f"map={map}, size={len(map)}")
        self.assertIsNotNone(map)
        self.assertEqual(0, len(map))
        print()

    def test_map_parameterized(self):
        print("test_map_parameterized")
        map = Map({"message": "Hello World"})
        print(f"map={map}, size={len(map)}")
        self.assertIsNotNone(map)
        self.assertEqual(1, len(map))
        print()

    def test_map_update(self):
        print("test_map_update")
        map = Map({"id": "0001",
                   "type": "donut",
                   "name": "Cake",
                   "ppu": 0.55})
        print(f"map={map}, size={len(map)}")
        self.assertIsNotNone(map)
        self.assertEqual(4, len(map))
        print()
        map.update({"data":{
            "id": "1001",
            "type": "Regular"
        }})
        print(f"map={map}, size={len(map)}")
        self.assertIsNotNone(map)
        self.assertEqual(5, len(map))
        print()


# Starting point
if __name__ == 'main':
    MapTest().start()
