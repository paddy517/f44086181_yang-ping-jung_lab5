#from tower import TowerGroup
import pygame
import os

#導入圖像
SELL_IMAGE=pygame.image.load(os.path.join("images","sell.png"))
UPGRADEMENU_IMAGE = pygame.image.load(os.path.join("images","upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images","upgrade.png"))


class UpgradeMenu:
    def __init__(self, x, y):
        #設定參數
        self.menu = pygame.transform.scale(UPGRADEMENU_IMAGE,(200,200)) # menu image
        self.sell = pygame.transform.scale(SELL_IMAGE,(40,40))  #sell image
        self.upgrade = pygame.transform.scale(UPGRADE_IMAGE,(50,30)) #upgrade inage
        self.rect= self.menu.get_rect() #get (width,height) from menu image
        self.rect.center = (x,y)    #get menu image center  point 

        #  Add buttons 
        self.__buttons = [Button(self.upgrade,"upgrade",self.rect.centerx,self.rect.centery-70),
                        Button(self.sell,"sell",self.rect.centerx,self.rect.centery+70)]  

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """

        # draw menu
        win.blit(self.menu,(self.rect.centerx - 100,self.rect.centery - 100))
        # draw button
        win.blit(self.sell,(self.rect.centerx - 20 , self.rect.centery + 55))
        win.blit(self.upgrade,(self.rect.centerx - 25 , self.rect.centery - 85))



        

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect= self.image.get_rect()
        self.rect.center = (x,y)




    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        
        #判斷滑鼠是否有點在button上
        if self.rect.collidepoint(x,y):
            return True
        return False
        
        
        

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name    #回傳button名字(str)






