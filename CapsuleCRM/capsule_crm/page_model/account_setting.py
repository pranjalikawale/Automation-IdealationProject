from utility.UI_operation import UIOperation
from utility.constant import Constant
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

class AccountSettingPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.constant=Constant()
        self.ui_action=UIOperation(self.driver,self.constant.PATH_PROPERTY_FILE_ACCOUNT_PAGE)
    
    def account_details(self):
        self.ui_action.get_locator("link_account_xpath").click()
        title=self.ui_action.get_locator("text_account_title_xpath").text
        return title

    def upload_logo(self,logo):
        self.ui_action.get_locator("link_appearance_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_upload_logo_xpath").send_keys(logo)
        self.ui_action.get_locator("button_upload_save_xpath").click()
        time.sleep(5)
        status=self.ui_action.get_locator("text_upload_status_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return status

    def add_new_user(self):
        self.ui_action.get_locator("link_users_term_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_add_new_user_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_first_name_xpath").send_keys("Peter")
        self.ui_action.get_locator("textbox_last_name_xpath").send_keys("Stephen")
        self.ui_action.get_locator("textbox_email_xpath").send_keys("Peter@gmail.com")
        self.ui_action.get_locator("textbox_username_xpath").send_keys("PeterStephen")
        self.ui_action.get_locator("button_save_xpath").click()
        time.sleep(4)
        if self.driver.title=="Bridgelabz CRM":
            error_message= self.ui_action.get_locator("add_new_user_error_msg_xpath").text
            return error_message
        self.ui_action.get_locator("textbox_search_xpath").send_keys("PeterStephen")
        time.sleep(5)
        result_user=self.ui_action.get_locator("text_verify_user_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return result_user
        
    def add_new_milestone(self):
        self.ui_action.get_locator("link_milstone_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_add_milestone_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_milestone_name_xpath").send_keys("Adminstrator")
        self.ui_action.get_locator("textbox_milestone_probability_xpath").send_keys("100")
        self.ui_action.get_locator("textbox_days_stale_xpath").send_keys("12")
        self.ui_action.get_locator("button_save_milestone_xpath").click()
        time.sleep(5)
        result_milestone=self.ui_action.get_locator("text_verify_milestone_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return result_milestone

    def add_new_tracks(self):
        self.ui_action.get_locator("link_tracks_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_add_tracks_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_tracks_name_id").send_keys("Deployment")
        self.ui_action.get_locator("textbox_task_description_id").send_keys("Deployment")
        self.ui_action.get_locator("button_save_tracks_xpath").click()
        time.sleep(5)
        result_tracks=self.ui_action.get_locator("text_verify_tracks_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return result_tracks

    def add_new_task_category(self):
        self.ui_action.get_locator("link_category_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_add_category_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_category_name_xpath").send_keys("accont")
        self.ui_action.get_locator("button_save_category_xpath").click()
        time.sleep(5)
        result_category=self.ui_action.get_locator("text_verify_category_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return result_category

    def add_new_tags(self):
        self.ui_action.get_locator("link_tags_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("button_add_tags_xpath").click()
        time.sleep(5)
        self.ui_action.get_locator("textbox_tag_name_xpath").send_keys("Deployment")
        self.ui_action.get_locator("button_save_tag_xpath").click()
        time.sleep(5)
        result_tags=self.ui_action.get_locator("text_verify_tag_xpath").text
        time.sleep(5)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return result_tags

    def total_configure_button(self):
        self.ui_action.get_locator("link_integration_xpath").click()
        time.sleep(5)
        webelement=[]
        while True:
            try:
                # Define an element that you can start scraping when it appears
                # If the element appears after 5 seconds, break the loop and continue
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary.settings-page-integration-configure")))
                break
            except TimeoutException:
                # If the loading took too long, print message and try again
                print("Loading took too much time!")
        webelement=self.driver.find_elements_by_class_name("btn-primary.settings-page-integration-configure")
        count=len(webelement)
        self.ui_action.get_locator("account_link").click()
        time.sleep(5)
        return count
        
    def all_link_in_setting(self):
        webelement=[]
        while True:
            try:
                # Define an element that you can start scraping when it appears
                # If the element appears after 5 seconds, break the loop and continue
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "over-animator.sp-portal__primary-item")))
                break
            except TimeoutException:
                # If the loading took too long, print message and try again
                print("Loading took too much time!")

        webelement=self.driver.find_elements_by_class_name("over-animator.sp-portal__primary-item")
        for item in webelement:
            time.sleep(5)
            try:
                # Define an element that you can start scraping when it appears
                # If the element appears after 5 seconds, break the loop and continue
                item.click()
            except StaleElementReferenceException:
                print('StaleElementReferenceException while trying to type password, trying to find element again')
                element = self.driver.find_element_by_partial_link_text(item)
                element.click()
            self.driver.execute_script("window.history.go(-1)")



       