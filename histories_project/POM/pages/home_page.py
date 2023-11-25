from selenium.webdriver.common.by import By

from histories_project.POM.lib.helpers import Helpers


class HomePage(Helpers):

    how_christmas_start_link =(By.LINK_TEXT, 'How Did Christmas Start?')

    def click_on_christmas_start_link(self):
        self.find_and_click(self.how_christmas_start_link)

