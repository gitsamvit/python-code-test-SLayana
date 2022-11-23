import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(
            typewise_alert.infer_breach(20, 50, 100) == "the temperature is too low"
        )

    def test_infers_breach_as_per_limits1(self):
        self.assertTrue(
            typewise_alert.infer_breach(200, 50, 100) == "the temperature is too high"
        )

    def test_infers_breach_as_per_limits2(self):
        self.assertTrue(
            typewise_alert.infer_breach(50, 50, 50) == "the temperature is normal"
        )




if __name__ == "__main__":
    unittest.main()
