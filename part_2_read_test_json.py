import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    
    json_lib = json_data['game_library']
    
    for json_game in json_lib:
        platform = test_data.Platform(json_game['platform']['name'], json_game['platform']['launch_year'])
        game = test_data.Game(json_game['title'], platform, json_game['year'])
        game_library.add_game(game)

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###

with open(input_json_file) as json_file:
    data = json.load(json_file)
    game_library = make_game_library_from_json(data)
    print(game_library)