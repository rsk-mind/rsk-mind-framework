#!/usr/bin/env python
import sys
import setting

from rsk_mind.core import commands

if __name__ == "__main__":
    commands.execute_from_command_line(sys.argv, setting)