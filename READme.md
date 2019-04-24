
# ROBOT FRAMEWORK TEST REGRESSION

# Quick Start Install Procedure
- navigate to the robotWrapper directory
- *python -m venv robotVenv*
- *robotVenv\Scripts\activate*
- python -m pip install -r requirements.txt
 - If this does not work, you can install each library one at a time:
  - *pip install <insert_library>*

# Running
- Ensure to always activate your virtual environment before running tests:
 - To activate: Navigate to robotWrapper directory, then enter *robotVenv\Scripts\activate*
 - To deactivate: Navigate to robotWrapper directory, then enter *robotVenv\Scripts\deactivate.bat*
- Runs with robot framework
 - To run this enter:  *robot tests*  (into your command prompt)
 - The above command runs whatever test suite you want to select, or all test suites if you select the highest level directory
- Added a python wrapper script that outputs all files into a table (html) in reverse chronological order
 - To run this enter:  *python htmlWrapper.py* (into your command prompt)
 - This script writes the test output data to a Logs directory in /testResults
 - All past tests in this directory are displayed in a table in reverse chronological order, with links to the robotframework reports and logs

# References
- robot --variable LOGGER_COMPORT:COM9 --variable IPI_COMPORT:COM4
- the command above lets you change what COMPORT you are writing to
- robot --pythonpath C:\\Users\\rechegaray\\Desktop\\robotWrapper\\tests\\ipi  v1.robot
- the command above lets you add a path to your pythonpath file
- http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide
- the link above is the robot framework user guide
- you can also type robot --help to display a list of several commands/parameters
