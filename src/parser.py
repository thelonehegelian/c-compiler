from abc import ABC, abstractmethod

# expression is an abstract class
class Expression(ABC):
  pass
    
class Visitor():
  def visit_binary_expression(self, expression):
    pass
  def visit_grouping_expression(self, expression):
    pass
  def visit_literal_expression(self, expression):
    pass
  def visit_unary_expression(self, expression):
    pass
  def visit_assignment_expression(self, expression):
    pass

class Binary(Expression):
  """
  left: Expression
  right: Expression
  operator: Token
  """
  def __init__(self, left, operator, right):
    self.left = left 
    self.right = right
    self.operator = operator

class Grouping(Expression):
  def __init__(self,left_paren, expression, right_paren):
    self.left_paren = left_paren
    self.expression = expression
    self.right_paren = right_paren


class Unary(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression


class Literal(Expression):
  """
  @note literal is either a string or a number
  value: string or number
  """
  def __init__(self, value):
        self.value = value
    
