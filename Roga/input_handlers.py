import libtcodpy as libtcod


def handle_keys(key):
    # Movement keys
    key_char = chr(key.c)
    if key_char == 'w':
        return {'move': (0, -1)}
    elif key_char == 's':
        return {'move': (0, 1)}
    elif key_char == 'a':
        return {'move': (-1, 0)}
    elif key_char == 'd':
        return {'move': (1, 0)}
    elif key_char == 'q':
        return {'move': (-1, -1)}
    elif key_char == 'e':
        return {'move': (1, -1)}
    elif key_char == 'c':
        return {'move': (1, 1)}
    elif key_char == 'z':
        return {'move': (-1, 1)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    

    # No key was pressed
    return {}