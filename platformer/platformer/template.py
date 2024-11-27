"""
Шаблон платформера
"""
import arcade

# --- Константи
SCREEN_TITLE = "Платформер"

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

# Константи для масштабування спрайтів зі збереженням пропорцій
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Швидкість руху гравця, у пікселях на кадр
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):
    """
    Головний клас додатку.
    """

    def __init__(self):

        # Виклик батьківського класу та налаштування вікна
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,
                         SCREEN_TITLE, resizable=True)

        # Наш об'єкт Карти Тайлів
        self.tile_map = None

        # Наш об'єкт Сцени
        self.scene = None

        # Окрема змінна для гравця
        self.player_sprite = None

        # Наш фізичний двигун
        self.physics_engine = None

        # Камера для прокрутки екрану
        self.camera_sprites = None

        # Камера, яка не прокручується і може використовуватися для відображення елементів GUI
        self.camera_gui = None

        # Ведення рахунку очків
        self.score = 0

        # Яка клавіша натиснута?
        self.left_key_down = False
        self.right_key_down = False

    def setup(self):
        """Налаштування гри тут. Викликайте цю функцію, щоб перезапустити гру."""

        # Налаштування камер
        self.camera_sprites = arcade.Camera(self.width, self.height)
        self.camera_gui = arcade.Camera(self.width, self.height)

        # Ім'я файлу карти для завантаження
        map_name = ":resources:tiled_maps/map.json"

        # Налаштування опцій для окремих шарів карти на основі назв шарів у словнику
        # Це робить так, що SpriteList для шарів платформ використовує хешування для виявлення.
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }

        # Зчитування карти
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Ініціалізація сцени з нашою картою та автоматичне додавання всіх шарів як SpriteLists у сцену в потрібному порядку.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Встановлення кольору фону
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Ведення рахунку очків
        self.score = 0

        # Налаштування гравця, зокрема його розміщення за цими координатами.
        src = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(src, CHARACTER_SCALING)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # --- Інше
        # Створення фізичного двигуна
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]
        )

    def on_draw(self):
        """Відображення екрану."""

        # Очистка екрану до кольору фону
        self.clear()

        # Активація камери гри
        self.camera_sprites.use()

        # Відображення сцени
        self.scene.draw()

        # Активація камери GUI перед відображенням елементів GUI
        self.camera_gui.use()

        # Відображення рахунку на екрані, який прокручується разом із відображенням
        score_text = f"Рахунок: {self.score}"
        arcade.draw_text(score_text,
                         start_x=10,
                         start_y=10,
                         color=arcade.csscolor.WHITE,
                         font_size=18)

    def update_player_speed(self):

        # Розрахунок швидкості на основі натискання клавіш
        self.player_sprite.change_x = 0

        if self.left_key_down and not self.right_key_down:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_key_down and not self.left_key_down:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        """Викликається при натисканні клавіші."""

        # Прижок
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

        # Вліво
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_key_down = True
            self.update_player_speed()

        # Вправо
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_key_down = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Викликається при відпусканні клавіші."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_key_down = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_key_down = False
            self.update_player_speed()

    def center_camera_to_player(self):
        # Знаходимо, де знаходиться гравець, потім обчислюємо нижній лівий кут від цього
        screen_center_x = self.player_sprite.center_x - (self.camera_sprites.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera_sprites.viewport_height / 2)

        # Встановлюємо деякі обмеження на те, наскільки далеко ми можемо прокручувати
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        # Ось наш центр, переходимо до нього
        player_centered = screen_center_x, screen_center_y
        self.camera_sprites.move_to(player_centered)

    def on_update(self, delta_time):
        """Рух та логіка гри"""

        # Рух гравця за допомогою фізичного двигуна
        self.physics_engine.update()

        # Перевірка, чи ми попали в якусь монету
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )

        # Проходимося по кожній монеті, яку ми попали (якщо є) і видаляємо її
        for coin in coin_hit_list:
            # Видаляємо монету
            coin.remove_from_sprite_lists()
            # Додаємо одиницю до рахунку
            self.score += 1

        # Позиціонування камери
        self.center_camera_to_player()

    def on_resize(self, width, height):
        """ Зміна розміру вікна """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    """Основна функція"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
