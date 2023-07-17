male = {"type":"Male", "weight":None}
female = {"type":"Female", "weight":None}
child = {"type":"Child", "weight":None}


def pax_C208(males,females,children):
	pax = []

	for _ in range(males):
		pax.append(male)

	for _ in range(females):
		pax.append(female)

	for _ in range(children):
		pax.append(child)

	return pax

# print(pax_C208(2,2,2))
