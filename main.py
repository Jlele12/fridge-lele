"""Notes From a Passive-Aggressive Fridge

Entry for make.fun competition u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.
The deliverable is one line, under 200 characters: a note a passive-aggressive
fridge leaves its owner. The note never names a date outright, forgives before
being asked, and weaponizes politeness, so the fridge's quiet disappointment is
the joke and the owner is left to figure out what they did.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
"""
import os
from pathlib import Path

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)

EMOJI = ("It's completely fine that the March yogurt is now a roommate. I keep things cold in here. As a fridge. That is the entire job, and I am doing it.")

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
