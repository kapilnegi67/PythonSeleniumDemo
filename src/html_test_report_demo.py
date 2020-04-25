import unittest
from my_test_classes import A
from my_test_classes import C
import os
import HtmlTestRunner

current_directory = os.getcwd()


class HTMLReportSuite(unittest.TestCase):

    def test_html_report(self):

        # Create a TestSuite
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(A),
            unittest.defaultTestLoader.loadTestsFromTestCase(C)
        ])
#         consolidated_test.addTest(A('test_A1'))
#         consolidated_test.addTest(C('test_C3'))

        output_file = open(current_directory + "\MyHTMLReport.html", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
