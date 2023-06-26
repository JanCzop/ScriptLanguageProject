import pygame


class Theme:

    def __init__(self, light_bg, dark_bg,
                 light_trace, dark_trace,
                 light_moves, dark_moves,
                 font):
        self.bg = Theme.Color(light_bg, dark_bg)
        self.trace = Theme.Color(light_trace, dark_trace)
        self.moves = Theme.Color(light_moves, dark_moves)
        self.font = font

    @staticmethod
    def lichess_theme():
        return Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646', pygame.font.SysFont('monospace', 18, bold=True))

    class Color:

        def __init__(self, light, dark):
            self.light = light
            self.dark = dark