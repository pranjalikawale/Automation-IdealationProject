import pytest
import time
import sys
sys.path.append("C://Users/User/Desktop/python/CapsuleCRM")
from utility.UI_operation import UIOperation
from utility.constant import Constant
from page_model.login import LoginPage
from page_model.home import HomePage
from page_model.case import CasePage
from page_model.logout import LogoutPage
from page_model.people_and_organization import PeopleAndOrganizationPage
from page_model.account_setting import AccountSettingPage
from selenium import webdriver

@pytest.mark.usefixtures("initialize_driver")
class TestCapsuleCRM():
    
    @pytest.fixture(autouse=True)
    def initial_setup(self,initialize_driver):
        self.driver=initialize_driver
        self.constant=Constant()

    def test_login(self):
        log_in=LoginPage(self.driver)
        log_in.login(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME_CREDENTIAL)
        time.sleep(10)
        assert self.driver.title=="Dashboard | Bridgelabz CRM"
    
    def test_new_person_added(self):
        home_page=HomePage(self.driver)
        home_page.people_and_organization()
        people=PeopleAndOrganizationPage(self.driver)
        people.add_person(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME_PERSON)
        time.sleep(10)
        assert self.driver.title=="Jon Thomas | Bridgelabz CRM"

    def test_new_person_case(self):
        home_page=HomePage(self.driver)
        home_page.case()
        case_page=CasePage(self.driver)
        name,status=case_page.create_case(self.constant.PATH_TESTDATA,self.constant.SHEET_NAME_CASE)
        time.sleep(10)
        assert name=="Jon Thomas" and status=="Open" 
    
    def test_tags_added(self):
        home_page=HomePage(self.driver)
        home_page.account_option()
        time.sleep(5)
        account=AccountSettingPage(self.driver)
        status=account.add_new_tags()
        time.sleep(10)
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="Deployment" 
    
    def test_task_category_add(self):
        account=AccountSettingPage(self.driver)
        status=account.add_new_task_category()
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="accont" 
    
    def test_tracks_added(self):
        account=AccountSettingPage(self.driver)
        status=account.add_new_tracks()
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="Deployment" 
    
    def test_milestone_added(self):
        account=AccountSettingPage(self.driver)
        status=account.add_new_milestone()
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="Adminstrator" 

    def test_user_add(self):
        account=AccountSettingPage(self.driver)
        status=account.add_new_user()
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="Peter Stephen · PeterStephen"  

    def test_total_configure_button(self):
        account=AccountSettingPage(self.driver)
        status=account.total_configure_button()
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status==11
     
    def test_upload_logo_image_in_appearance(self):
        account=AccountSettingPage(self.driver)
        status=account.upload_logo(self.constant.PATH_LOGO_IMAGE)
        assert self.driver.title=="Account Settings | Bridgelabz CRM" and status=="Current logo image"
    
    def test_logout(self):
        log_out=LogoutPage(self.driver)
        log_out.logout()
        assert self.driver.title=="Bridgelabz CRM"




    


    

    

    
    
       

    
 
    