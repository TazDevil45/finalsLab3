from PyQt6.QtWidgets import *
from gui import *


class Calc(QMainWindow, Ui_MainWindow):
    """
    A class representing details for a calulator object
    """
    def __init__(self) -> None:
        """
        Method that creates a calulator object with a 0 in the values and a default addition operation
        """
        super().__init__()
        self.setupUi(self)

        self.values = [0]
        self.operations = [-1]
        self.position = 0

        self.num0.clicked.connect(lambda: self.zero())
        self.num1.clicked.connect(lambda: self.one())
        self.num2.clicked.connect(lambda: self.two())
        self.num3.clicked.connect(lambda: self.three())
        self.num4.clicked.connect(lambda: self.four())
        self.num5.clicked.connect(lambda: self.five())
        self.num6.clicked.connect(lambda: self.six())
        self.num7.clicked.connect(lambda: self.seven())
        self.num8.clicked.connect(lambda: self.eight())
        self.num9.clicked.connect(lambda: self.nine())

        self.addition.clicked.connect(lambda: self.add())
        self.subtraction.clicked.connect(lambda: self.subtract())
        self.multiplication.clicked.connect(lambda: self.multiply())
        self.division.clicked.connect(lambda: self.divide())

        self.buttonclear.clicked.connect(lambda: self.redo())
        self.buttoncalculate.clicked.connect(lambda: self.calculate())

    def zero(self) -> None:
        """
        Adds a 0 to the end of the current number on the calculator or if the number is 0 keeps it the same
        """
        if self.answer.text() == '0':
            self.answer.setText('0')
        else:
            self.answer.setText(self.answer.text() + '0')

    def one(self) -> None:
        """
        Adds a 1 to the end of the current number on the
        calculator or if the number is 0 changes it to 1
        """
        if self.answer.text() == '0':
            self.answer.setText('1')
        else:
            self.answer.setText(self.answer.text() + '1')

    def two(self) -> None:
        """
        Adds a 2 to the end of the current number on the
        calculator or if the number is 0 changes it to 2
        """
        if self.answer.text() == '0':
            self.answer.setText('2')
        else:
            self.answer.setText(self.answer.text() + '2')

    def three(self) -> None:
        """
        Adds a 3 to the end of the current number on the
        calculator or if the number is 0 changes it to 3
        """
        if self.answer.text() == '0':
            self.answer.setText('3')
        else:
            self.answer.setText(self.answer.text() + '3')

    def four(self) -> None:
        """
        Adds a 4 to the end of the current number on the
        calculator or if the number is 0 changes it to 4
        """
        if self.answer.text() == '0':
            self.answer.setText('4')
        else:
            self.answer.setText(self.answer.text() + '4')

    def five(self) -> None:
        """
        Adds a 5 to the end of the current number on the
        calculator or if the number is 0 changes it to 5
        """
        if self.answer.text() == '0':
            self.answer.setText('5')
        else:
            self.answer.setText(self.answer.text() + '5')

    def six(self) -> None:
        """
        Adds a 6 to the end of the current number on the
        calculator or if the number is 0 changes it to 6
        """
        if self.answer.text() == '0':
            self.answer.setText('6')
        else:
            self.answer.setText(self.answer.text() + '6')

    def seven(self) -> None:
        """
        Adds a 7 to the end of the current number on the
        calculator or if the number is 0 changes it to 7
        """
        if self.answer.text() == '0':
            self.answer.setText('7')
        else:
            self.answer.setText(self.answer.text() + '7')

    def eight(self) -> None:
        """
        Adds an 8 to the end of the current number on the
        calculator or if the number is 0 changes it to 8
        """
        if self.answer.text() == '0':
            self.answer.setText('8')
        else:
            self.answer.setText(self.answer.text() + '8')

    def nine(self) -> None:
        """
        Adds a 9 to the end of the current number on the
        calculator or if the number is 0 changes it to 9
        """
        if self.answer.text() == '0':
            self.answer.setText('9')
        else:
            self.answer.setText(self.answer.text() + '9')

    def calculate(self) -> None:
        """
        Takes all the numbers and operations saved in the calc object and
        computes the final result in the order the user entered them in
        """
        try:
            self.values[self.position] = int(self.answer.text())
            solve = self.values[0]
            counter = 0
            while counter <= self.position:
                if self.operations[counter] == 3 and self.values[counter - 1] == 0:
                    raise TypeError
                if self.operations[0] == -1:
                    raise RuntimeError
                if self.operations[counter] == 0:
                    solve += self.values[counter + 1]
                if self.operations[counter] == 1:
                    solve -= self.values[counter + 1]
                if self.operations[counter] == 2:
                    solve *= self.values[counter + 1]
                if self.operations[counter] == 3:
                    solve /= self.values[counter + 1]
                counter += 1
            if solve % 1 == 0:
                self.answer.setText(f'{solve:.0f}')
            else:
                self.answer.setText(f'{solve:.2f}')
            self.values = [solve]
            self.operations = [-1]
            self.position = 0
        except TypeError:
            self.answer.setHidden(True)
            self.label_error.setText('Divide By Zero Error\nPlease Hit Clear')
        except RuntimeError:
            self.answer.setHidden(True)
            self.label_error.setText('No Operation Error\nPlease Hit Clear')

    def redo(self) -> None:
        """
        Sets everything back to its starting state
        """
        self.values = [0]
        self.operations = [-1]
        self.position = 0

        self.answer.setHidden(False)
        self.answer.setText('0')
        self.label_error.setText('')

    def element(self) -> None:
        """
        Confirms the number and the operation the user wishes to have
        """
        self.values[self.position] = int(self.answer.text())
        self.values.append(0)
        self.operations.append(-1)
        self.position += 1

        self.answer.setText('0')

    def add(self) -> None:
        """
        Changes the current operation to addition
        """
        self.operations[self.position] = 0
        self.values[self.position] = int(self.answer.text())
        self.values.append(0)
        self.operations.append(-1)
        self.position += 1

        self.answer.setText('0')

    def subtract(self) -> None:
        """
        Changes the current operation to subtraction
        """
        self.operations[self.position] = 1
        self.values[self.position] = int(self.answer.text())
        self.values.append(0)
        self.operations.append(-1)
        self.position += 1

        self.answer.setText('0')

    def multiply(self) -> None:
        """
        Changes the current operation to multiplication
        """
        self.operations[self.position] = 2
        self.values[self.position] = int(self.answer.text())
        self.values.append(0)
        self.operations.append(-1)
        self.position += 1

        self.answer.setText('0')

    def divide(self) -> None:
        """
        Tells the calc to divide the last number by the next number the user
        enters and prepares the calc for the next number the user enter
        """
        self.operations[self.position] = 3
        self.values[self.position] = int(self.answer.text())
        self.values.append(0)
        self.operations.append(-1)
        self.position += 1

        self.answer.setText('0')
