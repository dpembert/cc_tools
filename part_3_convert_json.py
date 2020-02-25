import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
input_json_file = "data/dpembert_ccl.json"

##Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    ##Use the json module to load the data from the file
    level_pack_json_data = json.load(reader)

#print(level_pack_json_data)
#Convert JSON data to CCLevelPack
def make_level_pack_from_json( json_data ):
    #Initialize a new CC Level Pack
    
    cclevel_pack = cc_classes.CCLevelPack()
    
    
    ### Begin Add Code Here ###
    #Loop through the json_data
    levels = json_data["levels"]

    for level in levels:
        #Create a new CCLevel object from the json_data by reading
        new_cclevel = cc_classes.CCLevel()
        
        #  level number
        level_number = level["level number"]
        new_cclevel.level_number = level_number
        
        #  time
        time = level["time"]
        new_cclevel.time = time

        #  number of chips
        num_chips = level["num chips"]
        new_cclevel.num_chips = num_chips

        #  upper layer
        upper_layer = level["upper layer"]
        new_cclevel.upper_layer = upper_layer

        #  optional fields (which requires reading map title, password, hint text and moving monster locations)
        optional_fields = level["optional_fields"]
        for field in optional_fields:
           #new_platform = test_data.Platform(platform["name"],platform["launch_year"])
           #new_game.platform = new_platform

        #Add that Game object to the game_library
        cclevel_pack.add_level(new_cclevel)    
    ### End Add Code Here ###

    return cclevel_pack


CCLevelPack = make_level_pack_from_json(level_pack_json_data)

print(CCLevelPack)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(CCLevelPack, "data/dpembert_ccl")
