# You're on the surface, you fall down underground. The only way back up is 
# through a series of caves and catacombs to find a key that allows you back up.
print ('You were playing in a forest on the surface. You fell down a hole in the earth')
has_determination = False
def the_ruins():
    global has_determination
    if has_determination:
        get_key()
        
    print('These are the ruins.')
    if not has_determination:
        print ('You must find your way back up to the surface.')
    print('east: cave')
    print('west: tombs')
    print('north: catacombs')
    choice = input('I think I will go ')
    if choice == 'east':
        cave()
    elif choice == 'west':
        tombs() 
    elif choice == 'north':
        catacombs()

    else:
        the_ruins()
        
def catacombs():
    if has_determination:
        get_key()
        
    print('You are in the catacombs. It may be dark and dreary.')
    print('But you are getting closer to the surface')
    print('east: another cave')
    print('west: The Under There')
    print('north: boiler room')
    print('south: the ruins')
    choice = input('I think I will go ')
    if choice == 'east':
        another_cave()
    elif choice == 'west':        
        under_there()
    elif choice == 'north':
        boiler_room()
    elif choice == 'south':
        print("Back so soon? You're going the wrong way")
        the_ruins()
    else:
        under_there()
        
def cave():
    if has_determination:
        get_key()
        
    print("You're in a cave. How will you ever get out of here?")
    print('north: another cave')
    print('west: the ruins')
    choice = input('Guess I must go ')
    if choice == 'north':
        another_cave()
    elif choice == 'west':
        the_ruins()
    else:
        the_ruins()
        
def tombs():
    if has_determination:
        get_key()
    
    print('You walked into The Tombs. Here, all the surface dwellers who never')
    print('made it back home have to rest here...')    
    print(' "A person! So many years, finally a person!" ')
    print('You wonder who this is so you ask their name')
    print(' "My name is Chara and I fell down here a long time ago." ')
    print(' "I think there is a key but I have no idea what door it opens." ')
    print(' "It might lead you back to the surface but you have to go to Under There" ')
    print('east: the ruins')
    choice = input('Looks like I have to go back ')
    if choice == 'east':
        the_ruins()
    else:
        the_ruins()
        
def boiler_room():
    if has_determination:
        get_key()
        
    print("Never gonna give you up, Never gonna let you down" * 50)
    print("YOU JUST GOT RICK ROLLED! GO BACK!")
    print('south: catacombs')
    choice = input ('Guess I have to go back ')
    if choice == 'south':
        catacombs()
    else:   
        catacombs()     

def another_cave():
    if has_determination:
        get_key()
    
    print('Oh man, this cave is darker than the last one and nothing is here')
    print('south: cave')
    print('west: catacombs')
    choice = input ('Looks like I better go ')
    if choice == 'south: cave':
        cave()
    elif choice == 'west':
        catacombs()

def under_there():
    
    print('This is The Under There. It holds the treasures of The Ruins')
    print(' "Chara was right, this room has a key!" ')
    print('Chara comes from out of the shadows...')
    print('"Told ya! If I were still alive, I would take that key')
    print('and run for the surface" ')
    print('yes: get key')
    print('no: leave key')
    choice = input ('Do you want the key? ')
    if choice == 'yes':
            print('You may proceed to the hallway...')
            hallway()
        
    elif choice == 'no':
            print('You cannot reach the surface without a key....')
            the_ruins() 
 
def hallway():
            
    print('You made it to the Great Hallway of The Ruins. Closer to the surface than ever...')
    print('The key you have in your hand unlocks more than one door. But only one door')
    print('leads you back to the surface...')
    print('Door Number 1: One Way')
    print('Door Number 2: Another Way')
    choice = input ('Unlock Door Number ')
    if choice == '1':
        print('This is The Swamp. Once here, you are here forever....')
        print('GAME OVER')
        swamp()
    elif choice == '2':
        print('You made it!! You are back home!')
        print('YOU WIN!!')
        surface()
     
def surface():
    if has_determination:
        get_key()
        
    
    
def swamp():
    if has_determination:
        get_key()
        
      
the_ruins()
