import unittest

import HTMLTestReport

suite = unittest.TestLoader().discover("./", pattern="test_*")
runner = HTMLTestReport.HTMLTestReport(
    description="Test Report",
    title="Test Report",
    file_path="../report/report.html")
runner.run(suite)
