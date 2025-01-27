import json
import subprocess

from airtest.cli.parser import cli_setup
from airtest.core.api import *

from Utilities.base import Base

with open('./data/testData.json') as jsonFile:
    testData = json.load(jsonFile)


class HomeScene(Base):
    def manage_permission_popups(self):
        gameName = self.get_config_value("game_name")
        try:
            self.step_info("#Manage Popups")
            if self.wait_for(self.get_imagePath("whileUsingThisApp"), time_out=7):
                self.tap_on(self.get_imagePath("whileUsingThisApp"))
            while self.wait_for(self.get_imagePath("allow_Button"), time_out=10):
                self.tap_on(self.get_imagePath("allow_Button"))
            self.step_pass(f"Successfully managed all Permission popups in '{gameName}' Application")
        except Exception as e:
            self.step_fail(f"Failed to manage Permission popup in '{gameName}' Application . Error: {str(e)}")

    def click_play_now_button(self):
        self.tap_on(self.get_imagePath("playNow_Button"))

    def login_as_a_validUser(self):
        userName = self.get_config_value("userName")
        password = self.get_config_value("password")
        try:
            self.tap_on(self.get_imagePath("userName_TextBox"))
            self.type_text(userName)
            sleep(2)
            self.tap_on(self.get_imagePath("password_TextBox"), times=2)
            self.type_text(password)
            sleep(1)
            self.tap_on(self.get_imagePath("login_Button"), times=2)
            sleep(5)
            # Validate home page appears
            if not self.is_exists(self.get_imagePath("WPT_icon")):
                self.return_to_game_application(self.get_config_value("appPackage"), self.get_config_value("appName"))
            while self.wait_for(self.get_imagePath("okay_Button"), 5):
                self.tap_on(self.get_imagePath("okay_Button"))
                sleep(3)
        except Exception as e:
            self.step_fail(
                f"Failed to login as valid user with Username:'{userName}' and Password:'{password}'. Error: {str(e)}")

    def login_as_a_invalidUser(self):
        userName = self.get_config_value("userName")
        invalid_password = self.get_config_value("invalid_password")
        try:
            self.tap_on(self.get_imagePath("userName_TextBox"))
            self.type_text(userName)
            sleep(2)
            self.tap_on(self.get_imagePath("password_TextBox"), times=2)
            self.type_text(invalid_password)
            sleep(1)
            self.tap_on(self.get_imagePath("login_Button"), times=2)
            sleep(5)
            # Validate home page appears
            if self.is_exists(self.get_imagePath("login_Error")):
                self.step_fail(f"Failed to Login as user: {userName} and password: {invalid_password}")
                self.tap_on(self.get_imagePath("close_Button"))
        except Exception as e:
            self.step_fail(
                f"Failed to login as valid user with Username:'{userName}' and Password:'{password}'. Error: {str(e)}")
    def validate_userName_and_playerId(self):
        userName = self.get_config_value("userName")
        try:
            self.step_info("Verify User Details")
            self.tap_on(self.get_imagePath("player_icon"), times=2)
            if self.is_exists(self.get_imagePath("player_name")):
                self.step_pass("Verification of Player name for user '" + userName + "' is successful!")
            else:
                self.step_fail("Failed to verify of Player name for user '" + self.get_config_value(
                    "userName") + "'. Please check the Player Name and UserName inputs!")
            if self.is_exists(self.get_imagePath("player_id")):
                self.step_pass("Verification of Player Id for user '" + userName + "' is successful!")
            else:
                self.step_fail(
                    "Failed to verify of Player name for user '" + userName + "'. Please check the Player Name and UserName inputs!")
        except Exception as e:
            self.step_fail(
                f"Failed to validate Username:'{userName}' or their respective player Id. Error: {str(e)}")
