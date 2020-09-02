from utility.UI_operation import UIOperation
from utility.constant import Constant
import time

class LogoutPage():

    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_lOGIN)

    def logout(self):
        self.ui_action.get_locator("button_account_name_xpath").click()
        self.ui_action.get_locator("button_logout_xpath").click()
        time.sleep(5)