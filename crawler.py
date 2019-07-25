import data_extraction as de
import requests_sigaa as rs


def get_all_deps():
    return de.get_departamentos(open("departamentos.html", encoding="ISO-8859-1"))


def get_n_disciplinas(dep_id, ini, n):
    dep_page = rs.request_departamento(dep_id)
    disciplinas = []
    discs = de.get_disciplinas(dep_page)
    for i in range(ini, min(ini+n, len(discs))):
        id_disc = discs[i]['id']
        disc_page = rs.request_disciplina(id_disc)
        disciplinas.append(de.get_info_disc(disc_page, id_disc))
    return disciplinas
