# -*- encoding=utf8 -*-
__author__ = "Ram K"

import json
import subprocess
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging

from Scene.HomeScene import HomeScene
from Utilities.base import Base

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
base = Base()
home = HomeScene()


class WPT_Poker:

    def wpt_login_as_validUser(self):
        # manage permission popups
        home.manage_permission_popups()
        # Login flow
        home.step_info("#Login Flow with valid username and password")
        home.click_play_now_button()
        home.login_as_a_validUser()
        home.validate_userName_and_playerId()

    def wpt_login_as_invalidUser(self):
        # manage permission popups
        home.manage_permission_popups()
        # Login flow
        home.step_info("#Login Flow with valid username and password")
        home.click_play_now_button()
        home.login_as_a_invalidUser()
