# Importando nossas bibliotecas.
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'


class IniciandoSite:
    URL = url
    html = requests.get(URL).content
    soup = BeautifulSoup(html, 'html.parser')
    driver.get(URL)

    options_uf = soup.find_all(name='option')
    lista_ufs = []
    for uf in range(2, 29):
        lista_ufs.append(uf)

    # Procurando UF e "clicando" em uma das opções.
    # As opções vão de 2 a 28.
    driver.find_element_by_name("UF").find_element_by_xpath(
        f"/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div/div/span[2]/label/select/option[{25}]").click() # 25 == Santa Catarina.

    # Clicando em "Buscar".
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/form/div/div/div[4]/input").click()


class ProcurandoTabela:
    while True:
        url_atual = driver.current_url # Obtendo a url atual

        print(url_atual) # Mostrando na tela

        sleep(5)

        # Se tiver proxima página de tabela, irá "clicar".
        if driver.find_element_by_link_text(
                "[ Próxima ]"):
            driver.find_element_by_link_text(
                "[ Próxima ]").click()
        # Se não tiver, encerraremos nosso programa.
        else:
            driver.quit()
            break








