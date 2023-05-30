from family_controller import DatabaseController
from database import Database

db = Database("bolt://44.193.5.126:7687", "neo4j",
              "restraints-cheeses-hunk")


controller = DatabaseController(db=db)


def seed():
    """
        Minha família
        Avó Materna - Eunice
        Avô Materno - Joaquim
        Avó Paterna - Tereza
        Avô Paterno - João
        Mãe - Adriana
        Pai - Gilson
        Irmã - Giovanna
        Tio Materno - Luiz
        Tia Materna - Flávia
        Tia Paterna - Jaqueline
        Tio Paterno - Jair
    """

    db.drop_all()

    # Criação dos nós
    eunice = controller.create_node(
        ["Person"], {"name": "Eunice", "age": 70, "sex": "F"})
    joaquim = controller.create_node(
        ["Person"], {"name": "Joaquim", "age": 75, "sex": "M"})
    tereza = controller.create_node(
        ["Person"], {"name": "Tereza", "age": 60, "sex": "F"})
    joao = controller.create_node(
        ["Person"], {"name": "João", "age": 60, "sex": "F"})
    adriana = controller.create_node(
        ["Person"], {"name": "Adriana", "age": 60, "sex": "F"})
    gilson = controller.create_node(
        ["Person"], {"name": "Gilson", "age": 60, "sex": "F"})
    giovanna = controller.create_node(
        ["Person"], {"name": "Giovanna", "age": 60, "sex": "F"})
    luiz = controller.create_node(
        ["Person"], {"name": "Luiz", "age": 60, "sex": "F"})
    flavia = controller.create_node(
        ["Person"], {"name": "Flávia", "age": 60, "sex": "F"})
    jaqueline = controller.create_node(
        ["Person"], {"name": "Jaqueline", "age": 60, "sex": "F"})
    jair = controller.create_node(
        ["Person"], {"name": "Jair", "age": 60, "sex": "F"})
    lucas = controller.create_node(
        ["Person"], {"name": "Lucas", "age": 60, "sex": "F"})

    # Criação dos relacionamentos
    controller.create_relationship(
        eunice, joaquim, "PARTNER_OF", {"since": "1970"})
    controller.create_relationship(
        tereza, joao, "PARTNER_OF", {"since": "1971"})
    controller.create_relationship(
        adriana, gilson, "PARTNER_OF", {"since": "2000"})
    controller.create_relationship(adriana, eunice, "PARENT_OF")
    controller.create_relationship(adriana, joaquim, "PARENT_OF")
    controller.create_relationship(gilson, tereza, "PARENT_OF")
    controller.create_relationship(gilson, joao, "PARENT_OF")
    controller.create_relationship(giovanna, gilson, "PARENT_OF")
    controller.create_relationship(giovanna, adriana, "PARENT_OF")
    controller.create_relationship(luiz, eunice, "PARENT_OF")
    controller.create_relationship(luiz, joaquim, "PARENT_OF")
    controller.create_relationship(flavia, eunice, "PARENT_OF")
    controller.create_relationship(flavia, joaquim, "PARENT_OF")
    controller.create_relationship(jaqueline, tereza, "PARENT_OF")
    controller.create_relationship(jaqueline, joao, "PARENT_OF")
    controller.create_relationship(jair, tereza, "PARENT_OF")
    controller.create_relationship(jair, joao, "PARENT_OF")
    controller.create_relationship(lucas, gilson, "PARENT_OF")
    controller.create_relationship(lucas, adriana, "PARENT_OF")
    # relacionamento de irmãos
    controller.create_relationship(
        giovanna, lucas, "SIBLING_OF", {"since": "2006"})

    # Criação de labels
    controller.create_label(eunice, "Grandmother")
    # eunice tbm é mãe
    controller.create_label(eunice, "Mother")
    controller.create_label(joaquim, "Grandfather")
    controller.create_label(joaquim, "Father")
    controller.create_label(tereza, "Grandmother")
    controller.create_label(tereza, "Mother")
    controller.create_label(joao, "Grandfather")
    controller.create_label(joao, "Father")
    controller.create_label(adriana, "Mother")
    controller.create_label(gilson, "Father")
    controller.create_label(giovanna, "Daughter")
    controller.create_label(luiz, "Uncle")
    controller.create_label(luiz, "Father")
    controller.create_label(flavia, "Aunt")
    controller.create_label(flavia, "Mother")
    controller.create_label(jaqueline, "Aunt")
    controller.create_label(jair, "Uncle")
    controller.create_label(jair, "Father")
    controller.create_label(lucas, "Son")


def buscas():

    print("Todas as pessoas:")
    family_members = controller.get_nodes()
    for member in family_members:
        print(member[0]._properties["name"])

    print("#"*10)

    print("Todas as mães:")
    family_members = controller.find_family_members_with_label("Mother")
    for member in family_members:
        print(member[0]._properties["name"])

    print("#"*10)

    print("Pais de Adriana:")
    ch = controller.find_parents_of("Adriana")
    for c in ch:
        print(c[0]._properties["name"])

    print("#"*10)

    print("Filhos de Eunice:")
    ch = controller.find_children_of("Eunice")
    for c in ch:
        print(c[0]._properties["name"])

    print("#"*10)

    print("Casado com Eunice:")
    ch = controller.find_partner_of("Eunice")
    for c in ch:
        print(c[0]._properties["name"])


def input_name():
    name = input("Digite o nome da pessoa: ")
    return name


def menu():
    print("1 - Buscar todas as pessoas")
    print("2 - Buscar todas as mães")
    print("3 - Buscar pais de uma pessoa")
    print("4 - Buscar filhos de uma pessoa")
    print("5 - Sair")


def validate_option():
    op = int(input("Digite a opção: "))
    while op < 1 or op > 5:
        print("Opção inválida")
        op = int(input("Digite a opção: "))
    return op


def get_all_people():
    family_members = controller.get_nodes()
    for member in family_members:
        print(member[0]._properties["name"])


def get_all_mothers():
    family_members = controller.find_family_members_with_label("Mother")
    for member in family_members:
        print(member[0]._properties["name"])


def get_parents_of():
    name = input_name()
    ch = controller.find_parents_of(name)
    for c in ch:
        print(c[0]._properties["name"])


def get_children_of():
    name = input_name()
    ch = controller.find_children_of(name)
    for c in ch:
        print(c[0]._properties["name"])


def main():
    # seed()

    while True:
        print("*"*10)
        menu()
        op = validate_option()
        if op == 1:
            get_all_people()
        elif op == 2:
            get_all_mothers()
        elif op == 3:
            get_parents_of()
        elif op == 4:
            get_children_of()
        elif op == 5:
            break

    db.close()


if __name__ == "__main__":
    main()
