from utility.UI_operation import UIOperation
from utility.constant import Constant
from utility.xls_util import XlsUtility
import time
from selenium import webdriver

class CasePage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_CASE)
    
    def create_case(self,path,sheet):
        data=[]
        data=XlsUtility.read_data_from_sheet(path,sheet)
        self.ui_action.get_locator("button_add_case_xpath").click()
        self.ui_action.get_locator("textbox_case_relates_to_xpath").send_keys(data[0])
        self.ui_action.get_locator("button_case_relates_to_xpath").click()
        self.ui_action.get_locator("textbox_case_name_xpath").send_keys(data[1])
        self.ui_action.get_locator("button_save_xpath").click()
        time.sleep(10)
        name=self.ui_action.get_locator("text_name_xpath").text
        status=self.ui_action.get_locator("text_status_xpath").text
        return name,status