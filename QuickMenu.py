import os

class Menu:

    def __init__(self):
        self.__prepare_terminal()

    def __prepare_terminal(self) -> None:
        os.system("color")
        self.width, self.height = os.get_terminal_size()
        self.header_height = 1
        self.navigation_width = self.width // 5
        self.__move_cursor()
        print("\u001b[J", end="")
        self.__hide_cursor()

    def __move_cursor(self, x: int = 1, y: int = 1) -> None:
        print(f"\u001b[{y};{x}H", end="")

    def __hide_cursor(self) -> None:
        print("\u001b[?25l", end="")

    def __show_cursor(self) -> None:
        print("\u001b[?25h", end="")

    def __get_text_offset(self, total_width: int, text: str) -> int:
        return min(total_width//2 + (len(text) // 2), total_width)

    def print_border(self):
        self.__move_cursor()
        print(u"\u2554", end="")
        self.__move_cursor(self.width, 0)
        print(u"\u2557", end="")
        self.__move_cursor(0, self.height)
        print(u"\u255A", end="")
        self.__move_cursor(self.width, self.height)
        print(u"\u255D", end="")
        for x in range(2, self.width):
            self.__move_cursor(x, 1)
            print(u"\u2550", end="")
            self.__move_cursor(x, self.height)
            print(u"\u2550", end="")
            self.__move_cursor(x, self.header_height + 2)
            print(u"\u2550", end="")
        for y in range(2, self.height):
            self.__move_cursor(1, y)
            print(u"\u2551", end="")
            self.__move_cursor(self.width, y)
            print(u"\u2551", end="")
        self.__move_cursor(1, self.header_height + 2)
        print(u"\u2560", end="")
        self.__move_cursor(self.width, self.header_height + 2)
        print(u"\u2563", end="")
        self.__move_cursor()

    def print_header(self, text: str):
        self.__move_cursor(self.__get_text_offset(self.width, text), self.header_height + 1)
        print(text, end="")
        self.__move_cursor()

    def print_navigation(self):
        for y in range(self.header_height + 3, self.height):
            self.__move_cursor(self.width - self.navigation_width, y)
            print(u"\u2551", end="")
        self.__move_cursor(self.width - self.navigation_width, self.header_height + 2)
        print(u"\u2566", end="")
        self.__move_cursor(self.width - self.navigation_width, self.height)
        print(u"\u2569", end="")
        self.__move_cursor(self.width - self.__get_text_offset(self.navigation_width, "123456789123456789123456789"), self.header_height + 3)
        print("123456789123456789123456789", end="")

    def exit(self):
        self.__move_cursor(self.width, self.height)
        self.__show_cursor()
        