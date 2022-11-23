import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == "TOO_LOW")

    def test_infers_breach_as_per_limits1(self):
        self.assertTrue(typewise_alert.infer_breach(200, 50, 100) == "TOO_HIGH")

    def test_infers_breach_as_per_limits2(self):
        self.assertTrue(typewise_alert.infer_breach(50, 50, 50) == "NORMAL")

#     def test_send_to_email_low(self):
#         self.assertTrue(
#             typewise_alert.send_to_email("TOO_LOW") == "To: a.b@c.com\nHi, the temperature is too low"
#         )

#     def test_send_to_email_high(self):
#         self.assertTrue(
#             typewise_alert.send_to_email("TOO_HIGH")
#             == "To: a.b@c.com\nHi, the temperature is too high"
#         )
    
    def test_check_and_alert(self):
        self.assertTrue(
            typewise_alert.check_and_alert("TO_EMAIL", "high_active_cooling", 200)
            == "To: a.b@c.com \n Hi, the temperature is too high"
        )


if __name__ == "__main__":
    unittest.main()
