"""Module sample_bot provides the "Samplebot" class, which implements
the clue AI interface
"""
from random import choice, randint
from typing import Union, Optional
from clue_game import *


class SampleBort(PlayerInterface):
    """A sample implementation of the player interface"""

    def __init__(self) -> None:
        self.player_id = None
        self.num_players = None
        self.face_up_cards = None
        self.face_down_cards = None

        self.known_cards = None
        self.solution = None

    def initialize(self,
                   player_id: int,
                   num_players: int,
                   face_up_cards: list[Card],
                   face_down_cards: list[Card]) -> None:
        self.player_id = player_id
        self.num_players = num_players
        self.face_up_cards = face_up_cards
        self.face_down_cards = face_down_cards

        self.known_cards = []
        self.solution = None

        for card in face_down_cards:
            self.known_cards.append(card)

        for card in face_up_cards:
            self.known_cards.append(card)

    def name(self) -> str:
        return "sample_bort"

    def possibleCards(self, cardSet):
        possibleCards = []

        for card in list(cardSet):
            if card not in self.known_cards:
                possibleCards.append(card)

        return possibleCards


    def take_turn(self) -> Union[Suggestion, Accusation]:

        if self.solution is not None:
            return Accusation(self.solution.who, self.solution.where, self.solution.what)

        who = choice(self.possibleCards(Suspect))
        where = choice(self.possibleCards(Location))
        what = choice(self.possibleCards(Weapon))

        if len(self.known_cards) >= 18:
            return Accusation(who, where, what)
        else:
            return Suggestion(who, where, what)

    def respond_to_suggestion(self,
                              suggestor_id: int,
                              suggestion: Suggestion) -> Optional[Card]:
        if(suggestion.who in self.face_down_cards):
            return suggestion.who
        elif(suggestion.where in self.face_down_cards):
            return suggestion.where
        elif(suggestion.what in self.face_down_cards):
            return suggestion.what
        else:
            return None

    def receive_suggestion_result(self,
                                  suggestion: Suggestion,
                                  result: Optional[Counterevidence]) -> None:
        if result is None:
            self.solution = suggestion
        else:
            self.known_cards.append(result.evidence)

    def observe_suggestion(self,
                           suggestor_id: int,
                           suggestion: Suggestion,
                           blocker_id: Optional[int]) -> None:
        if blocker_id is None:
            self.solution = suggestion

    def observe_accusation(self,
                           accusor_id: int,
                           accusation: Accusation) -> None:
        pass
