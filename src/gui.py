from math import e
import pygame
from pygame import gfxdraw
from pygame.locals import *

from cube import Cube

from config import *
from presets import *
from targets import *
from alg import *

WIDTH = 500
HEIGHT = 720

pygame.init()

# Enter the display font (recommended to not change)
#fontbig = pygame.font.Font('cyberbit.ttf', 40)
font = pygame.font.Font('freesansbold.ttf', 16)
fontbig = pygame.font.Font('freesansbold.ttf', 40)
fontmed = pygame.font.Font('freesansbold.ttf', 24)
fontsmall = pygame.font.Font('freesansbold.ttf', 16)

class Gui:
    """
    GUI to display virtual cube
    """
    def __init__(self, cube: Cube):
        self.cube = cube
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.virtualcube = pygame.Surface((500,400))
        self.screen.fill(bg_colour)
        self.virtualcube.fill(bg_colour)
        self.curr_alg = ""
        self.curr_cycle = {
            'buffer': "",
            'targets': ["", ""],
        }
        self.pce_idx = 0
        self.bld_mode = False
        self.show_cube = True
        self.show_targets = True
        self.out_txt = ""
        self.buttons = [
            Button(50, 650, 40, 40, button_clr, hover_clr, pce_types[self.pce_idx].upper()),
            Button(110, 650, 100, 40, button_clr, hover_clr, "Show Cube"),
            Button(230, 650, 130, 40, button_clr, hover_clr, "Show Targets"),
        ]
    
    def run(self):
        keybind_dict = keybind_333 
        running = True
        self.draw_cube()

        while running:
            #self.update_button_text(buttons)
            #self.draw_buttons(buttons)
            # Display the cube after every event in case cube state was changed
            self.draw_cube()
            self.draw_buttons(self.buttons)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    key = event.unicode
                    if key in keybind_dict:
                        self.cube.do_move(keybind_dict[key])
                    if event.key == pygame.K_RETURN:
                        self.gen_targets()
                        self.display_targets()
                        self.draw_cube()
                        self.reset_cube()
                    if event.key == pygame.K_ESCAPE:
                        self.reset_cube()
                    if event.key == pygame.K_SPACE:
                        self.clear_alg()
                        self.display_alg()
                    if event.key == pygame.K_TAB:
                        self.pce_idx += 1
                        self.pce_idx %= 2
                        self.buttons[0].set_text(pce_types[self.pce_idx].upper())
                
                # process button presses
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttons[0].is_hover():
                        self.pce_idx += 1
                        self.pce_idx %= 2
                        self.buttons[0].set_text(pce_types[self.pce_idx].upper())
                    if self.buttons[1].is_hover():
                        self.show_cube = not self.show_cube
                        self.draw_cube()
                    if self.buttons[2].is_hover():
                        self.show_targets = not self.show_targets
                        self.display_targets()
                        
            pygame.display.update()    
    
    def draw_cube(self):
        self.virtualcube.fill(bg_colour)
        if not self.show_cube:
            return
        # Coordinates of all facelet points
        for i, face in enumerate(facelets[self.cube.size]):
            for j, points in enumerate(face):
                x = j // self.cube.size
                y = j % self.cube.size
                if self.bld_mode:
                    if self.cube.faces["DLRBFU"[i]][x][y][0] == self.curr_cycle['buffer']:
                        stk_colour = target_clr2
                    elif self.cube.faces["DLRBFU"[i]][x][y][0] == self.curr_cycle['targets'][0]:
                        stk_colour = buffer_clr
                    elif self.cube.faces["DLRBFU"[i]][x][y][0] == self.curr_cycle['targets'][1]:
                        stk_colour = target_clr1
                    elif len(self.cube.faces["DLRBFU"[i]][x][y][0]) == len(self.curr_cycle['buffer']):
                        stk_colour = highlight_clr
                    else:
                        stk_colour = fill_clr
                else:
                    stk_colour = face_colours[self.cube.faces["DLRBFU"[i]][x][y][1]]
                pygame.gfxdraw.filled_polygon(self.virtualcube, points, stk_colour)
                pygame.gfxdraw.aapolygon(self.virtualcube, points, (0,0,0))
        
        self.screen.blit(self.virtualcube, (35,120))

    def draw_buttons(self, buttons):
        for button in buttons:
            button.draw(self.screen)

    def gen_targets(self):
        pce_type = pce_types[self.pce_idx]
        target = gen_letter_pair(pce_type)
        self.curr_cycle = target
        self.curr_alg = get_3cycle(target['buffer'], target['targets'][0], target['targets'][1])
        ltr1 = letter_scheme[target['targets'][0]]
        ltr2 = letter_scheme[target['targets'][1]]
        out_txt = f"[{target['buffer']}]  {ltr1}{ltr2}"
        print(out_txt)
        self.out_txt = out_txt

    def display_targets(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 0, 500, 150), 0)  
        pygame.draw.rect(self.screen, bg_colour, (0, 500, 540, 150), 0)   
        if not self.show_targets:
            return
        text = fontbig.render(self.out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 80))
        self.screen.blit(text, text_rect)

    def display_alg(self):
        out_txt = self.curr_alg
        text = fontmed.render(out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 580))
        self.screen.blit(text, text_rect)

    def clear_alg(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 500, 540, 150), 0)   

    def reset_cube(self):
        self.cube.reset()
        for _ in range(2):
            self.cube.do_scramble(comm_to_moves(self.curr_alg))

class Button:
    def __init__(self, x, y, width, height, button_clr, hover_clr, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_clr = button_clr
        self.hover_clr = hover_clr
        self.text = text

    def draw(self, screen):
        display_clr = self.hover_clr if self.is_hover() else self.button_clr
        pygame.draw.rect(screen, display_clr, (self.x,self.y,self.width,self.height), 0)

        if self.text != "":
            text = fontsmall.render(self.text, True, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and 
        mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height)

    def set_text(self, new_text):
        self.text = new_text
