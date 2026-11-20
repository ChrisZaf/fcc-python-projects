test_settings = {'theme' : 'dark',
    'language' : 'English',
    'notifications' : 'On'}

def add_setting(sett_dict, item):
    setting, kval = item
    setting = setting.lower()
    kval = kval.lower()

    if setting in sett_dict:
        return f"Setting '{setting}' already exists! Cannot add a new setting with this name."

    sett_dict[setting] = kval
    return f"Setting '{setting}' added with value '{kval}' successfully!"


def update_setting(sett_dict, item):
    setting, kval = item
    setting = setting.lower()
    kval = kval.lower()
    
    if setting in sett_dict:
        sett_dict[setting]=kval
        return f"Setting '{setting}' updated to '{kval}' successfully!"
    else:
        return f"Setting '{setting}' does not exist! Cannot update a non-existing setting."

def delete_setting(sett_dict, setting):
    setting = setting.lower()
    if setting in sett_dict:
        del sett_dict[setting]
        return f"Setting '{setting}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(sett_dict):
    if not sett_dict:
        return 'No settings available.'
    else:
       settings_display ='Current User Settings:\n'
       for key, value in sett_dict.items():
           key = key.capitalize()
           val = value
           settings_display += f'"{key}: {val}\n"'
    return settings_display 
        

