#import something here, i'd say it
#seems like the best place to do it

class Instrument():
    '''
    To Be Written

    This class contains a Synth, a collection of Notes, a Layo-
    ut, and metric info for each "x". I think this class is ac-
    ted upon by the Score, but i'm not sure. When the file gets
    saved, most of the data is probably taken from the instrum-
    ents and dumped in some efficient container, which is dump-
    ed into a file.

    This class might be kinda big, so we might need to split it
    up later if we need to.
    '''
    def __init__():
        pass

    def change_synth():
        pass

    def change_layout():
        pass

    def add_note():
        pass

    def add_tuplet():
        pass

    def remove():
        pass

    def select():
        #i think selections should be lists, so you can select
        #a tuplet, and then something inside of it, and then
        #deselect back to the tuplet
        pass

    def deselect():
        pass

    def move_selected():
        pass

    def extend_selected():
        pass

    def add_accidental():
        #what the accidentals are is determined by the Layout.
        pass

    #surely there will be more, but those will be added later
    
