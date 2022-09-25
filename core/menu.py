import json

from consolemenu import ConsoleMenu, MenuFormatBuilder, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem
from consolemenu.format import MenuBorderStyleType

from core.json_data import JsonData
from core.little_glue import LittleGlue


class LittleGlueMenu(object):
    def __init__(self, **kwargs):
        self.version = kwargs.get('version')

    def show_main_menu(self):
        """
        Main Menu
        :return: None
        """
        menu = ConsoleMenu(
            "Little Glue - v{}".format(self.version),
            "Aquele programinha maroto pra fazer aquela colinha marota pras eleições!",
            exit_option_text='Sair',
            formatter=LittleGlueMenu.get_menu_format(),
            clear_screen=True
        )
        json_data_menu = self.__get_json_data_menu()

        item_little_glue_create = FunctionItem(
            "Criar colinha de candidatos",
            function=self.__execute_selected_method,
            args=["register", self.__get_new_data, []]
        )
        item_little_glue_from_data = SubmenuItem("Criar colinha com dados salvos", submenu=json_data_menu)

        menu.append_item(item_little_glue_create)
        menu.append_item(item_little_glue_from_data)
        menu.show()

    # Auxiliary Methods
    # -----------------
    def __get_json_data_menu(self):
        """
        Menu to list JSON data files
        :return: SelectionMenu object
        """
        menu = SelectionMenu(
            title="Little Glue - v{}".format(self.version),
            subtitle="Alguns dados salvos foram encontrados. Você deseja selecionar um deles para gerar a colinha?",
            exit_option_text='Voltar',
            formatter=LittleGlueMenu.get_menu_format(),
            clear_screen=True,
            strings=[]
        )
        files = JsonData.get_json_data_files()
        for index, item in enumerate(files):
            data_item = FunctionItem(
                "{}".format(item),
                function=self.__execute_selected_method,
                args=["json_data_generate", None, [item]]
            )
            menu.append_item(data_item)

        return menu

    def __execute_selected_method(self, method_type, method, args_list):
        """

        :param method_type: 'json_data_generate' generate little glues from JSON data | 'register' registers a new one
        :param method: Method to be called. Can be set to None in case of 'json_data_generate' method type.
        :param args_list: List of arguments to be passed to the selected method.
        :return: None
        """
        if method_type == 'json_data_generate':
            file = open("candidates_json/{}".format(args_list[0]), "r")
            data = json.loads(file.read())

            little_glue = LittleGlue(**data)
            little_glue.generate()
        elif method_type == 'register':
            data = method()

            little_glue = LittleGlue(**data)
            little_glue.generate()
        else:
            raise ValueError("Tipo de método desconhecido.")

        self.__show_finished_menu()

    def __show_finished_menu(self):
        """
        Finished prompt screen.
        :return: None
        """
        menu = ConsoleMenu(
            title="Geração da colinha feita com sucesso!",
            subtitle="Você poderá ver sua colinha dentro da pasta generated_glues, na raíz do programa.",
            exit_option_text='Concluído',
            formatter=LittleGlueMenu.get_menu_format(),
            clear_screen=True
        )
        menu.show()

    def __get_new_data(self):
        """
        Basic prompts to assemble a new JSON data to be used to generate new little glues.
        :return: dict
        """
        print("Primeiro será necessário informar que tipo de eleição será!")
        print("-----------------------------------------------------------")
        election_type = input("Tipo de eleição [p = Presidencial | m = Municipal | o = Outro (Especifique)]: ")
        if election_type.lower() == 'p':
            election_type = 'presidential'
        elif election_type.lower() == 'm':
            election_type = 'municipal'

        candidates_dict = {}
        candidate_type = ''
        print("\n")
        print("Agora iremos cadastrar os candidatos nesta eleição! Por favor, selecione as opções abaixo.")
        print("------------------------------------------------------------------------------------------")
        ct_input = "Tipo de candidato [v = Vereador | p = Prefeito | de = Dep. Estadual | df = Dep. Federal | se = " \
                   "Senador | g = Governador | pr = Presidente | s = Sair]: "
        while candidate_type.lower() != 's':
            candidate_type = input(ct_input)
            if candidate_type.lower() == 's':
                break

            candidate_name = input("Nome do candidato: ")
            candidate_number = input("Número do candidato: ")
            candidate_dict = {
                "number": candidate_number,
                "name": candidate_name
            }

            print()
            if candidate_type.lower() == 's':
                break
            elif candidate_type.lower() == 'v':
                if not candidates_dict.get('alderman'):
                    candidates_dict['alderman'] = []
                candidates_dict['alderman'].append(candidate_dict)
            elif candidate_type.lower() == 'p':
                candidates_dict['prefect'] = candidate_dict
            elif candidate_type.lower() == 'de':
                if not candidates_dict.get('state_deputy'):
                    candidates_dict['state_deputy'] = []
                candidates_dict['state_deputy'].append(candidate_dict)
            elif candidate_type.lower() == 'df':
                if not candidates_dict.get('federal_deputy'):
                    candidates_dict['federal_deputy'] = []
                candidates_dict['federal_deputy'].append(candidate_dict)
            elif candidate_type.lower() == 'se':
                if not candidates_dict.get('senator'):
                    candidates_dict['senator'] = []
                candidates_dict['senator'].append(candidate_dict)
            elif candidate_type.lower() == 'g':
                candidates_dict['governor'] = candidate_dict
            elif candidate_type.lower() == 'pr':
                candidates_dict['president'] = candidate_dict
            else:
                break

        print("\n")
        print("Agora preciso que informe o tipo de arquivo que a exportação terá!")
        print("------------------------------------------------------------------")
        export_format = input("Tipo de arquivo [pdf = Formato PDF | jpg/jpeg = Imagem JPG]: ")

        print("\n")
        print("E para os toques finais! Preciso que selecione algumas opções para a aparência da colinha!")
        print("------------------------------------------------------------------------------------------")
        color_scheme_background = input("Cor de fundo (padrão #ffffff): ")
        color_scheme_font = input("Cor da fonte (padrão #000000): ")
        candidate_name_font_size = input("Tamanho da fonte no nome do candidato (padrão 18): ")
        candidate_number_font_size = input("Tamanho da fonte no número do candidato (padrão 42): ")
        candidate_number_font_spacing = input("Espaçamento da fonte no número do candidato (padrão 20): ")
        is_bold = input("Fonte em negrito? (s = Sim (padrão) | n = Não): ")

        if not color_scheme_background:
            color_scheme_background = "#ffffff"
        if not color_scheme_font:
            color_scheme_font = "#000000"
        if not candidate_number_font_size:
            candidate_number_font_size = 42
        if not candidate_name_font_size:
            candidate_name_font_size = 18
        if not candidate_number_font_spacing:
            candidate_number_font_spacing = 20
        if is_bold.lower() == 's':
            bold_type = 'bold'
        else:
            bold_type = 'normal'

        color_scheme = [color_scheme_background, color_scheme_font]
        font_configs = [candidate_name_font_size, candidate_number_font_size, candidate_number_font_spacing, bold_type]

        print("\n")
        print("E pronto! Agora iremos gerar a colinha!")
        print("---------------------------------------")
        input("Pressione ENTER para continuar...")

        data_dict = dict(
            election_type=election_type,
            candidates_data=candidates_dict,
            color_scheme=color_scheme,
            font_configs=font_configs,
            export_format=export_format
        )

        JsonData.save_json_data(data_dict)
        return data_dict

    # Static Methods
    # --------------
    @staticmethod
    def get_menu_format():
        """
        Menu format to be used by the program menus.
        :return: None
        """
        return MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.ASCII_BORDER) \
            .set_prompt(">> ") \
            .set_title_align('center') \
            .set_subtitle_align('center') \
            .set_left_margin(4) \
            .set_right_margin(4) \
            .show_header_bottom_border(True)
