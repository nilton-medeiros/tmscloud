from typing import Tuple


def main():
    def get_first_and_last_name(full_name: str) -> Tuple[str, str | None]:
        """
        Extrai o primeiro e o último nome de uma string de nome completo.
        Retorna uma tupla (primeiro_nome, ultimo_nome).
        """
        list_names = full_name.split()
        first_name = list_names[0].strip().capitalize()
        last_name = list_names[-1].strip().capitalize() if len(list_names) > 1 else None

        return first_name, last_name

    primeiro_nome, segundo_nome = get_first_and_last_name("Angelina")

    if segundo_nome is not None:
        print(f"Sr(a). {primeiro_nome} {segundo_nome}")
    else:
        print(f"Sr. {primeiro_nome}")



if __name__ == "__main__":
    main()
