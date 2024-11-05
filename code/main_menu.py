from resources import Resources
import pygame


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.level_num = game.level_num
        self.level_lists = game.level_lists
        self.continue_color = (255, 255, 255)
        self.new_game_color = (255, 255, 255)
        self.exit_color = (255, 255, 255)
        self.resources = Resources()

    def _render_text(self, text, font_size, color):
        font = pygame.font.Font(self.resources.font_path, font_size)  # Create the font with the new size
        text_surface = font.render(text, True, color)  # Render the text
        return text_surface

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self._handle_mouse_click(mouse_x, mouse_y)

    def _handle_mouse_click(self, mouse_x, mouse_y):
        """Handle mouse click events for menu items"""
        # Check if "Continue Game" is clicked
        if self.level_num != 0:
            text_surface1 = self._render_text("继续游戏", 36, (255, 255, 255))
            text_rect1 = text_surface1.get_rect(topleft=(528, 500))
            if text_rect1.collidepoint(mouse_x, mouse_y):
                self.game.start = True

        # Check if "New Game" is clicked
        text_surface2 = self._render_text("新的开始", 36, (255, 255, 255))
        text_rect2 = text_surface2.get_rect(topleft=(528, 550))
        if text_rect2.collidepoint(mouse_x, mouse_y):
            self.game.level_num = 1
            self.game.level = self.level_lists[self.level_num](self.game)
            self.game.start = True

        # Check if "New Game" is clicked
        text_surface3 = self._render_text("退出游戏", 36, (255, 255, 255))
        text_rect3 = text_surface3.get_rect(topleft=(528, 600))
        if text_rect3.collidepoint(mouse_x, mouse_y):
            pygame.quit()
            exit()

    def run_menu(self):
        self._check_events()

        # Fill the screen with a background color
        self.screen.fill((0, 0, 0))

        # Get the current mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if the mouse is over the "继续游戏" text
        if self.level_num != 0:
            text_surface1 = self._render_text("继续游戏", 36, self.continue_color)
            text_rect1 = text_surface1.get_rect(topleft=(528, 500))
            if text_rect1.collidepoint(mouse_x, mouse_y):
                if self.continue_color != (255, 0, 0):
                    self.resources.sounds['button_beep'].play()
                self.continue_color = (255, 0, 0)  # Change to red when hovered
            else:
                self.continue_color = (255, 255, 255)

            # Render "继续游戏" text with the updated color
            text_surface1 = self._render_text("继续游戏", 36, self.continue_color)
            self.screen.blit(text_surface1, text_rect1)

        # Check if the mouse is over the "新游戏" text
        text_surface2 = self._render_text("新的开始", 36, self.new_game_color)
        text_rect2 = text_surface2.get_rect(topleft=(528, 550))
        if text_rect2.collidepoint(mouse_x, mouse_y):
            if self.new_game_color != (255, 0, 0):
                self.resources.sounds['button_beep'].play()
            self.new_game_color = (255, 0, 0)  # Change to red when hovered
        else:
            self.new_game_color = (255, 255, 255)

        # Render "新游戏" text with the updated color
        text_surface2 = self._render_text("新的开始", 36, self.new_game_color)
        self.screen.blit(text_surface2, text_rect2)

        # Check if the mouse is over the "退出游戏" text
        text_surface3 = self._render_text("退出游戏", 36, self.exit_color)
        text_rect3 = text_surface3.get_rect(topleft=(528, 600))
        if text_rect3.collidepoint(mouse_x, mouse_y):
            if self.exit_color != (255, 0, 0):
                self.resources.sounds['button_beep'].play()
            self.exit_color = (255, 0, 0)  # Change to red when hovered
        else:
            self.exit_color = (255, 255, 255)

        # Render "退出游戏" text with the updated color
        text_surface3 = self._render_text("退出游戏", 36, self.exit_color)
        self.screen.blit(text_surface3, text_rect3)

        # Update the display
        pygame.display.flip()
