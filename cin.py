from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

#configura o navegador
options = webdriver.ChromeOptions()
b = webdriver.Chrome(chrome_options=options)

#abre o site
b.get('http://www.contagem.mg.gov.br/sine/')

#busca e trata o html
element = b.find_element(By.XPATH,'/html/body/section[3]/div/div[4]/div')
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
vagas = soup.findAll('div', attrs={'class': 'card mb-3'})

#abre o arquivo para ser salvo
f = open('vagasSine.txt', 'a')

#varre todas as vagas salvando no arquivo
for vaga in vagas:
    vagaNome = vaga.find('div', attrs={'class':'card-header'})
    vagaDesc = vaga.find('p', attrs={'class':'card-text'})
    tudo = vagaNome.text, vagaDesc.text
    f.write(vagaNome.text)
    f.write(vagaDesc.text+"\n")

    