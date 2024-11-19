from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_FIELD=(By.CLASS_NAME,'ant-select-selection-search-input')
    TICKET_SELING=(By.CSS_SELECTOR,'#root > div.w-full.navbar.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > p')
    CAT_TEATRON_BUTTON=(By.CSS_SELECTOR,'#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[180px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.pl-1.md\:px-4.py-2.m-1.md\:my-2.md\:ml-2.transition.duration-300.ease-in-out.transform.hover\:border-primaryPurple.hover\:animate-border-anticlockwise.hover\:rounded-full > span')
    TEATRON_HEADER=(By.CSS_SELECTOR,'#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_MUSIC_BUTTON = (By.CSS_SELECTOR,'#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[160px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryBlue.hover\:animate-border-anticlockwise > span')
    MUSIC_HEADER=(By.CSS_SELECTOR,'#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_SPORT_BUTTON = (By.CSS_SELECTOR,'#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[160px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-primaryGreen.hover\:animate-border-anticlockwise > span')
    SPORT_HEADER=(By.CSS_SELECTOR,'#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_STENDUP_BUTTON = (By.CSS_SELECTOR,'#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[210px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryOrange.hover\:animate-border-anticlockwise > span')
    STENDUP_HEADER=(By.CSS_SELECTOR,'#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_KIDS_BUTTON = (By.CSS_SELECTOR,'#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[130px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.pr-1.pl-2.md\:px-6.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryYellow.hover\:animate-border-anticlockwise > span')
    KIDS_HEADER=(By.CSS_SELECTOR,'#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    SAFSAR_LOGO_BUTTON=(By.CSS_SELECTOR,'#root > main > div.w-full.navbar.bg-primaryLight.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > div.hidden.md\:flex.space-x-10.md\:w-\[500px\] > a > img')
    BIG_TITL = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.font-Zvulun.order-1.md\:order-1.col-span-4.md\:col-span-3.text-4xl.md\:text-6xl.text-white')
    ABOUT_US = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-2.md\:order-3.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(1) > a')
    HOW_IT_WORKS = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-2.md\:order-3.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(2) > a')
    Q_A = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-2.md\:order-3.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(3) > a')
    TICKET_SALES = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-2.md\:order-3.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(4) > a')
    CONTACT_US = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-2.md\:order-3.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(5) > a')
    TERMS = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-3.md\:order-4.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(1) > a')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-3.md\:order-4.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(2) > a')
    CANCEL_LATION = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-3.md\:order-4.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(2) > a')
    ACCSSIBILITY = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.order-3.md\:order-4.mt-8.col-span-2.md\:col-span-1 > ul > li:nth-child(4) > a')
    INSTAGRAM = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.pt-4.md\:pt-0.order-5.md\:order-2.col-span-1.flex.justify-end.items-end > li > a:nth-child(1) > img')
    FACEBOOK = (By.CSS_SELECTOR, '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center > div > div.grid.sm\:grid-cols-2.md\:grid-cols-4.gap-4.mt-0.mb-12 > div.pt-4.md\:pt-0.order-5.md\:order-2.col-span-1.flex.justify-end.items-end > li > a:nth-child(2) > img')





    def click_search_field(self):
        self.click_element(self.SEARCH_FIELD)
    def click_ticket_seling(self):
        self.click_element(self.TICKET_SELING)
    def click_cat_teatron_button(self):
        self.click_element(self.CAT_TEATRON_BUTTON)
    def click_cat_music_button(self):
        self.click_element(self.CAT_MUSIC_BUTTON)
    def click_cat_sport_button(self):
        self.click_element(self.CAT_SPORT_BUTTON)
    def click_cat_stendup_button(self):
        self.click_element(self.CAT_STENDUP_BUTTON)
    def click_cat_kids_button(self):
        self.click_element(self.CAT_KIDS_BUTTON)
    def click_safsar_logo(self):
        self.click_element(self.SAFSAR_LOGO_BUTTON)
        def click_big_title(self):
        self.click_element(self.BIG_TITLE)
    def click_about_us(self):
        self.click_element(self.ABOUT_US)
    def click_how_it_works(self):
        self.click_element(self.HOW_IT_WORKS)
    def click_questions_answers(self):
        self.click_element(self.Q_A)
    def click_ticket_sales(self):
        self.click_element(self.TICKET_SALES)
    def click_contact_us(self):
        self.click_element(self.CONTACT_US)
    def click_terms(self):
        self.click_element(self.TERMS)
    def click_privacy_policy(self):
        self.click_element(self.PRIVACY_POLICY)
    def click_cancel_lation(self):
        self.click_element(self.CANCEL_LATION)
    def click_accssibility(self):
        self.click_element(self.ACCSSIBILITY)
    def click_instagram(self):
        self.click_element(self.INSTAGRAM)
    def click_facebook(self):
        self.click_element(self.FACEBOOK)
