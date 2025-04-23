from cmd import Cmd

from src.moolean import Calculator



# Moolean Shell
class MooleanShell(Cmd):
	prompt = "moolean>"
	intro = "Moolean Calculator Shell (type 'help' for commands)"
	calc:Calculator

	def __init__(self):
		super().__init__()
		self.calc = Calculator()
		self.history = []

	def default(self,expr): #type:ignore
		"""Evaluate an expression: eval 1+2*3"""
		try:
			result = self.calc.calculate(expr)
			print(result)
			self.history.append(expr)
		except Exception as e:
			print(f"Error: {e}")
	def do_exit(self,_):
		print("Exiting Moolean ... Bye!")
		return True


if __name__ == "__main__":
	MooleanShell().cmdloop()
