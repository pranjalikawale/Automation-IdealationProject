import pytest
import time
from selenium import webdriver
import sys
sys.path.append("C://Users/User/Desktop/python/CapsuleCRM")
from utility.constant import Constant
from utility.custom_logger import CustomLogger
from page_model.login import LoginPage
from page_model.home import HomePage
from page_model.account_setting import AccountSettingPage

@pytest.mark.usefixtures("initialize_driver")
class TestNegativeCaseInCapsuleCRM():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()
    
    def test_login_with_invalid_credentials(self):
        log_in=LoginPage(self.driver)
        error_msg=log_in.login_for_multiple_credential(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME_CREDENTAILS)
        assert error_msg=="Unrecognised username or password"
    
    def test_user_add(self):
        log_in=LoginPage(self.driver)
        log_in.login(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME_CREDENTIAL)
        time.sleep(5)
        home_page=HomePage(self.driver)
        home_page.account_option()
        time.sleep(5)
        account=AccountSettingPage(self.driver)
        status=account.add_new_user()
        assert status=="a user already exists with that username"  
        
    
        
        
    
    