import arcade, os, time, math

WIN_WIDTH = 1280
WIN_HEIGHT = 700
WIN_TITLE = "Demon birds"
GRAVITY = (0, -1000)

STATE_STAND = 0
STATE_DIED = 1

PATH = os.path.dirname(__file__) + os.sep

class Enemy(arcade.Sprite):
    def __init__(self, path, scale=1.5):
        super().__init__()

        self.frame = 0

        self.delay = 0.2
        self.last_animation = time.time()

        self.state = STATE_STAND

        self.scale = scale
        self.enemies_textures = [
            [arcade.load_texture(PATH + 'assets/pig.png')],
            [arcade.load_texture(PATH + 'assets/pig_dead1.png')]
        ]
        self.texture = self.enemies_textures[self.state][0]

    def animation(self):
        animate_layer = self.enemies_textures[self.state]

        if (time.time() - self.last_animation) >= self.delay:
            if self.frame < len(animate_layer):
                self.frame += 1
            if self.frame == len(animate_layer):
                self.frame = 0
            self.texture = animate_layer[self.frame]
            self.last_animation = time.time()

class GameScene(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color((75, 160, 255))

        tile_map = arcade.load_tilemap(PATH + "assets/main.json")

        self.scene = arcade.Scene.from_tilemap(tile_map)

        self.camera = arcade.Camera(WIN_WIDTH, WIN_HEIGHT)

        self.bird_count = 3

        self.follow_shell = None

        self.fire = False

        self.world_limits = {
            'left': 0,
            'right': tile_map.width * tile_map.tile_width,
            'down': 0,
            'up': tile_map.height * tile_map.tile_height
        }

        self.power = 1050

        self.gun = arcade.Sprite('assets/artillery.png', scale=0.35)
        self.gun.left = 20
        self.gun.bottom = 150
        self.scene.add_sprite("Gun", self.gun)

        self.physics_engine = arcade.PymunkPhysicsEngine(GRAVITY)

        self.physics_engine.add_sprite_list(self.scene['walls'], body_type=arcade.PymunkPhysicsEngine.STATIC, friction=1)
        self.physics_engine.add_sprite_list(self.scene['planks'], friction=0.4, elasticity=0.3, collision_type='planks')

        self.fly_init = tile_map.object_lists['enemies']

        for point in self.fly_init:
            fly = Enemy(PATH + "assets/pig.png", 0.35)
            fly.left = point.shape[0]
            fly.center_y = point.shape[1]
            fly.center_x = point.shape[0]
            print(fly.center_x, fly.center_y)
            self.scene.add_sprite('enemies', fly)
            self.physics_engine.add_sprite(fly, collision_type='enemy')

        self.enemy_count = len(self.fly_init)

        def object_collision(enemy, shell, *args):
            if enemy.state == STATE_STAND:
                enemy.state = STATE_DIED
                enemy.frame = 0
                self.enemy_count -= 1
                print(self.enemy_count)
                if self.enemy_count == 0:
                    victory_view = VictoryView()
                    self.window.show_view(victory_view)

        self.physics_engine.add_collision_handler('enemy', 'shell', post_handler=object_collision)

        def planks_collision(planks, shell, *args):
            planks.remove_from_sprite_lists()
        self.physics_engine.add_collision_handler('planks', 'shell', post_handler=planks_collision)

    def on_mouse_press(self, x, y, button, modifier):
        if not self.fire:
            shell_x = self.gun.center_x + (self.gun.width / 2) * math.cos(math.radians(self.angle))
            shell_y = self.gun.center_y + (self.gun.width / 2) * math.sin(math.radians(self.angle))
            shell = arcade.Sprite("assets/bird.png", center_x=shell_x, center_y=shell_y, scale=0.13)
            self.scene.add_sprite("Shells", shell)

            self.physics_engine.add_sprite(shell, collision_type='shell')


            force_direction_x = shell_x - self.gun.center_x
            force_direction_y = shell_y - self.gun.center_y


            self.physics_engine.apply_force(shell, (force_direction_x * self.power, force_direction_y * self.power))
            self.follow_shell = shell
            self.fire = True

    def center_camera_to_object(self, obj):
        camera_x = obj.center_x - (self.camera.viewport_width / 2)
        camera_y = obj.center_y - (self.camera.viewport_height / 2)
        if camera_x < self.world_limits['left']:
            camera_x = self.world_limits['left']
        if camera_x + self.camera.viewport_width > self.world_limits['right']:
            camera_x = self.world_limits['right'] - self.camera.viewport_width
        if camera_y < self.world_limits['down']:
            camera_y = self.world_limits['down']
        if camera_y + self.camera.viewport_height > self.world_limits['up']:
            camera_y = self.world_limits['up'] - self.camera.viewport_height
        self.camera.move_to((camera_x, camera_y), 0.1)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        x_diff = x - self.gun.center_x
        y_diff = y - self.gun.center_y

        angle = math.degrees(math.atan2(y_diff, x_diff))
        if -50 <= angle <= 50:
            self.gun.angle = self.angle = angle

        return super().on_mouse_motion(x, y, dx, dy)

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        for enemy in self.scene['enemies']:
            enemy.animation()
        if self.follow_shell:
            self.center_camera_to_object(self.follow_shell)

        self.draw_text_with_outline(f"Enemies Left: {self.enemy_count}", self.camera.position[0] + 10, self.camera.position[1] + WIN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_update(self, delta_time: float):
        self.physics_engine.step(delta_time)
        self.scene.update()
        if self.follow_shell:
            velocity = self.physics_engine.get_physics_object(self.follow_shell).body.velocity
            if velocity[0] < 1 and velocity[1] < 1:
                self.follow_shell = None
                self.fire = False
                self.center_camera_to_object(self.gun)

    def draw_text_with_outline(self, text, start_x, start_y, color, font_size, outline_color=arcade.color.BLACK, outline_width=2):
        arcade.draw_text(text, start_x - outline_width, start_y, outline_color, font_size)
        arcade.draw_text(text, start_x + outline_width, start_y, outline_color, font_size)
        arcade.draw_text(text, start_x, start_y - outline_width, outline_color, font_size)
        arcade.draw_text(text, start_x, start_y + outline_width, outline_color, font_size)
        arcade.draw_text(text, start_x, start_y, color, font_size)

class StartView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)

    def on_draw(self):
        self.clear()
        self.draw_text_with_outline("Demon birds", WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50, arcade.color.FLORAL_WHITE, 90, outline_width=7, anchor_x="center")
        self.draw_text_with_outline("Click to Start", WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50, arcade.color.ANTI_FLASH_WHITE, 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameScene()
        self.window.show_view(game_view)

    def draw_text_with_outline(self, text, start_x, start_y, color, font_size, outline_color=arcade.color.BLACK, outline_width=2, anchor_x="left"):
        arcade.draw_text(text, start_x - outline_width, start_y, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x + outline_width, start_y, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y - outline_width, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y + outline_width, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y, color, font_size, anchor_x=anchor_x)

class VictoryView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.EARTH_YELLOW)

    def on_draw(self):
        self.clear()
        self.draw_text_with_outline("You destroyed all enemies!", WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50, arcade.color.ORANGE_PEEL, 50, outline_width=5, anchor_x="center")
        self.draw_text_with_outline("Click to Start", WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50, arcade.color.ANTI_FLASH_WHITE, 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameScene()
        self.window.show_view(game_view)

    def draw_text_with_outline(self, text, start_x, start_y, color, font_size, outline_color=arcade.color.BLACK, outline_width=2, anchor_x="left"):
        arcade.draw_text(text, start_x - outline_width, start_y, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x + outline_width, start_y, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y - outline_width, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y + outline_width, outline_color, font_size, anchor_x=anchor_x)
        arcade.draw_text(text, start_x, start_y, color, font_size, anchor_x=anchor_x)

window = arcade.Window(WIN_WIDTH, WIN_HEIGHT, WIN_TITLE)
start_view = StartView()
window.show_view(start_view)
arcade.run()
