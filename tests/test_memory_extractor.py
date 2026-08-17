"""
Test automatic memory extraction.
"""

from memory.extractor import MemoryExtractor


def main() -> None:
    extractor = MemoryExtractor()

    test_messages = [
        "My name is Naveen.",
        "My favorite programming language is Python.",
        "I am building AURA AI.",
        "I prefer VS Code.",
        "What is Python?",
        "Hello Aura!",
    ]

    print()
    print("=" * 60)
    print("MEMORY EXTRACTION TEST")
    print("=" * 60)

    for message in test_messages:
        candidates = extractor.extract(
            message
        )

        print()
        print(f"Message: {message}")

        if not candidates:
            print("  → No memory detected.")
            continue

        for candidate in candidates:
            print(
                f"  → {candidate.content}"
            )
            print(
                f"    Type: {candidate.memory_type}"
            )
            print(
                f"    Importance: "
                f"{candidate.importance}"
            )


if __name__ == "__main__":
    main()