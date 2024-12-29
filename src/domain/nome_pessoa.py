class NomePessoa:
    def __init__(self, primeiro_nome: str, ultimo_nome: str = None):
        if not primeiro_nome and not ultimo_nome:
            raise ValueError("Os nomes não podem ser vazios.")

        self.primeiro_nome = None
        self.ultimo_nome = ''

        if primeiro_nome:
            self.primeiro_nome = primeiro_nome.strip().capitalize()
            if ultimo_nome:
                self.ultimo_nome = ultimo_nome.strip().capitalize()
        else:
            self.primeiro_nome = ultimo_nome.strip().capitalize()

    @property
    def nome_completo(self) -> str:
        return f"{self.primeiro_nome} {self.ultimo_nome}"

    @property
    def nome_completo_maiusculo(self) -> str:
        return self.nome_completo.upper()



# Exemplo de uso:
'''
try:
    pessoa = NomePessoa("João", "Silva")
    print("Primeiro nome:", pessoa.primeiro_nome)
    print("Último nome:", pessoa.ultimo_nome)
    print("Nome completo:", pessoa.nome_completo)
    print("Nome completo em maiúsculo:", pessoa.nome_completo_maiusculo)

    # Testando com nome vazio
    pessoa_invalida = NomePessoa("", "Silva")
except ValueError as e:
    print("Erro:", e)
'''
