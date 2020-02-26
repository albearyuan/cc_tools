import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_cc_level_pack_from_json( json_data ):
    #Initialize a new GameLibrary
    level_pack = cc_classes.CCLevelPack()

    json_levels = json_data['levels']

    level_number = 1
    for json_level in json_levels:
        level = cc_classes.CCLevel()
        level.level_number = level_number
        level.time = json_level['time']
        level.num_chips = json_level['num_chips']
        level.upper_layer = json_level['upper_layer']
        level.lower_layer = json_level['lower_layer']

        for json_field in json_level['optional_fields']:
            if json_field['field_type'] == 3:
                field = cc_classes.CCMapTitleField(json_field['title'])
            if json_field['field_type'] == 6:
                field = cc_classes.CCEncodedPasswordField(json_field['password'])
            if json_field['field_type'] == 7:
                field = cc_classes.CCMapHintField(json_field['hint'])
            if json_field['field_type'] == 10:
                monsters = []
                for json_monster in json_field['monsters']:
                    coordinate = cc_classes.CCCoordinate(json_monster['x'], json_monster['y'])
                    monsters.append(coordinate)
                field = cc_classes.CCMonsterMovementField(monsters)
            level.add_field(field)

        level_pack.add_level(level)
        level_number += 1

    return level_pack


input_json_file = "data/ayuan1_cc1.json"

with open(input_json_file) as json_file:
    data = json.load(json_file)
    level_pack = make_cc_level_pack_from_json(data)
    cc_dat_utils.write_cc_level_pack_to_dat(level_pack, 'data/ayuan1_cc1.dat')
