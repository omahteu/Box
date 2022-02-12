from requests import post, get, delete


class Livia:
    def __init__(self):
        self.item = None
        self.dados = None
        self.url = None

    def livia_salva(self, url, dados):
        self.url = url
        self.dados = dados

        post(url, dados)
        print('Dados Salvos!')

    def livia_ler(self, url):
        self.url = url

        lendo = get(url)
        return lendo

    def livia_apaga(self, url, item):
        self.url = url
        self.item = item

        url_formatada = url + item

        delete(url_formatada)
        print('Item Excluido')
