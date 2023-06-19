from abc import ABC, abstractmethod
import unittest

# expression is an abstract class
class Expression(ABC):
   def accept(self, visitor):
    pass
    
class Visitor():
    def visit_binary_expression(self, expression):
        return self.parenthesize(expression.operator, [expression.left, expression.right])

    def visit_grouping_expression(self, expression):
        return self.parenthesize("group", [expression.expression])

    def visit_literal_expression(self, expression):
        return str(expression.value)

    def parenthesize(self, name, expressions):
        final_expression = "(" + name
        for expression in expressions:
            final_expression += " " + expression.accept(self)
        final_expression += ")"
        
        return final_expression
    
class Binary(Expression):
    def __init__(self, left, operator, right):
        self.left = left 
        self.right = right
        self.operator = operator

    def accept(self, visitor):
        return visitor.visit_binary_expression(self)

    
class Grouping(Expression):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_grouping_expression(self)

    
class Unary(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_unary_expression(self)
        
class Literal(Expression):
  """
  @note literal is either a string or a number
  value: string or number
  """
  def __init__(self, value):
        self.value = value
    
  def accept(self, visitor):
        return visitor.visit_literal_expression(self)
        

class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.visitor = Visitor()

    def test_visit_binary_expression(self):
        # Test with literal expressions
        expr = Binary(Literal(1), '+', Literal(2))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(+ 1 2)')

        # Test with nested binary expressions
        expr = Binary(Binary(Literal(1), '+', Literal(2)), '*', Literal(3))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(* (+ 1 2) 3)')

    def test_visit_grouping_expression(self):
        expr = Grouping(Binary(Literal(1), '+', Literal(2)))
        result = expr.accept(self.visitor)
        self.assertEqual(result, '(group (+ 1 2))')

    def test_visit_literal_expression(self):
        expr = Literal(5)
        result = expr.accept(self.visitor)
        self.assertEqual(result, '5')

if __name__ == '__main__':
    unittest.main()