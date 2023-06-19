from abc import ABC, abstractmethod

# expression is an abstract class
class Expression(ABC):
   def accept(self, visitor):
    pass
    
class Visitor():
  def visit_binary_expression(self, expression):
    self.parenthesize(expression.operator.lexeme, [expression.left, expression.right])

  def visit_grouping_expression(self, expression):
    pass  
  def visit_literal_expression(self, expression):
    pass
  def visit_unary_expression(self, expression):
    return (expression.operator, expression.expression.accept(self))
  
  def visit_assignment_expression(self, expression):
    pass
    
  # generate the AST from an expression
  def parenthesize(self, lexeme, expressions):
    # this would also take care of precedence of operators
    # 1. it wraps the lexeme in parenthesis
    # 2. it checks if the expression is a binary expression
    # 3. if it is, it calls the parenthesize function on the left and right expressions
    # 4. if it is not, it returns the expression
    # 5. it returns the result of the parenthesize function
    final_expression = ""
    final_expression.append("(")
    final_expression.append(lexeme)
    for expression in expressions:
      final_expression.append(expression.accept(self))
    final_expression.append(")")
    
    return final_expression
    
        
    
    

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

  def accept(self, visitor):
    visitor.visit_binary_expression(self)
    
class Grouping(Expression):
  def __init__(self,left_paren, expression, right_paren):
    self.left_paren = left_paren
    self.expression = expression
    self.right_paren = right_paren

  def accept(self, visitor):
    visitor.visit_grouping_expression(self)
    
class Unary(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def accept(self, visitor):
        visitor.visit_unary_expression(self)
        
class Literal(Expression):
  """
  @note literal is either a string or a number
  value: string or number
  """
  def __init__(self, value):
        self.value = value
    
  def accept(self, visitor):
        visitor.visit_literal_expression(self)