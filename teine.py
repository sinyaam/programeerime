from pykkar import *
def myPykkar():
    create_world("""
    ########
    #  >   #
    #      #
    #      #
    #      #
    #      #
    ########
    """)
    for i in range(18):
        if is_painted() == False:
            if is_wall() == True:
                right()
            paint()
            step()
            
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    step()
    paint()

    right()
    step()
    paint()
    right()
    step()
    paint()
    step()
    paint()
    step()
    paint()
    
    right()
    step()
    step()
    paint()
    step()
    paint()
    
    right()
    step()
    paint()
    step()
    paint()
    right()
    step()
    paint()
    right()
    step()
    paint()
    paint()