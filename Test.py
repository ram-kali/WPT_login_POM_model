# -*- encoding=utf8 -*-
__author__ = "Ram K"

import json
import subprocess
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging

from airtest.report.report import simple_report

from Scene.HomeScene import HomeScene
from TestScenario.WPT_Poker import WPT_Poker
from Utilities.base import Base

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
base = Base()



try:
    base.step_info("***Start TestCase 1***")
    if base.get_excutable("testcase1") == "True":
        base.beforeAll()
        testcase1 = WPT_Poker()
        testcase1.wpt_login_as_invalidUser()
    base.step_info("***Stop TestCase 1***")
    base.afterAll()
except Exception as e:
    base.step_fail("Failed to execute TestCase 1 - Login Flow as invalid user. Error: " + str(e))

try:
    base.step_info("***Start TestCase 2***")
    if base.get_excutable("testcase2") == "True":
        base.beforeAll()
        testcase2 = WPT_Poker()
        testcase2.wpt_login_as_validUser()
    base.step_info("***Stop TestCase 2***")
    base.afterAll()
except Exception as e:
    base.step_fail("Failed to execute TestCase 2 - Login Flow as valid user. Error: " + str(e))

simple_report(__file__, logpath=True, logfile='./log.txt', output='./TestResult/Report.html')
