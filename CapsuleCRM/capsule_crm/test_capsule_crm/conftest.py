import pytest
from environment_setup.browser_instance import BrowserInstance
from utility.send_mail import SendMail
from utility.constant import Constant
from utility.custom_logger import CustomLogger
from exception.capsulecrm_exception import CapsulecrmException
import socket

global REMOTE_SERVER 
REMOTE_SERVER= "one.one.one.one"

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    log=CustomLogger.log_utility()
    constant=Constant()
    file_name=[]
    file_name = report.nodeid.split("::")
    if(report.when == 'call'):
        log.info('Name : '+file_name[2]+' when : '+report.when + '  status : ' +report.outcome)

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
    
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot=constant.PATH_SCREENSHOT+file_name[2]+".png"
            _capture_screenshot(screenshot)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False 

@pytest.yield_fixture(scope="class")
def initialize_driver(request,browser):
    global driver
    driver=BrowserInstance(browser).get_browser_instance()
    if (is_connected(REMOTE_SERVER)):
        constant=Constant()
        # Set class attribute and assign the variable
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        sent_mails=SendMail()
        sent_mails.sent_email_report(constant.PATH_EMAIL,constant.SHEET_MAIL_CREDENTIAL,constant.PATH_REPORT)
        driver.quit() 
    else:
        raise CapsulecrmException("No Internet Connection","NO_NETWORK") 

# Create parsers to get value from command prompt
def pytest_addoption(parser):
    parser.addoption("--browser")

#Return the argument value
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")    




