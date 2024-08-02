class Calculator:
    def get_result(self, tokens):
        if not self.validate_expression(tokens):
            return "wrong equation"

        values, operators = [], []
        i = 0

        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):  # Handle negative numbers
                values.append(float(token))
            elif token == "(":
                balance, j = 1, i
                while balance:
                    i += 1
                    balance += tokens[i] == "("
                    balance -= tokens[i] == ")"
                values.append(self.get_result(tokens[j + 1 : i]))
            elif token in "+-*/":
                while (operators and operators[-1] in "*/" and token in "+-") or (operators and operators[-1] in "*/"):
                    values.append(self.apply_operator(operators.pop(), values.pop(-2), values.pop()))
                operators.append(token)
            i += 1

        while operators:
            values.append(self.apply_operator(operators.pop(), values.pop(-2), values.pop()))

        return values[0]

    def validate_expression(self, tokens):
        for i in range(len(tokens) - 1):
            if tokens[i] in "+-*/" and tokens[i + 1] in "+-*/":
                return False
        return True

    def apply_operator(self, operator, a, b):
        return {"+": a + b, "-": a - b, "*": a * b, "/": a / b}[operator]


calculator = Calculator()
tokens = ["11", "+", "-", "*", "2", "+", "(", "2", "+", "3", ")", "+", "2"]
result = calculator.get_result(tokens)
print(result)

tokens = ["11", "+", "2", "*", "2", "+", "(", "2", "+", "3", ")", "+", "2"]
result = calculator.get_result(tokens)
print(result)
