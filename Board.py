import pygame 
class Board :
    def __init__(self , screen , size , tilesize) :
        self.screen = screen 
        self.size = size 
        self.tilesize = tilesize 
        self.Board_surface = pygame.Surface((15*self.tilesize , 15*self.tilesize) )
        self.Board_surface.fill((255,255,255))
        self.WorkFlow()

    
    def draw_Grid(self) :
        for i in range (16) :
            pygame.draw.line(self.Board_surface , (0,0,0) , (50*(i+1),0) , (50*(i+1),self.size[1]))

        for i in range (16) :
            pygame.draw.line(self.Board_surface , (0,0,0) , (0,(i+1)*50) , (self.size[0] , (i+1)*50))

        
    
    def draw_House(self , House_color , House_no ) :
        self.House_color = House_color 
        self.House_no = House_no
        self.center = (7.5*self.tilesize , 7.5*self.tilesize)
        self.House_surface = pygame.Surface((6*self.tilesize , 6*self.tilesize) )
        self.House_surface.fill(self.House_color)
        self.inner_surface = pygame.Surface((4*self.tilesize , 4*self.tilesize) )
        self.inner_surface.fill((255,255,255))

        self.horizontal_colored_path = pygame.Surface((5*self.tilesize , self.tilesize))
        self.vertical_colored_path = pygame.Surface(( self.tilesize , 5*self.tilesize))

        self.house_entry_tile = pygame.Surface((self.tilesize , self.tilesize))


        for i in range (2) :
            for j in range (2) :
                pygame.draw.circle(self.inner_surface , self.House_color , ((2*(i+1)-1)*self.tilesize , (2*(j+1)-1)*self.tilesize) , self.tilesize/2 ) 
        
        self.House_surface.blit(self.inner_surface , (self.tilesize , self.tilesize , 4*self.tilesize , 4*self.tilesize ))

        self.Board_surface.blit(self.House_surface , (House_no[0]*9*self.tilesize, House_no[1]*9*self.tilesize , 6*self.tilesize , 6*self.tilesize))

        

        if (self.House_no[0] == self.House_no[1]) :

            self.house_entry_tile.fill(self.House_color)
            self.Board_surface.blit(self.house_entry_tile , ((12*House_no[0] + 1)*self.tilesize , (self.House_no[0]*2 + 6)*self.tilesize , self.tilesize , self.tilesize ))

            self.horizontal_colored_path.fill(self.House_color)
            self.Board_surface.blit(self.horizontal_colored_path , ((8*House_no[0] + 1)*self.tilesize , 7*self.tilesize , 5*self.tilesize , self.tilesize ) )

            pygame.draw.polygon(self.Board_surface , self.House_color , [self.center , ((3*self.House_no[0] + 6)*self.tilesize , 6*self.tilesize) , ((3*self.House_no[0] + 6)*self.tilesize , 9*self.tilesize )])
                                    
        else :
            self.house_entry_tile.fill(self.House_color)
            self.Board_surface.blit(self.house_entry_tile , ((self.House_no[0]*2 + 6)*self.tilesize , (self.House_no[1]*12 + 1)*self.tilesize , self.tilesize , self.tilesize))


            self.vertical_colored_path.fill(self.House_color)
            self.Board_surface.blit(self.vertical_colored_path , (7*self.tilesize , (8*House_no[1] + 1)*self.tilesize , 5*self.tilesize , self.tilesize  ))

            pygame.draw.polygon(self.Board_surface , self.House_color , [self.center , (6*self.tilesize , (3*self.House_no[1] + 6)*self.tilesize) , ( 9*self.tilesize , (3*self.House_no[1] + 6)*self.tilesize )])

            
    def WorkFlow(self) :
        self.draw_Grid()
        self.draw_House((255,0,0) , (0,0))
        self.draw_House((0,255,0) , (1,0))
        self.draw_House((0,191,255) , (0,1))
        self.draw_House((255,255,0) , (1,1))

       





        

    
    




         

    

    

