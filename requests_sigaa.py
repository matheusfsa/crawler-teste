import requests


def request_disciplina(id_disciplina):
    url = "https://www.sigaa.ufs.br/sigaa/public/componentes/resumo.jsf"
    payload = "id=" + str(id_disciplina)
    headers = {
        'Connection': "keep-alive",
        'Cache-Control': "max-age=0",
        'Origin': "https://www.sigaa.ufs.br",
        'Upgrade-Insecure-Requests': "1",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': "_ga=GA1.2.932303132.1539527696; JSESSIONID=A3A4D61EEF04A0D41D015D4E08F8540D.cardeal1,_ga=GA1.2.932303132.1539527696; JSESSIONID=A3A4D61EEF04A0D41D015D4E08F8540D.cardeal1; JSESSIONID=5B0D1C4039109889853AF598DB1EA492.bemtevi1",
        'Postman-Token': "6a6bf5b1-dde0-4e84-bb7a-b835054de214,a91a2368-1082-4b47-8636-645317e30740",
        'Host': "www.sigaa.ufs.br",
        'content-length': "8",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    return response.text


def request_departamento(id_dep):
    url = "https://www.sigaa.ufs.br/sigaa/public/departamento/componentes.jsf"
    querystring = {"id":str(id_dep)}
    headers = {
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "40a5e80c-d01d-47a7-bb12-3034751f30d4,48572c73-ac8a-495d-9b12-1fe6bd9e156d",
        'Host': "www.sigaa.ufs.br",
        'cookie': "JSESSIONID=5B0D1C4039109889853AF598DB1EA492.bemtevi1",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

