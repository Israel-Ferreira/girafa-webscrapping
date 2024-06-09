from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.by import By

from models.produto import Produto

import time

import utils



def instantiate_selenium():
    firefox_options =  FirefoxOptions()
    firefox_options.add_argument("--headless")

    return webdriver.Firefox(options=firefox_options)







if __name__ == "__main__":
    print("Crawler Girafa.com")

    produtos =  []

    with instantiate_selenium() as driver:
        driver.get("https://www.girafa.com.br/c/Smartphone/Celulares")

        time.sleep(30)

        elems = driver.find_elements(By.CLASS_NAME, "box-produto")

        for elem in elems:
            div_info = elem.find_element(By.CSS_SELECTOR, "div > div:nth-child(2) > a.informacao-produto")

            nome_produto =  div_info.find_element(By.TAG_NAME, "h2").text
            link_produto =  div_info.get_attribute("href")
            preco_produto_str =  div_info.find_element(By.CSS_SELECTOR, "div.valores>span.valor-vista").text


            # Formatando o Preço para o formato padrão e convertendo para float
            preco_produto_str = preco_produto_str.removeprefix("R$").strip().replace(".","").replace(",", ".")
            preco_produto = float(preco_produto_str)

            produto = Produto(nome_produto, preco_produto, link_produto)

            produtos.append(produto)

    utils.write_products_csv(produtos)
    
    


