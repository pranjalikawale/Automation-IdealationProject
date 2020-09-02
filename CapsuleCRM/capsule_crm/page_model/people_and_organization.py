from utility.UI_operation import UIOperation
from utility.constant import Constant
from utility.xls_util import XlsUtility

class PeopleAndOrganizationPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_PEOPLE_AND_ORGANIZATION)
    
    def add_person(self,path,sheet):
        data=[]
        data=XlsUtility.read_data_from_sheet(path,sheet)
        self.ui_action.get_locator("button_add_person_xpath").click()
        self.ui_action.get_locator("drop_down_title_xpath").click()
        self.ui_action.get_locator("select_mr_xpath").click()
        self.ui_action.get_locator("textbox_first_name_xpath").send_keys(data[1])
        self.ui_action.get_locator("textbox_last_name_xpath").send_keys(data[2])
        self.ui_action.get_locator("textbox_job_title_xpath").send_keys(data[3])
        self.ui_action.get_locator("textbox_organization_xpath").send_keys(data[4])
        self.ui_action.get_locator("list_organization_xpath").click()
        self.ui_action.get_locator("textbox_tags_xpath").send_keys(data[5])
        self.ui_action.get_locator("list_tags_xpath").click()
        self.ui_action.get_locator("textbox_phone_xpath").send_keys(data[6])
        self.ui_action.get_locator("textbox_email_xpath").send_keys(data[8])
        self.ui_action.get_locator("textbox_social_network_xpath").send_keys(data[10])
        self.ui_action.get_locator("button_add_address_xpath").click()
        self.ui_action.get_locator("textarea_address_xpath").send_keys(data[13])
        self.ui_action.get_locator("textbox_city_xpath").send_keys(data[15])
        self.ui_action.get_locator("textbox_state_xpath").send_keys(data[16])
        self.ui_action.get_locator("textbox_zip_xpath").send_keys(data[17])
        self.ui_action.get_locator("drop_down_country_xpath").click()
        self.ui_action.get_locator("search_country_xpath").send_keys(data[18])
        self.ui_action.get_locator("select_country_xpath").click()
        self.ui_action.get_locator("button_save_xpath").click()
        


        
    


