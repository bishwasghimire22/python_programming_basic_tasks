# Create a program called tuples_argument.
# The program should have a function named print_player  that takes a tuple as argument.
# The tuple should contain a team name, player name and the number of the goals the player has scored.
# Finally, the print_player function should print these values.

# First, copy/paste the main function below to your program. Then write the print_player  function.


def print_player(player_tuple):
    # print(f"{player_tuple[1]} ({player_tuple[0]}), {player_tuple[2]} goals")

    team, player, goals = player_tuple
    print(f"{player} ({team}), {goals} goals")


def main():
    p = ("Hawks", "Jennifer", 10)
    print_player(p)


main()
