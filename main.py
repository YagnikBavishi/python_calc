import sys
from  model import evaluateExpression
from controller import Controller
from PyQt5.QtWidgets import QApplication
from view import GUI
# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)


    # Show the calculator's GUI
    view = GUI()
    view.show()

    model = evaluateExpression
    Controller(model=model, view=view)
    sys.exit(pycalc.exec_())



if __name__ == '__main__':
    main()
