from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extrair_webtoons():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    url = "https://www.webtoons.com/en/ranking/trending"
    driver.get(url)

    elementos = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.webtoon_list li"))
    )

    print("Quantidade de elementos:", len(elementos))

    dados = []

    for item in elementos:
        try:
            titulo = item.find_element(By.CSS_SELECTOR, "strong.title").text
            genero = item.find_element(By.CSS_SELECTOR, ".genre").text
            likes = item.find_element(By.CSS_SELECTOR, ".view_count").text

            dados.append({
                "titulo": titulo,
                "genero": genero,
                "likes": likes
            })

        except Exception as e:
            print("Erro:", e)

    driver.quit()
    return dados