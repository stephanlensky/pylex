"""Deterministic finite automaton class."""

from pylex.automaton import Automaton, AutomatonState


class DFA(Automaton):
    """
    A deterministic finite automaton. Each state has only a single transition
    for each symbol and epsilon transitions are not allowed.

    """

    def __init__(self, initial):
        super().__init__(initial)

class DFAState(AutomatonState):
    """
    A state in a deterministic finite automaton.

    Attributes:
    transitions -- A set of outgoing transitions from this state represented as
    a dictionary from characters to another state.
    
    """

    def __init__(self, accepting=None):
        super().__init__(accepting)

    def add_transition(self, symbol, to):
        """Add a transition to this state. 

        Arguments:
        symbol -- The symbol on which to take the transition; must not already
        be in the keys of transitions and must not be None.
        to -- The state to transition to on the given symbol.

        >>> state1 = DFAState()
        >>> state2 = DFAState()
        >>> state1.add_transition('a', state2)
        >>> state1.add_transition('b', state1)
        >>> len(state1.transitions)
        2
        >>> state1.add_transition(None, state2)
        Traceback (most recent call last):
            ...
        AssertionError: DFA cannot contain epsilon transitions
        >>> state1.add_transition('a', state2)
        Traceback (most recent call last):
            ...
        AssertionError: state already contains given transition
        """

        assert symbol is not None, 'DFA cannot contain epsilon transitions'
        assert symbol not in self.transitions, 'state already contains given transition'
        self.transitions[symbol] = to