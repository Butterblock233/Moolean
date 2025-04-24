from cmd import Cmd

from src.moolean import Calculator


# Moolean Shell
class MooleanShell(Cmd):
    prompt = "moolean>"
    intro = "Moolean Calculator Shell (type 'help' for commands)"
    calc: Calculator

    def __init__(self):
        super().__init__()
        self.calc = Calculator()
        self.history = []

    def default(self, line):
        """Evaluate an expression: eval 1+2*3"""
        try:
            result = self.calc.calculate(line)
            print(result)
            self.history.append(line)
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self, _):
        print("Exiting Moolean ... Bye!")
        return True

    def do_history(self, _):
        for i, line in enumerate(self.history):
            print(f"{i+1}. {line}")


def main():
    MooleanShell().cmdloop()


if __name__ == "__main__":
    main()
