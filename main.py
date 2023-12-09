from logic import *  # import statement needed to gain access to logic class


def main():
    application = QApplication([])
    window = Calc()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
