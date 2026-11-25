"""Fortune cookie for the liquidated trader — make.fun entry program.

Writes the one-line fortune to /output/entry.txt.
"""
# Design notes — why this line should win:
# It keeps the small oracular fortune voice, then breaks it on a double
# meaning: the moon the trader chases (the pump) is the same moon they
# keep missing (the sky). Rueful and warm, never cruel — the cookie
# comforts the trader by telling them the moon was never theirs to catch.

ENTRY = "You will lose every coin you chase. But the moon you keep missing was never yours to catch, dear trader."

MAX_CHARS = 160
MAX_WORDS = 20

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
