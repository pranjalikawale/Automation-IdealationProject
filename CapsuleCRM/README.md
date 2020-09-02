Project Title
    CapsuleCrm Automation

Description
    The project is to automate CRM application

Prerequisites
    Visual Studio Code
    Browser[Chrome, Firfox or Internet]
    Internet Connection

Technology Used
    Python
    
Frameworks
    Selenium
    Data Driven

Design Pattern
    Page Object Model

Packages
    jProperties- A jProperties is a Java Property file parser and writer for Python.
    socket- Socket is used for to check network connection
    pyhtml report- To generate Test Reports 
    openpyxl- To access data from xls file
    pytest- To define test cases, assertion
    selenium.webdriver- Binding for selenium webdriver API
    chromedriver- Driver for Google Chrome
    geckodriver- Driver for Firefox
    Iedriver- Driver for Internet Explore
    smtplib- Used to send mail to any Internet machine with an SMTP
    logging-Logging Test steps to log file

Test scenario covered
    Pre-Conditions(Manual Step)
    1. Go to https://capsulecrm.com
    2. Create a free account
    Ex:http://.......capsulecrm.com

    TestCase 1:
    1) go to this url - http://.......capsulecrm.com/login?
        a) Login with correct credentials
    2) click on person icon and add a person
    3) click on cases icon
    4) click on Add Case button
    5) Create a new case with the added person
    6) Verify the correct case got created for the same person
    7) Verify the case status : Open
    8) Close the browser

    Testcase 2:
    1) go to this url - http://.......capsulecrm.com/login?
        a) Login with correct credentials
    2) Click on account name at left top corner
    3) goto account settings
    4) verify account settings page header
    5) click on each link available at left panel:
        Account Settings
        1) Account
        2) Invoices
        3) Export
        4) Appearance
        5) Mail drop box
        6) Users
        7) Opportunities
        8) Tracks
        9) Task Categories
        10) Custom Fields
        11) Tags
        12) Integrations
        13) Trash
    6) After clicking on each link, verify the page header
    7) click on Appearance and upload a logo image
    8) click on Users: Add new user and Verify the same user
    9) click on opportunities:Add new milestone and verify the same
    10)click on tracks : add new track and verify the same
    11)click on task categories:add new category and verify the same
    12)click on tags:add new milestone and verify the same
    13)Click on integration and verify total number of configure buttons
    14)close the browser

Author
    Pranjali Kawale

