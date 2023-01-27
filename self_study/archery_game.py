import secrets


def generate_score():
    return secrets.randbelow(11)


def print_scores(scores):
    print("Player\tChance 1\tChance 2\tChance 3       Total")
    for i in range(4):
        print(f"{i + 1}\t\t\t{scores[i][0]}\t\t\t{scores[i][1]}\t\t\t{scores[i][2]}\t\t\t{sum(scores[i])}")


def main():
    scores = [[generate_score() for j in range(3)] for i in range(4)]
    print_scores(scores)

    winner = max(range(4), key=lambda i: sum(scores[i]))
    print()
    print(f"Player {winner + 1} wins with a total score of {sum(scores[winner])}.")


if __name__ == '__main__':
    main()
