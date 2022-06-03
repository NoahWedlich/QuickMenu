from QuickMenu import Menu

def main():
    menu = Menu()
    while True:
        try:
            menu.print_border()
            menu.print_header("MENU :) Was geht ")
            menu.print_navigation()
        except KeyboardInterrupt:
            menu.exit()
            break

if __name__ == '__main__':
    main()