import json
import logging
import json
import shutil
import subprocess

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from colorama import Fore, Style


def empty_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Remove files or symbolic links
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove directories
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")


folder_path = "./TestResult"
empty_folder(folder_path)
# Configure logging
logging.basicConfig(level=logging.INFO, filename="./TestResult/TestResult.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

with open('./data/testData.json') as jsonFile:
    testData = json.load(jsonFile)


class Base:
    def __int__(self):
        self.testData = testData

    def get_config_value(self, key):
        return testData['config'].get(key, f"'{key}' not found in config")

    def get_imagePath(self, key):
        return testData['imagePath'].get(key, f"'{key}' not found in imagePath")

    def get_excutable(self, key):
        return testData['executables'].get(key, f"'{key}' not found in imagePath")

    def step_pass(self, statement):
        print(f"{Fore.GREEN}Step Pass: {str(statement)}{Style.RESET_ALL}")
        logging.info(f"Step Pass: {str(statement)}")

    def step_fail(self, statement):
        print(f"{Fore.RED}Step Fail: {str(statement)}{Style.RESET_ALL}")
        logging.error(f"Step Fail: {str(statement)}")

    def step_info(self, statement):
        print(f"{Fore.BLUE}Step Info: {str(statement)}{Style.RESET_ALL}")
        logging.info(f"#Step Info: {str(statement)}")

    def install_game_application(self, apkPath):
        try:
            install(apkPath)
            self.step_pass(f"Install Application from path '{apkPath}'")
        except Exception as e:
            self.step_fail(F"Failed to install Application '{apkPath}' . Error: {str(e)}")

    def start_new_game_application(self, appPackage, appName):
        try:
            clear_app(appPackage)
            start_app(appPackage)
            self.step_pass(f"Start '{appName}' Game Application")
        except Exception as e:
            self.step_fail(
                f"Failed to start Application '{appName}' as new Application. Error" + str(e))

    def stop_application(self, appPackage, appName):
        try:
            stop_app(appPackage)
            self.step_pass(f"Stop '{appName}' Game Application")
        except Exception as e:
            self.step_fail(
                f"Failed to Stop Application '{appName}' as new Application. Error" + str(e))

    def return_to_game_application(self, appPackage, appName):
        try:
            start_app(appPackage)
            self.step_pass(f"Return to '{appName}' Game Application")
        except Exception as e:
            self.step_fail(
                f"Failed to return to  '{appName}' game Application. Error" + str(e))

    def find_image_Element(self, imagePath):
        return Template(imagePath)

    def tap_on(self, imagePath, times=1, duration=0.1):
        try:
            element = touch(self.find_image_Element(imagePath), times=times, duration=duration)
            if element is not None:
                self.step_pass(f"Tap On: '{imagePath.split('/')[-1].split('.')[0]}'")
            return element
        except Exception as e:
            self.step_fail(f"Failed to tap on '{imagePath.split('/')[-1].split('.')[0]}' . Error: {str(e)}")

    def wait_for(self, imagePath, time_out):
        try:
            return wait(self.find_image_Element(imagePath), timeout=time_out)
        except Exception as e:
            self.step_info(f"Wait- '{imagePath.split('/')[-1].split('.')[0]}' is not displayed. Wait Time: {time_out}.")

    def is_exists(self, imagePath):
        try:
            return exists(self.find_image_Element(imagePath))
        except:
            self.step_info(f"Exists- '{imagePath.split('/')[-1].split('.')[0]}' is not found.")

    def type_text(self, inputText):
        try:
            subprocess.call(f"adb shell input keyboard text '{inputText}'", shell=True)
            self.step_pass(f"Type: Text '{inputText}'")
        except Exception as e:
            self.step_fail(f"Failed to type text '{inputText}' . Error: {str(e)}")

    def beforeAll(self):
        auto_setup(__file__,  logdir="./TestResult", devices=[self.get_config_value("device_URL"), ])
        apkPath = self.get_config_value("apkPath")
        # self.install_game_application(apkPath) // Turn On When app needed to be installed
        appPackage = self.get_config_value("appPackage")
        appName = self.get_config_value("game_name")
        self.start_new_game_application(appPackage, appName)

    def afterAll(self):
        appPackage = self.get_config_value("appPackage")
        appName = self.get_config_value("game_name")
        self.stop_application(appPackage, appName)

