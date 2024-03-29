import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#este código de JS dice que, dentro del DOM encuentra los elementos con una clase determinada y haz scroll vertical "x" número de pixels.
#Tenemos que saber cual es el contenedor al que vamos hacer scroll para introducirlo dentro de nuestro script
scrollingScript = """
    document.getElementsByClassName('m6QErb DxyBCb kA9KIf dS8AEf')[0].scroll(0, 2000000)
"""#esto es una cadena de texto NO UN COMENTARIO xD

#rotamos user-agents
with open('user-agents.txt', 'r', encoding="utf-8") as f:
    user_agents = [(line.strip()) for line in f.readlines()]
#opciones necesarias
opts = Options()
opts.add_argument("--profile-directory=Profile 2")
opts.add_argument(f"user-agent={random.choice(user_agents)}")
opts.add_argument("--start-maximized")
#opts.add_argument("--proxy-server=geo.iproyal.com:22323")
#opts.add_argument("--headless")
#time.sleep(random.uniform(3, 10))
#pasamos instrucciones a nuestro driver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',chrome_options=opts)
url_google = 'https://www.google.com/maps/place/Restaurant+Port+Pesquer/@41.675297,2.8005786,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipNikjbJbhA7JYeoQH94MOo6RTySgnb4OG3VBtHk!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNikjbJbhA7JYeoQH94MOo6RTySgnb4OG3VBtHk%3Dw203-h114-k-no!7i2923!8i1645!4m7!3m6!1s0x12bb16464da8c7b3:0x118529eaf9214b5d!8m2!3d41.6751137!4d2.800596!14m1!1BCgIgAQ'
ir_url_google = driver.get(url_google)
time.sleep(3)
try:
#cookies
    galletas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button/div[contains(text(),"Rechazar todo")]')))
    galletas.click()
except Exception as error:
    print(error, "Error en la ventana de cookies-1")
#enviamos al driver de selenium a la url de google maps concreta
time.sleep(3)
#scrolling antes de extraer datos con un while
SCROLLS = 0
while (SCROLLS != 18):
    driver.execute_script(scrollingScript)#esto permite ejecutar código de JS
    time.sleep(random.uniform(1.2, 2.9))
    SCROLLS += 1
#buscar bloques
time.sleep(3)
encontrar_bloques_fotos = driver.find_elements(By.XPATH, '//a[contains(@data-photo-index,"")]')
#url = []
a = 1
f = open("urls_img.csv", "a", encoding="utf-8")
for u in encontrar_bloques_fotos:
    u.click()
    time.sleep(random.uniform(2.0,3.0))
    buscar_url = u.find_element(By.XPATH, './/div[@class="Uf0tqf loaded"]').get_attribute("style")
    fecha = u.find_element(By.XPATH, '//div[@class="SAtV7"]').text
    #url.append(buscar_url.get_attribute("style"))
    #strurl = "".join(url)
    time.sleep(random.uniform(1.0,2.0))
    #print(a, fecha, buscar_url)
    a += 1
    try:
        f.write(str(a) + "$" + str(fecha) + "$" + buscar_url + "\n")
    except Exception as e:
        print("error:", e)
f.close()
"""
bloques_foto = []
i = 0
for tag_a in encontrar_bloques_fotos:
    bloques_foto.append(tag_a.get_attribute())
for u in range(0, 60):
    for bloques in encontrar_bloques_fotos:
        url_img = bloques.find_element(By.XPATH, './/div[contains(@class,"Uf0tqf")]')
        url_imgstr = "".join(url_img)
        time.sleep(random.uniform(1.0,2.0))
        i += 1
        print(i, url_imgstr)
        
        
        
"""