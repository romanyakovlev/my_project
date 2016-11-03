def test0():
	
	def mpl():
		return [lambda x: i * x for i in range(3)]

print([m(4) for m in mpl()])
