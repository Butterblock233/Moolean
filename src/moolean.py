from pyparsing import (
	Combine,
	Group,
	Literal,
	ParseResults,
	Word,
	alphas,
	infix_notation,
	nums,
	oneOf,
	opAssoc,
	OpAssoc
)


class Calculator:
	_number = Word(nums + ".").setParseAction(lambda t: float(t[0])) #type:ignore
	_operator = oneOf("+ - * /")
	_grammar = infix_notation(
		_number,
		[
			(oneOf("* /"), 2, OpAssoc.LEFT),
			(oneOf("+ -"), 2, OpAssoc.LEFT),
		],
		lpar="(", rpar=")",
	)
	expression:str

	def __init__(self,expression_str:str = "") -> None:
		self.expression = expression_str
	
	def _apply_operator(self,operator:str,left:float,right:float)->float:
		match operator:
			case "+":
				return left + right

			case "-":
				return left - right

			case "*":
				return left * right

			case "/":
				if right != 0:
					return left / right
				else:
					raise ZeroDivisionError("Numbers cannot be devided by 0")
			case _:
				raise ValueError(f"Invalid operator {operator}",operator)
	def _evaluate(self,node:ParseResults|list|float)->float:
		"""
		- 如果是数字，立刻返回: _evaluate(3) -> 3
		- 如果是表达式，递归求值: 
		  _evaluate([3, '*', 5]) -> 
		  [_evaluate(3), '*', _evaluate(5)] ->
		  [3 , '*', 5] ->
		  _apply_operator([3 , '*', 5]) -> 15
		"""
		if isinstance(node,(float,int)):
			return float(node) #数字返回自身
		else:
			if len(node) == 1:
				return self._evaluate(node[0]) # 
			
			if len(node) == 3:
				left = self._evaluate(node[0])
				operator = node[1]
				right = self._evaluate(node[2])
				if isinstance(operator, str) and operator in {"+", "-", "*", "/"}:
					return self._apply_operator(operator, left, right)
				raise ValueError(f"Invalid operator {operator}")

		
			else:
				# 将表达式分组为二元操作，例如 1+1+1 -> (1+1)+1
				left = self._evaluate(node[0])
				operator = node[1]
				right = self._evaluate(node[2:])
				if isinstance(operator, str) and operator in {"+", "-", "*", "/"}:
					return self._apply_operator(operator, left, right)
				raise ValueError(f"Invalid operator {operator}")
	def calculate(self,expression:str = ""):
		expression_to_parse = expression if expression else self.expression
		try:
			parsed = self._grammar.parse_string(expression_to_parse,parse_all=True)
		except Exception as e:
			print(e)
		return self._evaluate(parsed)


# Test:

if __name__ == "__main__":
	calc = Calculator("12+1+1")
	result = calc.calculate("1+1+1")
	print(f"Expression: {calc.expression}",f"Result:{result}",sep="\n")
