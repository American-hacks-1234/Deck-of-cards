#!/usr/bin/env python3
"""
Digital Python Deck of CARDS — V1.05

Controls:
 - Enter = draw a card (can't draw the same card again until you reshuffle)
 - r     = reshuffle the deck (puts all drawn cards back and shuffles)
 - q     = quit
"""
import random
import sys
from typing import List, Optional

RANK_NAMES = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]


class Card:
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def name(self) -> str:
        return RANK_NAMES.get(self.rank, str(self.rank))

    def __str__(self) -> str:
        return f"{self.name()} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card({self.rank!r}, {self.suit!r})"


class Deck:
    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        self._build_deck()

    def _build_deck(self) -> None:
        if self.seed is not None:
            random.seed(self.seed)
        # Create full 52-card deck
        self._all_cards: List[Card] = [Card(rank, suit) for rank in range(1, 14) for suit in SUITS]
        self.reset()

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw(self) -> Optional[Card]:
        """Draw one card. Once drawn it is removed and cannot be drawn again until reset()."""
        if not self._cards:
            return None
        card = self._cards.pop()
        self._drawn.append(card)
        return card

    def remaining(self) -> int:
        return len(self._cards)

    def drawn_count(self) -> int:
        return len(self._drawn)

    def reset(self) -> None:
        """Return all cards to the deck and shuffle."""
        # Copy all_cards so reset always restores full deck
        self._cards = list(self._all_cards)
        self._drawn: List[Card] = []
        self.shuffle()


def main() -> None:
    seed = None
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
        except ValueError:
            pass

    deck = Deck(seed=seed)
    print("welcome to the digital python deck of CARDS V1.05")
    print("controls: Enter = draw, r = reshuffle, q = quit")
    print("You cannot draw the same card again until you reshuffle.")

    while True:
        if deck.remaining() == 0:
            print("Deck is empty. Press 'r' to reshuffle or 'q' to quit.")
        else:
            print(f"Cards remaining: {deck.remaining()}  (drawn: {deck.drawn_count()})")

        user = input().strip().lower()

        if user == "q":
            print("Goodbye.")
            break

        if user == "r":
            deck.reset()
            print("Deck reshuffled.")
            continue

        # Treat Enter (empty input) as draw
        if user == "":
            card = deck.draw()
            if card:
                print(f"You drew the {card}")
            else:
                print("No cards to draw. Press 'r' to reshuffle or 'q' to quit.")
            continue

        # Unknown command
        print("Unknown command. Use Enter to draw, 'r' to reshuffle, 'q' to quit.")


if __name__ == "__main__":
    main()
