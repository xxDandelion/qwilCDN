import unittest
from core.setup_mapping import Cluster
from core.logs import ComponentLog
cluster = None


class TestResult(object):

    def startTestRun(self):
        """
        Called once before any tests are executed.

        :return:
        """
        global cluster
        cluster = Cluster()
        ComponentLog()

    setattr(unittest.TestResult, 'startTestRun', startTestRun)

    def stopTestRun(self):
        """
        Called once after all tests are executed.

        :return:
        """
        global cluster
        cluster.clear_cluster()

    setattr(unittest.TestResult, 'stopTestRun', stopTestRun)

    def load_tests(self):
        tests = unittest.defaultTestLoader.discover(".")
        suite = unittest.TestSuite()
        suite.addTests(tests)
        unittest.TextTestRunner(verbosity=2).run(suite)
