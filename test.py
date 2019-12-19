import pygame.examples.eventlist

pygame.examples.eventlist.main()
#####
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
