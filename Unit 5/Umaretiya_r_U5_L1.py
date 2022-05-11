from pomegranate import *

# Pop Quiz

# Graduated (G) Node
Graduated = DiscreteDistribution({'graduated':0.9, 'no-graduated':0.1})

# Offer Child Nodes
Offer1 = ConditionalProbabilityTable([
['graduated', 'offer', 0.5],
['graduated', 'no-offer', 0.5],
['no-graduated', 'offer', 0.05],
['no-graduated', 'no-offer', 0.95]], [Graduated])

Offer2 = ConditionalProbabilityTable([
['graduated', 'offer', 0.75],
['graduated', 'no-offer', 0.25],
['no-graduated', 'offer', 0.25],
['no-graduated', 'no-offer', 0.75]], [Graduated])

# Setting up states for each node
s_graduated = State(Graduated, 'graduated-offer')
s_offer_1 = State(Offer1, 'offer_1')
s_offer_2 = State(Offer2, 'offer_2')

# Creating Bayesian Network
model = BayesianNetwork('graduated-offer')

# Adding nodes to network
model.add_states(s_graduated, s_offer_1, s_offer_2)

# Creating edges
model.add_transition(s_graduated, s_offer_1)
model.add_transition(s_graduated, s_offer_2)

model.bake() # finalize the topology of the model

print()
print('Pop Quiz:')
print('The number of nodes:', model.node_count())
print('The number of edges:', model.edge_count())

# predict_proba(Given factors)
# P(o2 | g, ~o1)
print('P(o2 | g, ~o1): ', model.predict_proba({'graduated-offer': 'graduated', 'offer_1': 'no-offer'})[2].parameters[0]['offer'])

# predict_proba(Given factors)
# P(g | o1, o2)
print('P(g | o1, o2): ', model.predict_proba({'offer_1': 'offer', 'offer_2': 'offer'})[0].parameters[0]['graduated'])

# predict_proba(Given factors)
# P(g | ~o1, o2)
print('P(g | ~o1, o2): ', model.predict_proba({'offer_1': 'no-offer', 'offer_2': 'offer'})[0].parameters[0]['graduated'])

# predict_proba(Given factors)
# P(g | ~o1, ~o2)
print('P(g | ~o1, ~o2): ', model.predict_proba({'offer_1': 'no-offer', 'offer_2': 'no-offer'})[0].parameters[0]['graduated'])

# predict_proba(Given factors)
# P(o2 | o1)
print('P(o2 | o1): ', model.predict_proba({'offer_1': 'offer'})[2].parameters[0]['offer'])

# Example 5, Day 2 Note

# Happiness Factors
Sunny = DiscreteDistribution({'sunny':0.7, 'not-sunny':0.3})
Raise = DiscreteDistribution({'raise': 0.01, 'no-raise': 0.99})

# Happiness Conditional Probability
Happiness = ConditionalProbabilityTable([
['sunny', 'raise', 'happy', 1],
['sunny', 'raise', 'not-happy', 0],
['sunny', 'no-raise', 'happy', 0.7],
['sunny', 'no-raise', 'not-happy', 0.3],
['not-sunny', 'raise', 'happy', 0.9],
['not-sunny', 'raise', 'not-happy', 0.1],
['not-sunny', 'no-raise', 'happy', 0.1],
['not-sunny', 'no-raise', 'not-happy', 0.9]], [Sunny, Raise])

# Setting up states for each node
s_sunny = State(Sunny, 'is-sunny')
s_raise = State(Raise, 'got-raise')
s_happiness = State(Happiness, 'happiness')

# Creating Bayesian Network
model = BayesianNetwork('happiness-network')

# Adding nodes to network
model.add_states(s_sunny, s_raise, s_happiness)

# Creating edges
model.add_transition(s_sunny, s_happiness)
model.add_transition(s_raise, s_happiness)

model.bake() # finalize the topology of the model

print()
print('Day 2 Note, Example 3:')
print('The number of nodes:', model.node_count())
print('The number of edges:', model.edge_count())

# predict_proba(Given factors)
# P(r | s)
print('P(r | s): ', model.predict_proba({'is-sunny': 'sunny'})[1].parameters[0]['raise'])

# predict_proba(Given factors)
# P(r | h, s)
print('P(r | h, s): ', model.predict_proba({'is-sunny': 'sunny', 'happiness': 'happy'})[1].parameters[0]['raise'])

# predict_proba(Given factors)
# P(r | h)
print('P(r | h): ', model.predict_proba({'happiness': 'happy'})[1].parameters[0]['raise'])

# predict_proba(Given factors)
# P(r | h, ~s)
print('P(r | h, ~s): ', model.predict_proba({'is-sunny': 'not-sunny', 'happiness': 'happy'})[1].parameters[0]['raise'])