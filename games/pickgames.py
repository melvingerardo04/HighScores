import arcade
import arcade.gui

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class PlayerCharacter(arcade.Sprite):
    def __int__(self):
        super().__init__()


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.box = arcade.gui.UIBoxLayout()

        # For Start Button
        self.start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.box.add(self.start_button.with_space_around(bottom=20))

        # For Settings Button
        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.box.add(settings_button.with_space_around(bottom=20))

        # For Quit Button
        quit_button = QuitButton(text="Quit", width=200)
        self.box.add(quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box)
        )
        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        self.start_button.on_click = self.on_click_start

    def setup(self):
        self.player_list = arcade.SpriteList()
        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_click_start(self, event):
        self.box.clear()
        arcade.set_background_color(arcade.color.AMAZON)


class Game(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_list = None
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.WHITE)
        self.player_list.draw()



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    if window.start_button:
        window = Game()
        window.setup()

    arcade.run()


if __name__ == "__main__":
    main()