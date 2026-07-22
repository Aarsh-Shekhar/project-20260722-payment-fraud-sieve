import unittest

from payment_fraud_sieve.models import Record
from payment_fraud_sieve.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="payment-017", exposure=75795, signal=0.892, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
