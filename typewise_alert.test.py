
import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == "TOO_LOW")

    def test_infers_breach_as_per_limits1(self):
        self.assertTrue(typewise_alert.infer_breach(200, 50, 100) == "TOO_HIGH")

    def test_infers_breach_as_per_limits2(self):
        self.assertTrue(typewise_alert.infer_breach(50, 50, 50) == "NORMAL")

    def test_send_to_email_low(self):
        self.assertFalse(
            typewise_alert.send_to_email("TOO_LOW") == ""
        )

    def test_send_to_email_high(self):
        self.assertFalse(
            typewise_alert.send_to_email("TOO_HIGH")
            == ""
        )
    
    def test_check_and_alert_email(self):
        self.assertFalse(
            typewise_alert.check_and_alert("TO_EMAIL", "high_active_cooling", 200)
            == ""
        )

    def test_check_and_alert_controller(self):
        self.assertTrue(
            typewise_alert.check_and_alert("TO_CONTROLLER", "med_active_cooling", 200)
            == "0xfeed, med_active_cooling"
        )


if __name__ == "__main__":
    unittest.main()
