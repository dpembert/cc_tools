import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    games = json_data["games"]
    
    ### Begin Add Code Here ###
    #Loop through the json_data
    for game in games:
        #Create a new Game object from the json_data by reading
        new_game = test_data.Game()
        #  title
        title = json_data["title"]
        #  year
        year = json_data["year"]
        #  platform (which requires reading name and launch_year)
        platforminfo = json_data["platform"]
        for platform in platforminfo:
            new_platform = test_data.Platform(platform["name"],platform["launch_year"])
            new_game.add_platform(new_platform)
        #Add that Game object to the game_library
        game_library.add_game(new_game)    
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    #Use the json module to load the data from the file
    game_library_json_data = json.load(reader)

#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data

GameLibrary = make_game_library_from_json(game_library_json_data)

#Print out the resulting GameLibrary data using print()
print(GameLibrary)
### End Add Code Here ###
