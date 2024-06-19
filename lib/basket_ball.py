def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },

        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


game = game_dict()


# get players
def get_all_players(game):
    players = []
    for team in game.values():
       # team => home and away
        for player in team["players"]:
            players.append(player)
    return players



def num_points_per_game(player_name):
    all_players = get_all_players(game)
    points_per_game = [player["points_per_game"]
                       for player in all_players if player_name.lower() == player["name"].lower()]
    return points_per_game[0] if points_per_game else None


print(num_points_per_game("Kevin Love"))
print(num_points_per_game("Kyle Kuzma"))


def player_age(player_name):
    # knows the age of each player
    # takes player's name as argument
    # returns that player's age
    all_players = get_all_players(game)
    age_per_player = [player["age"]
                      for player in all_players if player_name.lower() == player["name"].lower()]
    return age_per_player[0] if age_per_player else None


print(player_age("Jarrett Allen"))


def team_colors(team_name):
    # takes team name as argument
    # returns a list of that team's colors
    team_colors_all = [team["colors"] for team in game.values(
    ) if team_name.lower() == team["team_name"].lower()]
    return team_colors_all[0] if team_colors_all else None


print(team_colors("Cleveland Cavaliers"))  # ["Wine", "Gold"]


def team_names():
    # returns a list of the team names
    return [team["team_name"] for team in game.values()]


print(team_names())


def player_numbers(team_name):
    # Takes in team name as argument, returns a list of the jersey numbers for that team
    for team in game.values():  # Iterate through the teams in the game dictionary
        # Check if team_name matches (case insensitive)
        if team["team_name"].lower() == team_name.lower():
            # Extract jersey numbers of players
            return [player["number"] for player in team["players"]]

    # If no team with matching team_name is found, return an empty list or handle as needed
    return []


print(player_numbers('Cleveland Cavaliers'))


def player_stats(player_name):
    # returns all stats for a given player
    # player's name is the arg => returns a dict of player's stats
    all_players = get_all_players(game)
    for player in all_players:
        if player["name"].lower() == player_name.lower():
            return player

# If player_name is not found, return None
    return None


# print(get_all_players(game))
# print(player_stats("Jarrett Allen"))


def average_rebounds_by_shoe_brand():
    # return average number of rebounds for players who wear a particular shoe brand
    # average is a float w 2 decimals

    all_players = get_all_players(game)
    shoe_brand_rebounds = {}
    for player in all_players:
        # {"Nike" : [5.0, 8.1, 4.7]}
        # add shoe brands and rebounds in a list.
        if player["shoe_brand"] not in shoe_brand_rebounds:
            shoe_brand_rebounds[player["shoe_brand"]] = [
                player["rebounds_per_game"]]
        else:
            shoe_brand_rebounds[player["shoe_brand"]].append(
                player["rebounds_per_game"])

    # average rebounds per shoe brand
    for shoe_brand, rebounds in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds) / len(rebounds)
        shoe_brand_rebounds[shoe_brand] = "{:.2f}".format(
            average_rebounds)  # 2 decimal points

    for brand, average in shoe_brand_rebounds.items():
        print(f"{brand}:  {average}")


print(average_rebounds_by_shoe_brand())


# Which player has the most career points?

#iterate over the dictionary to compare career points, return the maximum

def get_max_point():
    all_players = get_all_players(game)
    max_player = max(all_players, key=lambda player: player["career_points"])
    return max_player["name"]

print(get_max_point())  # Kevin Love

# Are there any jersey numbers that are worn by players on both teams?

#iterate through the players to find numbers that are used more than once
# check both teams for same numbers if any exists
# if exists , return the number
# else, return no matching number found

def jersey_numbers():
    all_players = get_all_players(game)
    jersey_numbers = []
    for player in all_players:
        if player["number"] not in jersey_numbers:
            jersey_numbers.append(player["number"])

    for number in jersey_numbers:
        if jersey_numbers.count(number) > 1:
            return number
        else:
            return "No matching number found"

print(jersey_numbers())


# Which player has the longest name?

def find_longest_name():
    all_players = get_all_players(game)
    longest_name = max(all_players, key=lambda player: len(player["name"]))
    return longest_name["name"]

print(find_longest_name())  # Kentavious Caldwell-Pope