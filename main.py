from core.menu import LittleGlueMenu


def main(*args, **kwargs):
    pass
   # TODO: Integrate with Google Fire and develop a interactive menu to generate new little glues


if __name__ == '__main__':
    VERSION = "1.0.0"
    menu = LittleGlueMenu(version=VERSION)
    menu.show_main_menu()
