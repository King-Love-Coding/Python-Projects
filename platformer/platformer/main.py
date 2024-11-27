import arcade
import os
import time

PATH = os.path.dirname(__file__) + os.sep

WIN_WIDTH = 1280
WIN_HEIGHT = 640
WIN_TITLE = "The Deep"
PLAYER_SPEED = 7
PLAYER_JUMP_SPEED = 25
TILE_WIDTH = 128

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIN_WIDTH, WIN_HEIGHT, WIN_TITLE)

        self.scene = None
        self.player = None

        self.physic_engine = None
        self.camera = None
        self.ui_camera = None

        self.keys_down = {'left': False, 'right': False}
        self.limits_worlds = {}

        self.tile_map = None

        self.score = 0
        self.current_level = 1
        self.game_over = False
        self.start_screen = True
        self.victory = False
        self.show_level_name = True
        self.level_name_start_time = None

        self.music = arcade.Sound(PATH + "assets/Music/MX_Platformer-8bit.mp3")
        self.music_playing = False

        self.slime_right = PATH + "assets/images/sprite/Slime_right.png"
        self.slime_left = PATH + "assets/images/sprite/Slime_left.png"

    def setup(self, level=1):
        arcade.set_background_color(arcade.color.BLUE_YONDER)
        self.current_level = level
        self.game_over = False
        self.start_screen = False
        self.victory = False
        self.show_level_name = True
        self.level_name_start_time = time.time()

        if self.current_level == 1:
            self.tile_map = arcade.load_tilemap(PATH + 'Level1.json')
        elif self.current_level == 2:
            self.tile_map = arcade.load_tilemap(PATH + 'Level2.json')

        self.camera = arcade.Camera()
        self.ui_camera = arcade.Camera(self.width, self.height)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.limits_worlds['left'] = 0
        self.limits_worlds['right'] = 128 * 15
        self.limits_worlds['down'] = 0

        self.player = arcade.Sprite(self.slime_right, 0.20)
        self.player.center_x = 100
        self.player.center_y = 500
        self.scene.add_sprite("Player", self.player)

        self.physic_engine = arcade.PhysicsEnginePlatformer(
            self.player, self.scene["Walls"], 2
        )

        if level == 1:
            self.score = 0

    def on_update(self, delta_time):
        if self.game_over or self.start_screen or self.victory:
            return

        self.player.change_x = 0
        if self.keys_down["left"]:
            if self.player.left > self.limits_worlds['left']:
                self.player.change_x = -PLAYER_SPEED
                self.player.texture = arcade.load_texture(self.slime_left)

        if self.keys_down["right"]:
            if self.player.right < self.limits_worlds['right']:
                self.player.change_x = PLAYER_SPEED
                self.player.texture = arcade.load_texture(self.slime_right)

        self.physic_engine.update()

        col_obj = arcade.check_for_collision_with_list(self.player, self.scene['Coins'])
        for obj in col_obj:
            obj.remove_from_sprite_lists()
            self.score += 100

        if arcade.check_for_collision_with_list(self.player, self.scene["Water"]):
            self.player_die()

        if arcade.check_for_collision_with_list(self.player, self.scene["Portal"]):
            self.load_next_level()

        self.center_camera_to_player()

        # Check if 5 seconds have passed to hide the level name
        if time.time() - self.level_name_start_time > 5:
            self.show_level_name = False

    def player_die(self):
        self.game_over = True

    def load_next_level(self):
        if self.current_level == 1:
            self.setup(level=2)
        elif self.current_level == 2:
            if self.score >= 1900:
                self.victory = True
            else:
                self.game_over = True

    def center_camera_to_player(self):
        camera_x = self.player.center_x - (self.camera.viewport_width / 2)
        camera_y = self.player.center_y - (self.camera.viewport_height / 2)

        if camera_x < self.limits_worlds['left']:
            camera_x = self.limits_worlds['left']

        if camera_x + self.camera.viewport_width > self.limits_worlds['right']:
            camera_x = self.limits_worlds['right'] - self.camera.viewport_width

        if camera_y < self.limits_worlds['down']:
            camera_y = self.limits_worlds['down']

        self.camera.move_to((camera_x, camera_y), 0.1)

    def on_key_press(self, symbol, modifiers):
        if self.start_screen:
            if symbol == arcade.key.ENTER:
                self.setup(level=1)
            elif symbol == arcade.key.ESCAPE:
                arcade.close_window()
            elif symbol == arcade.key.M:
                self.toggle_music()
            return

        if self.game_over or self.victory:
            if symbol == arcade.key.ENTER:
                self.setup(level=1)
            elif symbol == arcade.key.ESCAPE:
                arcade.close_window()
            return

        if symbol == arcade.key.A:
            self.keys_down["left"] = True
            self.player.texture = arcade.load_texture(self.slime_left)

        if symbol == arcade.key.D:
            self.keys_down["right"] = True
            self.player.texture = arcade.load_texture(self.slime_right)

        if symbol == arcade.key.W:
            if self.physic_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if self.game_over or self.start_screen or self.victory:
            return

        if symbol == arcade.key.A:
            self.keys_down["left"] = False

        if symbol == arcade.key.D:
            self.keys_down["right"] = False

    def on_draw(self):
        self.clear()
        if self.start_screen:
            self.draw_start_screen()
        elif self.game_over:
            self.draw_game_over_screen()
        elif self.victory:
            self.draw_victory_screen()
        else:
            self.camera.use()
            self.scene.draw()

            self.ui_camera.use()
            arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 20)
            if self.show_level_name:
                self.draw_level_name()

    def draw_start_screen(self):
        arcade.draw_text("The Deep", self.width / 2, self.height / 2 + 100,
                         arcade.color.WHITE, 50, anchor_x="center")
        arcade.draw_text("Press ENTER to start", self.width / 2, self.height / 2,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press ESC to quit", self.width / 2, self.height / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press M to toggle music", self.width / 2, self.height / 2 - 100,
                         arcade.color.WHITE, 20, anchor_x="center")

    def draw_game_over_screen(self):
        arcade.draw_text("Game Over", self.width / 2, self.height / 2 + 50,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Press ENTER to restart", self.width / 2, self.height / 2,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press ESC to quit", self.width / 2, self.height / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center")

    def draw_victory_screen(self):
        arcade.draw_text("You did this!", self.width / 2, self.height / 2 + 50,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Press ENTER to restart", self.width / 2, self.height / 2,
                         arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press ESC to quit", self.width / 2, self.height / 2 - 50,
                         arcade.color.WHITE, 20, anchor_x="center")

    def draw_level_name(self):
        level_names = {1: "The world", 2: "Cave of slimers"}
        level_name = level_names.get(self.current_level, "")
        arcade.draw_text(f"{level_name}", self.width / 2, self.height - 100,
                         arcade.color.WHITE, 40, anchor_x="center")

    def toggle_music(self):
        if self.music_playing:
            self.music.stop()
        else:
            self.music.play(loop=True)
        self.music_playing = not self.music_playing


game = MyGame()
arcade.run()
