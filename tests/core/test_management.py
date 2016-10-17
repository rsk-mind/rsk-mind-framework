from rsk_mind.core.management import *


class TestManagementError:

    def test_execute_from_command_line(self):
        execute_from_command_line(["rskmind-admin.py", "not_valid", "test"])

    def test_execute_from_command_line_startapp(self):
        execute_from_command_line(["rskmind-admin.py", "startapp", "test"])
