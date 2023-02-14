from logic import *

P,Q,R,S = vars('P', 'Q', 'R', 'S')

# valid argument forms
modus_ponens = ArgumentForm(
	P, P >> Q,
	conclusion = Q
)
modus_tollens = ArgumentForm(
	P >> Q, ~Q,
	conclusion = ~P
)
disjunctive_syllogism = ArgumentForm(
	P | Q, ~P,
	conclusion = Q
)
hypothetical_syllogism = ArgumentForm(
	P >> Q, Q >> R,
	conclusion = R
)
dilemma = ArgumentForm(
	P | Q, P >> R, Q >> S,
	conclusion = R | S
)
explosion_principle = ArgumentForm(
	False,
	conclusion = P
)
tautology_from_no_premises = ArgumentForm(
	conclusion = True
)

# invalid argument forms
non_sequitur = ArgumentForm(
	P,
	conclusion = Q
)
affirming_the_consequent = ArgumentForm(
	P >> Q, Q,
	conclusion = P
)
denying_the_antecedent = ArgumentForm(
	P >> Q, ~P,
	conclusion = ~Q
)
fallacy_of_the_excluded_middle = ArgumentForm(
	P | Q, P,
	conclusion = ~Q
)
contingency_from_no_premises = ArgumentForm(
	conclusion = P
)