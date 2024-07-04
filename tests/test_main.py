import unittest
from unittest.mock import patch
import os
import sys

# Calculate the directory path relative to this script
current_dir = os.path.dirname(__file__)
project_dir = os.path.join(current_dir, '..')
sys.path.append(os.path.abspath(project_dir))
print("Current sys.path:", sys.path)

import main  # Import main after adjusting sys.path

class TestSaveResults(unittest.TestCase):

    @patch('main.save_results')
    def test_save_results_called(self, mock_save_results):
        # Test that save_results is called with expected arguments
        expected_args = ('data', 'file.txt')
        main.some_function()
        mock_save_results.assert_called_once_with(*expected_args)

    @patch('main.save_results', side_effect=Exception('Test exception'))
    def test_save_results_exception(self, mock_save_results):
        # Test exception handling when save_results raises an exception
        with self.assertRaises(Exception):
            main.some_function()

    def test_save_results_import(self):
        # Test that save_results can be successfully imported
        class TestCalculateDoses(unittest.TestCase):
        
            def test_total_bolus_zero_doses(self):
                carb_dose = 0
                correction_dose = 0
                total_bolus = main.total_bolus(carb_dose, correction_dose)
                self.assertEqual(total_bolus, 0)
        
            def test_total_bolus_positive_doses(self):
                carb_dose = 2.5
                correction_dose = 1.0
                total_bolus = main.total_bolus(carb_dose, correction_dose)
                self.assertEqual(total_bolus, 3.5)
        
            def test_total_bolus_negative_correction_dose(self):
                carb_dose = 3.0
                correction_dose = -1.5
                total_bolus = main.total_bolus(carb_dose, correction_dose)
                self.assertEqual(total_bolus, 1.5)
        
            def test_total_bolus_large_doses(self):
                carb_dose = 100.0
                correction_dose = 50.0
                total_bolus = main.total_bolus(carb_dose, correction_dose)
                self.assertEqual(total_bolus, 150.0)
        
            def test_total_bolus_float_precision(self):
                carb_dose = 2.12345
                correction_dose = 1.98765
                total_bolus = main.total_bolus(carb_dose, correction_dose)
                self.assertAlmostEqual(total_bolus, 4.1111, places=4)
                self.assertTrue(hasattr(main, 'save_results'))