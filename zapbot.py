from selenium import webdriver
import time

class WhatsappBot:
    def _init_(self):
        self.mensage = " Bom Dia"
        self.grupos = ["Audios"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'.chromedriver.exe')

    def EviarMensagens(self):
        # <span dir="auto" title="Audios" class="_3ko75 _5h6Y_ _3Whw5">Audios</span>
        # <div tabindex="-1" class="_2FVVk _2UL8j">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_2FVVk _2UL8j')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensage)
            botao_enviar = self.driver.find_elements_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

#bot = WhatsappBot()
#bot.EviarMensagens()
            
        