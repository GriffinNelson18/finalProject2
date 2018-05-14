
'''Initial Idea: Space Invaders'''
#Pivot #1: Cubefield 'Turtle Edition' (4/7/18)
#Pivot #2: Meteor Dodge (4/27/18) 
    '''After dealing with numerous errors with the pygame module including issues with
    initialization and image loading, I consulted with my twin brother Carter and he 
    solved the bug because apparently my indentation was off??? (I'm pretty sure he 
    added a new line to my code adding in a centerx get_rect statement because I 
    noticed that he commented '#griffin you're an idiot' next to that line.) So, After
    Carter got the images to work I figured I could do a lot more with pygame than I 
    could with Turtle and decided to go with a new game called 'Meteor Dodge', basically
    a more immersive version of cubefield with images and sound effects.'''
#Pivot #3: Back to cubefield (5/6/18)
    '''I was highly disappointed with Pygame because after running successful trials with 
    the original images that I spent 2 hours gathering and editing in photoshop, Pygame 
    decided to stop working on its own and forget how to open the image file that it
    was able to do the day before. I also noticed that the same error occurred with sound 
    effects in Mr. Cozort's 'shmup.py' file, because I pulled a few lines from his code. 
    I ran his 'shmup' file that had worked when I first downloaded all the assets and it
    too stopped working due to an error with pygame opening one of the sound files.'''

#Cubefield design process:
    '''Luckily for me, the base code that I used with meteor dodge was very similar to what I 
    needed to make cubefield. I ultimately decided that images were too buggy with my computer
    for whatever reason, so I figured that it would be safest to just use Pygame sprites
    that were shaped as colorful rectangles. It has a cool retro gaming appeal to it, so I may
    make another attempt at adding in some retro sounding music and sound effects to go along
    with it, given that pygame cooperates. Kids Can Code was a big help for me, and his template
    provided me everything I needed to get started. I encountered an error on Monday (5/7/18)
    where the Player sprite (A class titled 'Glider' in the main.py file) would remain stuck
    in the corner of the screen no matter where I positioned it. I spent 2 hours rewatching the
    video to see where I went wrong, and I later found out after much frustration that literally
    ONE key was off that caused the rectangle to update back to a certain position every frame.
    I found this out because I added in the keystate conditional to the update loop, and every 
    time I pressed the arrow keys, I would notice it move a few pixels and then latch back to the
    initial location. I managed to patch the error and from there added in the enemy sprites 
    which is programmed in the Mob class, and an update file that makes the sprites move down 
    the y-axis. Every time the frame updates, 1 point is added to the Player's score. Therefore,
    every second the player is alive, they earn 60 points because the FPS = 60. Additionally,
    you will notice that there are no two enemy sprites on the same Y-axis line, and that is because
    each frame produces 1 new sprite after another, so they all come down in a ladder formation
    rather than in chunks.   '''

    #Key Concepts Included That I learned in class:
    '''
        -For Loops
        -If Statements
        -While Loops
        -Variables
        -String manipulation
        -Libraries
        -Classes
        -Functions (And parameters)
    '''

    #Concepts Learned Outside of Class:
    '''
        -Pygame base requirements
        -Sprites
        -Grouping sprites (Player, Mob)
        -Collisions
        
