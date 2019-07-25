from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_disciplinas(id_dep, ini, fim):
    driver = webdriver.Chrome()
    driver.get("https://www.sigaa.ufs.br/sigaa/public/departamento/componentes.jsf?id="+ str(id_dep))
    disciplinas = []
    for i in range(ini, fim):
        disciplinas_link = driver.find_elements_by_xpath("//a[@title='Visualizar Detalhes do Componente Curricular']")
        #html_file = open("/htmls-disciplinas/disciplina"+ str(i) + ".html", "w")
        disciplinas_link[i].click()
        html_str = driver.page_source
        disciplinas.append(html_str)
        driver.back()

def salva_html(html_src, html_str):
    html_file = open(html_src, "w")
    html_file.write(html_str)
    html_file.close()