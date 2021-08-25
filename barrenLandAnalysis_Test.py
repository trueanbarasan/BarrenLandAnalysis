import unittest
from barrenLandAnalysis import Farm


class BarrenLandAnalysis_Test(unittest.TestCase):
    """
    Unitesting of Barren Land Analysis module and find_area_of_fertile_lands function

    Args:
        param1: (int) Height of the farm
        param2: (int) Width of the farm
        param3: (set) The coordinates of barren land. String seprated by space.
    Returns:
        (string) sorted areas of fertile lands or error message
    """

    def test_case_study_input_1(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(
            600, 400, {"0 292 399 307"}
        )
        self.assertEqual(land, "116800 116800")

    def test_case_study_input_2(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(
            600,
            400,
            {"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"},
        )
        self.assertEqual(land, "22816 192608")

    def test_simple_valid_case(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(6, 4, {"0 2 2 3"})
        self.assertEqual(land, "18")

    def test_fully_barren(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(4, 3, {"0 0 2 3"})
        self.assertEqual(land, "0")

    def test_one_pointer_barren(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(4, 5, {"0 0 0 0"})
        self.assertEqual(land, "19")

    def test_smaller_area(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(5, 6, {"2 0 4 4"})
        self.assertEqual(land, "5 10")

    def test_width_only(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(4, 5, {"0 0 0 3"})
        self.assertEqual(land, "16")

    def test_height_only(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(4, 5, {"4 0 4 3"})
        self.assertEqual(land, "16")

    def test_no_barren_land(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(5, 6, {})
        self.assertEqual(land, "30")

    # Invalid test cases
    def test_barren_out_of_range(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(5, 6, {"4 4 6 5"})
        self.assertEqual(land, "Barren coordinates are outside of farm")

    def test_negative_barren(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(5, 6, {"-1 0 2 2"})
        self.assertEqual(land, "Barren coordinates are outside of farm")

    def test_invalid_height_width(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(-1, 2, {"0 0 2 2"})
        self.assertEqual(land, "Invalid height or width")

    # Performace testing case for single fertile land optimization
    def test_single_fertile_land(self):
        barrenLandAnalysis = Farm()
        land = barrenLandAnalysis.find_area_of_fertile_lands(
            6000, 4000, {"0 2930 3998 3070"}
        )
        self.assertEqual(land, "23436141")
