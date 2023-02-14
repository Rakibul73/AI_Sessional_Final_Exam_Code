# quantifier: "there exists a unique ..."
# e.g. exactly_one( n*n == 9 for n in range(1,10) ) is True
def exactly_one(S):
	return len([ s for s in S if s ]) == 1
#

def in_order(L):
	return all( L[i] <= L[i+1] for i in range(0, len(L)-1) )
#

def set_to_predicate(S):
	return lambda x: x in S
#

def truth_table_rows(variables):
	if len(variables) == 0:
		return [dict()]
	variables = list(variables)
	P = variables[0]
	R = truth_table_rows(variables[1:])
	add_P = lambda v: [ dict([(P,v)] + list(r.items())) for r in R ]
	return add_P(True) + add_P(False)
#

def vars(*var_names):
        return ( Variable(name) for name in var_names )
#

def cast_to_proposition(p):
	if isinstance(p, Proposition):
		return p
	elif isinstance(p, str):
		return Variable(p)
	elif isinstance(p, bool):
		return Constant(p)
	else:
		raise ValueError()
#

class Proposition:
	symbol = ''
	empty_str = ''
	def __init__(self, *children):
		self.children = [ cast_to_proposition(c) for c in children ]
	def __str__(self):
		if len(self.children) == 0: return self.empty_str
		return self.symbol.join( c.child_str() for c in self.children )
	def evaluate(self, **assignments):
		raise NotImplementedError()
	def variables(self):
		if len(self.children) == 0:
			return frozenset()
		else:
			return frozenset.union(*[ c.variables() for c in self.children ])
	def __repr__(self):
		return 'Proposition( {0} )'.format(self)
	def child_str(self):
		return ('{0}' if isinstance(self, (Constant,Variable,Not)) else '({0})').format(self)
	def print_truth_table(self):
		vars = sorted( self.variables() )
		rows = truth_table_rows(vars)
		
		formula_header = str(self)
		formula_len = max(5,len(formula_header))
		header = '{0}  #  {1: ^{2}}'.format('  '.join('{0: ^5}'.format(v) for v in vars), formula_header, formula_len)
		print(header)
		print('#'*len(header))
		
		for r in rows:
			var_cols = '  '.join('{0: ^{1}}'.format(str(r[v]), max(5,len(v))) for v in vars)
			result_col = '{0: ^{1}}'.format(str(self.evaluate(**r)), formula_len)
			print('{0}  #  {1}'.format(var_cols, result_col)) 
		print()
	def to_tree(self):
		from trees import ListTree
		result = ListTree(value=str(self))
		for c in self.children:
			result.add_child_node(c.to_tree())
		return result
	def __and__(self,other):
		v = self.children if isinstance(self,And) else [self]
		w = other.children if isinstance(other,And) else [other]
		return And(*(v+w))
	def __rand__(self,other):
		return cast_to_proposition(other) & self
	def __or__(self,other):
		v = self.children if isinstance(self,Or) else [self]
		w = other.children if isinstance(other,Or) else [other]
		return Or(*(v+w))
	def __ror__(self,other):
		return cast_to_proposition(other) | self
	def __invert__(self):
		return Not(self)
	def __rshift__(self,other):
		return Implies(self,other)
	def __rrshift__(self,other):
		return Implies(other,self)
	def __lshift__(self,other):
		return ImpliedBy(self,other)
	def __rlshift__(self,other):
		return ImpliedBy(other,self)
	def disjunction(self,other):
		return self | other
	def conjunction(self,other):
		return self & other
	def negation(self):
		return ~self
	def implies(self,other):
		return self >> other
	def impliedby(self,other):
		return self << other
	def iff(self,other):
		return Iff(self,other)
	def is_tautology(self):
		return all( self.evaluate(**r) for r in truth_table_rows(self.variables()) )
	def is_contradiction(self):
		return all( not self.evaluate(**r) for r in truth_table_rows(self.variables()) )
	def is_contingency(self):
		return not self.is_tautology() and not self.is_contradiction()
	def __eq__(self,other):
		return self.is_equivalent(other)
	def is_equivalent(self,other):
		other = cast_to_proposition(other)
		return all( self.evaluate(**r) == other.evaluate(**r) for r in truth_table_rows(self.variables() | other.variables()) )
	def is_identical(self,other):
		return self.__class__ == other.__class__ \
			and len(self.children) == len(other.children) \
			and all( c.is_identical(d) for (c,d) in zip(self.children,other.children) )
	def substitute(self, e1, e2):
		if self.is_identical(e1):
			return e2
		else:
			return self.__class__( *[c.substitute(e1,e2) for c in self.children] )
#

class Constant(Proposition):
	def __init__(self,value):
		self.children = []
		self.value = bool(value)
	def substitute(self, e1, e2):
		return Constant(self.value)
	def __str__(self):
		return str(self.value)
	def evaluate(self, **assignments):
		return self.value
	def is_identical(self,other):
		return isinstance(other, Constant) and self.value == other.value
#

class Variable(Proposition):
	def __init__(self,name):
		self.children = []
		self.name = name
	def substitute(self, e1, e2):
		if self.is_identical(e1):
			return e2
		else:
			return Variable(self.name)
	def variables(self):
		return frozenset({ self.name })
	def __str__(self):
		return self.name
	def evaluate(self, **assignments):
		return assignments[self.name]
	def is_identical(self,other):
		return isinstance(other, Variable) and self.name == other.name
#

class Not(Proposition):
	def __init__(self,child):
		Proposition.__init__(self,child)
	def __str__(self):
		return u'Â¬{0}'.format(self.children[0].child_str()) 
	def evaluate(self, **assignments):
		return not self.children[0].evaluate(**assignments)
#

class And(Proposition):
	symbol = ' ^ '
	empty_str = 'True'
	def evaluate(self, **assignments):
		return all( child.evaluate(**assignments) for child in self.children )
#

class Or(Proposition):
	symbol = ' v '
	empty_str = 'False'
	def evaluate(self, **assignments):
		return any( child.evaluate(**assignments) for child in self.children )
#

class Implies(Proposition):
	symbol = ' => '
	def __init__(self,child1,child2):
		Proposition.__init__(self,child1,child2)
	def evaluate(self, **assignments):
		if self.children[0].evaluate(**assignments):
			return self.children[1].evaluate(**assignments)
		else:
			return True
#

class ImpliedBy(Proposition):
	symbol = ' <= '
	def __init__(self,child1,child2):
		Proposition.__init__(self,child1,child2)
	def evaluate(self, **assignments):
		if self.children[1].evaluate(**assignments):
			return self.children[0].evaluate(**assignments)
		else:
			return True
#

class Iff(Proposition):
	symbol = ' <=> '
	def __init__(self,child1,child2):
		Proposition.__init__(self,child1,child2)
	def evaluate(self, **assignments):
		return self.children[0].evaluate(**assignments) == self.children[1].evaluate(**assignments)
#

class ArgumentForm:
	def __init__(self, *premises, conclusion):
		self.premises = [ cast_to_proposition(c) for c in premises ]
		self.conclusion = cast_to_proposition(conclusion)
	def variables(self):
		return frozenset.union(self.conclusion.variables(), *[ c.variables() for c in self.premises ])
	def __repr__(self):
		return 'ArgumentForm( {0} )'.format(self)
	def __str__(self):
		return ((', '.join(str(c) for c in self.premises) + ', ') if self.premises else '') + 'conclusion = ' + str(self.conclusion)
	def print_truth_table(self):
		vars = sorted( self.variables() )
		rows = truth_table_rows(vars)
		
		var_strings = [ '{0: ^5}'.format(v) for v in vars ]
		premise_strings = [ '{0: ^6}'.format(str(c)) for c in self.premises ]
		conclusion_string = '{0: ^10}'.format(str(self.conclusion))
		vars_header = '  '.join(var_strings)
		premises_header = '{0: ^8}'.format('   '.join(premise_strings))
		print('{0}  #  {1: ^{2}}  #  {3: ^{4}}'.format(' '*len(vars_header), 'premises', len(premises_header), 'conclusion', len(conclusion_string)))
		header = '{0}  #  {1: ^8}  #  {2}'.format(vars_header, premises_header, conclusion_string)
		print(header)
		print('#'*len(header))
		
		for r in rows:
			premise_values = [ c.evaluate(**r) for c in self.premises ]
			conclusion_value = self.conclusion.evaluate(**r)
			star = '*' if all( v for v in premise_values ) else ''
			var_cols = '  '.join( '{0: ^{1}}'.format(str(r[v]), len(k)) for (k,v) in zip(var_strings, vars) )
			premise_cols = '   '.join( '{0: ^{1}}'.format(str(v)+star, len(k)) for (k,v) in zip(premise_strings, premise_values) )
			conclusion_col = '{0: ^{1}}'.format(str(conclusion_value)+star, len(conclusion_string))
			print('{0}  #  {1: ^8}  #  {2}'.format(var_cols, premise_cols, conclusion_col))
		print()
	def is_valid(self):
		vars = (frozenset.union(*[ c.variables() for c in self.premises ]) if self.premises else frozenset()) | self.conclusion.variables()
		return all( self.conclusion.evaluate(**r) for r in truth_table_rows(vars) if all( c.evaluate(**r) for c in self.premises ) )
	def substitute(self, e1, e2):
		return ArgumentForm( *[ c.substitute(e1,e2) for c in self.premises ], conclusion = self.conclusion.substitute(e1,e2) )
#