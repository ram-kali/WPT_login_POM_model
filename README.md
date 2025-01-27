**README**

**Test Automation – Login Flow (Approach 2)**

**Overview**

This repository contains the implementation of the login flow automation for a mobile poker application using a robust framework based on the Page Object Model (POM) and Test-Driven Development (TDD). This approach ensures maintainable, reusable, and scalable automation scripts.

**Folder Structure**

Test.py: Main script for executing test cases.

Scene/: Contains methods for UI interactions specific to individual game scenes (e.g., Login Page).

TestScenario/: Includes test case scripts for various scenarios, such as valid and invalid login.

utilities/: Contains a base class with generic methods for reusable actions and log generation.

data/: Includes the testdata.json file for managing test configurations and input data.

ReferenceImages/: Holds images for UI element recognition.

TestResults/: Stores logs and test result reports.

**Requirements**

**Tools:**

Python 3.8.10 (or higher)

PyCharm Community Edition (or any Python IDE)

**Setup:**

APK file of the mobile poker application (make sure to paste the apk in apk folder) .

**Setup Instructions**

1. Clone or download this repository:

   git clone https://github.com/ram-kali/WPT_login_POM_model.git

2.Ensure the following files and folders are present:

  Test.py
  
  Scene/
  
  TestScenario/
  
  utilities/
  
  data/testdata.json
  
  ReferenceImages/
  
  TestResults/

3.Open the project in PyCharm (or any preferred Python IDE).

4.Framework Configuration

Open data/testdata.json and update the following fields:

a.Input Data: Customize username, password, or other fields as required.

b.Executables: Define which test cases should run.

c.Image Paths: Set paths for reference images.

d.Config Fields: Update execution-related settings.

**Execution Steps**

1. Open Test.py in the Python IDE.

(Optional) Uncomment the install_game_application line in the script if APK installation is required. The APK file is included for automated installation.

2. Run the script:

3. Right-click on Test.py and select "Run."

4. Monitor the logs in the IDE's console for real-time execution updates.

**Post-execution, review the following:**

Logs in TestResults/TestResults.log

HTML report in TestResults/Report.html

**Test Scenarios**

Valid Login: Tests successful login using correct credentials.

Invalid Login: Tests error handling for incorrect credentials.

**Deliverables**

Automation scripts for login flow.

Logs and HTML reports detailing execution results.

**Notes**

Ensure that Python 3.8.10 (or higher) is installed and properly configured.

Default APK installation is commented out for convenience; un-comment as needed and add the apk in folder.

Customize testdata.json to match the specific requirements of your test scenarios.
