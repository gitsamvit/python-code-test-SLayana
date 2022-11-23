import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertFalse(
            typewise_alert.check_and_alert("TO_EMAIL", "passive_cooling", 200) == "the temperature is too low"
        )

if __name__ == "__main__":
    unittest.main()
