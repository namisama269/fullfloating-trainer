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
        self.bld_mode = False
        self.show_cube = True
        self.show_targets = True
    
    def run(self):
        keybind_dict = keybind_333 
        running = True
        self.draw_cube()
    
        buttons = [
            """
            Button(50, 500, 140, 40, button_clr, hover_clr, ""),
            Button(50, 560, 140, 40, button_clr, hover_clr, ""),
            Button(210, 500, 180, 40, button_clr, hover_clr, ""),
            Button(210, 560, 180, 40, button_clr, hover_clr, ""),
            Button(50, 620, 140, 40, button_clr, hover_clr, ""),

            Button(500, 50, 140, 40, button_clr, hover_clr, ""),
            Button(660, 50, 140, 40, button_clr, hover_clr, ""),
            Button(820, 50, 240, 40, button_clr, hover_clr, ""),
            """
        ]

        while running:
            #self.update_button_text(buttons)
            #self.draw_buttons(buttons)
            # Display the cube after every event in case cube state was changed
            self.draw_cube()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    key = event.unicode
                    if key in keybind_dict:
                        self.cube.do_move(keybind_dict[key])
                    if event.key == pygame.K_RETURN:
                        self.display_targets()
                        self.reset_cube()
                    if event.key == pygame.K_ESCAPE:
                        self.reset_cube()
                    if event.key == pygame.K_SPACE:
                        self.display_alg()
                """
                # Process button presses
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Apply scramble
                    if buttons[0].is_hover():
                        self.apply_scramble()
                    if buttons[1].is_hover():
                        self.gen_scramble()
                    if buttons[2].is_hover():
                        self.toggle_auto_cb()
                    if buttons[3].is_hover():
                        self.change_cube_size()
                    if buttons[4].is_hover():
                        self.reset_cube()
                    if buttons[5].is_hover():
                        self.draw_memo()
                """

            pygame.display.update()

    def update_button_text(self, buttons):
        for i, button_text in enumerate([
            
        ]):
            buttons[i].set_text(button_text)            
    
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

    def display_targets(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 0, 500, 150), 0)  
        pygame.draw.rect(self.screen, bg_colour, (0, 500, 540, 150), 0)   
        target = gen_letter_pair(random.choice(train_pcs))
        self.curr_cycle = target
        self.curr_alg = get_3cycle(target['buffer'], target['targets'][0], target['targets'][1])
        ltr1 = letter_scheme[target['targets'][0]]
        ltr2 = letter_scheme[target['targets'][1]]
        out_txt = f"[{target['buffer']}]  {ltr1}{ltr2}"
        print(out_txt)
        if not self.show_targets:
            return
        text = fontbig.render(out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 80))
        self.screen.blit(text, text_rect)

    def display_alg(self):
        pygame.draw.rect(self.screen, bg_colour, (0, 500, 540, 150), 0)   
        out_txt = self.curr_alg
        text = fontmed.render(out_txt, True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH/2, 580))
        self.screen.blit(text, text_rect)

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
            text = font.render(self.text, True, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        return (mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and 
        mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height)

    def set_text(self, new_text):
        self.text = new_text
