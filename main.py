from QuickMenu import Menu

def main():
    menu = Menu()
    menu.print_border()
    while True:
        menu.print_header("MENU :) Was geht ")
        menu.print_navigation()

if __name__ == '__main__':
    main()