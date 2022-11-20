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

    def test_check_and_alert(self):
        ct = CoolingType()
        self.assertTrue(
            typewise_alert.check_and_alert("TO_EMAIL", ct.high_active_cooling, 200)
            == "the temperature is too high"
        )


if __name__ == "__main__":
    unittest.main()
