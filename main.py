from QuickMenu import Menu

def main():
    menu = Menu()
    menu.print_border()
    menu.print_header("MENU :) Was geht ")
    while True:
        try:
            menu.print_navigation()
        except KeyboardInterrupt:
            menu.exit()
            break

if __name__ == '__main__':
    main()