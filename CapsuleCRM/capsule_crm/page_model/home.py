from utility.UI_operation import UIOperation
from utility.constant import Constant
import time

class HomePage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_HOME)

    def people_and_organization(self):
        self.ui_action.get_locator("button_people_id").click()
    
    def case(self):
        self.ui_action.get_locator("button_case_id").click()

    def account_option(self):
        time.sleep(10)
        self.ui_action.get_locator("button_account_name_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_account_setting_xpath").click()
