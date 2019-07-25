from bs4 import BeautifulSoup
import re
import  os
from selenium import webdriver



def get_departamentos(dep_page):
    soup = BeautifulSoup(dep_page, "html.parser")
    tabela = soup.findAll("table", {"class":"listagem"})[0]
    linhas = tabela.find_all('tr')
    centros = [[]]
    centro = []
    for linha in linhas:
        if linha.find('span'):
            if centro:
                centros.append(centro)
                centro = []
        else:
            if linha.a:
                centro.append(linha)
    del centros[0:4]
    del centros[-1]
    departamentos = []
    i = 0
    for c in centros:
        if c:
            for departamento in c:
                i += 1
                nome = departamento.a.text.replace('\t', '').replace('\n', '')
                dep_id = str(departamento.a['href']).split('id=')[1]
                departamentos.append({'nome': nome, 'dep_id': dep_id})
    return departamentos

def get_disciplinas_w_sel(id_dep, ini, fim):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-svm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    driver.get("https://www.sigaa.ufs.br/sigaa/public/departamento/componentes.jsf?id="+ str(id_dep))
    disciplinas = []
    for i in range(ini, fim):
        disciplinas_link = driver.find_elements_by_xpath("//a[@title='Visualizar Detalhes do Componente Curricular']")
        disciplinas_link[i].click()
        html_str = driver.page_source
        disciplinas.append(get_info_disc(html_str))
        driver.back()
    return disciplinas

def get_disciplinas(dep_page):
    soup = BeautifulSoup(dep_page, "html.parser")
    tabelas = soup.find_all('table')
    linhas = tabelas[1].find_all('tr') + tabelas[2].find_all('tr')
    disciplinas = []
    for linha in linhas:
        id = re.findall(',[0-9]+,', linha.a['onclick'])[0].replace(',', '')
        nome = linha.find('td', {'class': 'nome'}).text
        disciplinas.append({'nome': nome, 'id': id})
    return disciplinas


def get_info_disc(disc_page):
    soup = BeautifulSoup(disc_page, "html.parser")
    tabela = soup.table
    linhas = tabela.find_all('tr')
    del linhas[14:]
    del linhas[5]
    del linhas[9]
    del linhas[2]
    del linhas[3]
    disciplina = dict()
    #disciplina['id'] = id_disc
    for linha in linhas:
        if linha.th and linha.td:
            disciplina[linha.th.text.replace(': ', '')] = linha.td.text.replace('\t', '').replace('\n', '')
    cursos = soup.find_all('table', {'id': 'form:listaCurriculosComponente'})[0].tbody.find_all('tr')
    curriculos = []
    for curso in cursos:
        nome = curso.find_all('td', {'class': 'colMatriz'})[0].text.split(' - ')[0]
        obg = curso.find_all('td', {'class': 'colObg'})[0].text == 'Sim'
        periodo = curso.find_all('td', {'class': 'colPeriodo'})[0].text
        ativo = curso.find_all('td', {'class': 'colAtivo'})[0].text == 'Sim'
        curriculos.append({'nome': nome, 'obg': obg, 'periodo': periodo, 'ativo': ativo})
    disciplina['curriculos'] = curriculos
    return disciplina



