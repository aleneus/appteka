import sys
import os
import unittest

sys.path.insert(0, os.path.abspath("."))
from appteka.sqlite import testing as dbt


class TestSqliteSchemaTesting(unittest.TestCase):
    def test_smoke(self):
        terster = dbt.SchemaTester(self)
        terster.dot_read("test/test_sqlite/data/script.sql")
        terster.assert_select("SELECT * FROM T", [(1, 2)])
        terster.close()
