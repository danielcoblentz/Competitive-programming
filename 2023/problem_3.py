def declare_winner(game: list) -> None:
    scores = {}  # Scores stored in a dictionary
    winner = None

    for throw in game:
        points, player = throw

        if player == "GROUND":
            # Ignore the ball landing on the ground
            continue

        if player not in scores:
            # Add player to scores if they are not already in
            scores[player] = 0

        if points == "JACKPOT":
            # Award instantaneous win for jackpot
            print(f"The winner is {player}.")
            return
        elif points == "BANKRUPT":
            scores[player] = 0
        else:
            # We have ruled out the "GROUND" and both "JACKPOT" and
            # "BANKRUPT" - meaning that a player caught the ball and
            # the ball had an integer point value
            scores[player] += int(points)

        for p, s in scores.items():
            # If a player has 500 or more points, they win
            if s >= 500:
                winner = p
                break

        if winner is not None:
            # Declare winner, if one exists
            print(f"The winner is {winner}.")
            return

    # Game ended with no winner
    print("There is no winner.")


if __name__ == "__main__":
    games: list[list[tuple[str, str]]] = []
    game_index = 0

    # Take input
    while True:
        # Get the number of throws in the game
        n = int(input())

        # When n == 0, input is over
        if n == 0:
            break

        game = []
        for i in range(n):
            # Take input, turn it into a tuple of the form:
            # (pts, player)
            next_throw = input()
            next_throw_list = next_throw.split()
            next_throw_tuple = (next_throw_list[0], next_throw_list[1])
            game.append(next_throw_tuple)

        games.append(game)  # Add throw to game

    # Iterate through all games
    for game in games:
        declare_winner(game)
