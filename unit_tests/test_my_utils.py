import sys
import unittest

sys.path.append('src/')  # noqa

import numpy as np
import my_utils
import random


class TestCalc(unittest.TestCase):
    # Define mean tests for empty arrays, negative
    # numbers, and positive numbers
    def test_mean_zero(self):
        self.assertEqual(my_utils.mean_func([]), 0)

    def test_mean_neg(self):
        rand_data = [random.randint(-150, -5) for _ in range(15)]
        self.assertAlmostEqual(my_utils.mean_func(rand_data),
                               np.mean(rand_data))

    def test_mean_pos(self):
        rand_data = [random.randint(5, 150) for _ in range(15)]
        self.assertAlmostEqual(my_utils.mean_func(rand_data),
                               np.mean(rand_data))

    # Define median tests for empty arrays, negative
    # numbers, and positive numbers
    def test_med_func(self):
        self.assertEqual(my_utils.med_func([]), 0)

    def test_med_neg(self):
        rand_data = [random.randint(-150, -5) for _ in range(15)]
        self.assertAlmostEqual(my_utils.med_func(rand_data),
                               np.median(rand_data))

    def test_med_pos(self):
        rand_data = [random.randint(5, 150) for _ in range(15)]
        self.assertAlmostEqual(my_utils.med_func(rand_data),
                               np.median(rand_data))

    # Define standard deviation tests for empty arrays, negative
    # numbers, and positive numbers
    def test_sd_func(self):
        self.assertEqual(my_utils.sd_func([]), 0)

    def test_sd_neg(self):
        rand_data = [random.randint(-150, -5) for _ in range(15)]
        self.assertAlmostEqual(my_utils.sd_func(rand_data), np.std(rand_data))

    def test_sd_pos(self):
        rand_data = [random.randint(5, 150) for _ in range(15)]
        self.assertAlmostEqual(my_utils.sd_func(rand_data), np.std(rand_data))


if __name__ == '__main__':
    unittest.main()
