from utility.UI_operation import UIOperation
from utility.constant import Constant
from utility.xls_util import XlsUtility
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_lOGIN)

    def login(self,path,sheet):
        data=[]
        data=XlsUtility.read_data_from_sheet(path,sheet)
        self.ui_action.get_locator("textbox_username_id").clear()
        self.ui_action.get_locator("textbox_username_id").send_keys(data[0])
        self.ui_action.get_locator("textbox_password_id").send_keys(data[1])
        self.ui_action.get_locator("button_login_id").click()

    def login_for_multiple_credential(self,path,sheet):
        rows=XlsUtility.get_row_count(path,sheet)
        for row in range(2,rows+1):
            username=XlsUtility.read_data_sheet(path,sheet,row,1)
            password=XlsUtility.read_data_sheet(path,sheet,row,2)
            #self.ui_action.get_locator("textbox_username_id").send_keys(Keys.CONTROL + "a")
            #self.ui_action.get_locator("textbox_username_id").send_keys(Keys.DELETE)
            time.sleep(5)
            self.ui_action.get_locator("textbox_username_id").clear()
            self.ui_action.get_locator("textbox_username_id").send_keys(username)
            self.ui_action.get_locator("textbox_password_id").send_keys(password)
            self.ui_action.get_locator("button_login_id").click()
            time.sleep(5)
        error_msg=self.ui_action.get_locator("text_invalid_credentail_error_xpath").text
        return error_msg
            


    