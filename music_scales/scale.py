"""Module for representing a musical scale"""

from typing import List, Tuple

from .constants import DEGREES, NOTES
from .note import Note


class Scale:
    """A musical scale"""

    interval_to_steps = {
        'h': 1,
        'w': 2,
        'w+h': 3,
        '3h': 3,
    }

    def __init__(self, name: str, intervals: str, mode: str = None):
        """
        Args:
            name: name of the scale e.g. minor pentatonic
            intervals: scale intervals as 'w h' etc
            mode: name of the mode associated with the scale
        """

        self.name = name
        self.intervals = intervals.split()
        self.mode = mode

    def in_key(self, key: str) -> List[Note]:
        """Generates the notes for the scale in the specified key

        Args:
            key: the key of the scale to generate e.g. 'c' or 'd'
        """
        return [step[0] for step in self.with_degrees(key)]

    def with_degrees(self, key: str) -> List[Tuple[Note, str]]:
        """Generate notes of scale and include degrees e.g. 'major third'

        Args:
            key: the key of the scale to generate e.g. 'c' or 'd'
        """
        if key not in NOTES:
            raise ValueError(f'"{key}" is not a valid key')

        notes_idx = NOTES.index(Note(key))
        intervals_idx = 0

        key_notes = []

        for step in self.intervals:
            key_notes.append((NOTES[notes_idx], DEGREES[intervals_idx]))

            if step not in self.interval_to_steps:
                raise ValueError(f'Incorrect value "{step}" for scale interval')

            next_step = self.interval_to_steps[step]
            notes_idx += next_step
            intervals_idx += next_step

            notes_idx = notes_idx % len(NOTES)

        return key_notes
