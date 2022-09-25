import fire

from core.little_glue import LittleGlue
from core.menu import LittleGlueMenu
from core.json_data import JsonData


VERSION = "1.0.0"


class MainClass(object):
    @staticmethod
    def generate_from(from_file):
        if not from_file:
            return None

        little_glue = LittleGlue(**JsonData.get_data_from_json_file(from_file))
        little_glue.generate()
        print('Geração da colinha feita com sucesso! Verifique na pasta generated_glues.')

    @staticmethod
    def menu():
        menu = LittleGlueMenu(version=VERSION)
        menu.show_main_menu()

    @staticmethod
    def help():
        print("Little Glue - v{}".format(VERSION))
        print("====================")
        print("")
        print("Opções:")
        print("-------")
        print("- menu: Executa o programa com um menu interativo.")
        print("Exemplo: ./main menu")
        print("")
        print("- generate_from: Executa o programa e gera a colinha através do JSON passado nos parâmetros.")
        print("Exemplo: ./main generate_from candidates_json/meus_candidatos.json")
        print("")


if __name__ == '__main__':
    fire.Fire(MainClass)
