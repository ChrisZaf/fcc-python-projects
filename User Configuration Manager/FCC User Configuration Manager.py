test_settings = {'theme' : 'dark',
    'language' : 'English',
    'notifications' : 'On'}

def add_setting(diction, item):
    setting, kval = item
    setting = setting.lower()
    kval = kval.lower()

    if setting in diction:
        return f"Setting '{setting}' already exists! Cannot add a new setting with this name."

    diction[setting] = kval
    return f"Setting '{setting}' added with value '{kval}' successfully!"


def update_setting(diction, item):
    setting, kval = item
    setting = setting.lower()
    kval = kval.lower()
    
    if setting in diction:
        diction[setting]=kval
        return f"Setting '{setting}' updated to '{kval}' successfully!"
    else:
        return f"Setting '{setting}' does not exist! Cannot update a non-existing setting."

    