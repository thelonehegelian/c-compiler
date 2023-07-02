from abc import ABC, abstractmethod

# @todo operation precedence is not implemented yet

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
        