import math
import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# ---------------------------------------------------------
# SETUP MAP & ENVIRONMENT
# ---------------------------------------------------------
window.title = "Python Hero Shooter (OW Style - Q Key Menu)"
window.borderless = False
window.fps_counter.enabled = True

ground = Entity(model="plane", scale=(100, 1, 100), color=color.dark_gray, collider="box")

for i in range(15):
    Entity(
        model="cube",
        scale=(random.uniform(2, 6), random.uniform(3, 8), random.uniform(2, 6)),
        position=(random.uniform(-40, 40), 0, random.uniform(-40, 40)),
        color=color.gray,
        collider="box",
    )

def play_sfx(sound_name, pitch=1.0, volume=0.5):
    try:
        Audio(sound_name, pitch=pitch, volume=volume, auto_destroy=True)
    except:
        pass


# ---------------------------------------------------------
# ENEMY AI CLASS
# ---------------------------------------------------------
class EnemyAI(Entity):
    def __init__(self, position):
        super().__init__(
            model="capsule",
            color=color.red,
            scale=(1.5, 2.5, 1.5),
            position=position,
            collider="box"
        )
        self.hp = 200
        self.max_hp = 200
        self.shoot_cooldown = random.uniform(1.0, 2.5)

    def update(self):
        # หากเกมถูก Pause หรืออยู่ในเมนู AI จะหยุดทำงาน
        if not player or not player.enabled or pause_menu_parent.enabled:
            return

        dist = distance(self.position, player.position)

        if dist < 35:
            self.look_at(player.position)
            self.shoot_cooldown -= time.dt
            if self.shoot_cooldown <= 0:
                self.shoot_at_player()
                self.shoot_cooldown = random.uniform(1.5, 2.5)

    def shoot_at_player(self):
        play_sfx("enemy_shoot.wav", pitch=0.8, volume=0.3)

        bullet = Entity(
            model="sphere",
            color=color.orange,
            scale=0.4,
            position=self.position + Vec3(0, 1, 0),
            collider="sphere"
        )
        bullet.look_at(player.position + Vec3(0, 1, 0))
        bullet.animate_position(
            bullet.position + bullet.forward * 40,
            duration=1.2,
            curve=curve.linear
        )
        invoke(self.check_bullet_hit, bullet, delay=0.2)
        destroy(bullet, delay=1.2)

    def check_bullet_hit(self, bullet):
        if not bullet or not player or not player.enabled:
            return
        if distance(bullet.position, player.position) < 2.0:
            player.take_damage(20)
            destroy(bullet)
        elif bullet.enabled:
            invoke(self.check_bullet_hit, bullet, delay=0.1)


enemies = []
def spawn_enemies():
    global enemies
    for e in enemies:
        destroy(e)
    enemies.clear()
    
    for i in range(5):
        enemy = EnemyAI(position=(random.uniform(-25, 25), 1.25, random.uniform(10, 35)))
        enemies.append(enemy)


# ---------------------------------------------------------
# PLAYER CONTROLLER
# ---------------------------------------------------------
class HeroPlayer(FirstPersonController):
    def __init__(self, hero_type="DPS"):
        super().__init__()
        self.hero_type = hero_type
        self.speed = 12
        self.hp = 200
        self.max_hp = 200

        self.skill_cd = 0
        self.ult_cd = 0
        self.ult_charge = 0

        self.max_ammo = 30
        self.current_ammo = 30
        self.is_reloading = False
        self.reload_time = 1.5
        self.reload_timer = 0

        self.weapon = Entity(
            parent=camera.ui,
            model="cube",
            scale=(0.2, 0.2, 0.6),
            position=(0.5, -0.4, 0.8),
            color=color.gold,
        )

        self.setup_hero_stats()

    def setup_hero_stats(self):
        if self.hero_type == "Tracer":
            self.speed = 18
            self.hp = 150
            self.max_hp = 150
            self.max_ammo = 40
            self.reload_time = 1.0
            self.weapon.color = color.orange
        elif self.hero_type == "Reinhardt":
            self.speed = 9
            self.hp = 500
            self.max_hp = 500
            self.max_ammo = 999
            self.reload_time = 0.1
            self.weapon.color = color.azure
        elif self.hero_type == "Pharah":
            self.speed = 12
            self.hp = 200
            self.max_hp = 200
            self.max_ammo = 6
            self.reload_time = 2.0
            self.weapon.color = color.magenta
            
        self.current_ammo = self.max_ammo

    def update(self):
        # เมื่อเปิด Pause Menu ห้ามหมุนกล้องหรือเดิน
        if pause_menu_parent.enabled:
            return

        super().update()

        if self.skill_cd > 0:
            self.skill_cd -= time.dt
        if self.ult_cd > 0:
            self.ult_cd -= time.dt

        if self.is_reloading:
            self.reload_timer -= time.dt
            if self.reload_timer <= 0:
                self.current_ammo = self.max_ammo
                self.is_reloading = False
                play_sfx("reload_finish.wav", pitch=1.1, volume=0.5)

        if self.ult_charge < 100:
            self.ult_charge += time.dt * 1.5

        hp_text.text = f"HP: {int(self.hp)} / {self.max_hp}"
        cd_text.text = f"Skill (E): {'READY' if self.skill_cd <= 0 else f'{int(self.skill_cd)}s'}"
        ult_text.text = f"Ultimate (F): {int(self.ult_charge)}% {'[READY]' if self.ult_charge >= 100 else ''}"
        
        if self.hero_type == "Reinhardt":
            ammo_text.text = "Ammo: Melee (∞)"
        elif self.is_reloading:
            ammo_text.text = "Ammo: RELOADING..."
        else:
            ammo_text.text = f"Ammo (R): {self.current_ammo} / {self.max_ammo}"

    def input(self, key):
        # ปุ่ม Q เปิด/ปิด Pause Menu
        if key == "q":
            toggle_pause_menu()
            return

        # ถ้าติด Pause Menu ห้ามกดรับ Input ยิงหรือใช้สกิล
        if pause_menu_parent.enabled:
            return

        super().input(key)

        if key == "left mouse down":
            self.attack()

        if key == "r" and not self.is_reloading and self.current_ammo < self.max_ammo and self.hero_type != "Reinhardt":
            self.start_reload()

        if key == "e" and self.skill_cd <= 0:
            self.use_skill()

        # เปลี่ยนปุ่ม Ultimate เป็น F แทน Q
        if key == "f" and self.ult_charge >= 100:
            self.use_ult()

    def start_reload(self):
        self.is_reloading = True
        self.reload_timer = self.reload_time
        play_sfx("reload_start.wav", pitch=1.0, volume=0.6)

    def attack(self):
        if self.is_reloading:
            return

        if self.current_ammo <= 0 and self.hero_type != "Reinhardt":
            play_sfx("dry_fire.wav", pitch=1.5, volume=0.3)
            self.start_reload()
            return

        if self.hero_type != "Reinhardt":
            self.current_ammo -= 1
            play_sfx("shoot.wav", pitch=random.uniform(0.95, 1.05), volume=0.5)
        else:
            play_sfx("swing.wav", pitch=0.8, volume=0.7)

        self.weapon.position = (0.5, -0.38, 0.7)
        invoke(setattr, self.weapon, "position", (0.5, -0.4, 0.8), delay=0.05)

        bullet_ray = raycast(camera.world_position, camera.forward, distance=60, ignore=(self,))
        if bullet_ray.hit:
            for enemy in enemies:
                if bullet_ray.entity == enemy:
                    play_sfx("hitmarker.wav", pitch=1.2, volume=0.8)

                    damage = 35 if self.hero_type != "Reinhardt" else 80
                    enemy.hp -= damage
                    enemy.color = color.yellow
                    invoke(setattr, enemy, "color", color.red, delay=0.1)

                    self.ult_charge = min(100, self.ult_charge + 6)

                    if enemy.hp <= 0:
                        play_sfx("kill.wav", pitch=1.0, volume=0.8)
                        enemy.position = (random.uniform(-25, 25), 1.25, random.uniform(10, 35))
                        enemy.hp = 200

        if self.current_ammo <= 0 and self.hero_type != "Reinhardt":
            self.start_reload()

    def take_damage(self, amount):
        self.hp -= amount
        play_sfx("hurt.wav", pitch=1.0, volume=0.7)

        damage_overlay.alpha = 0.3
        invoke(setattr, damage_overlay, "alpha", 0, delay=0.15)

        if self.hp <= 0:
            self.die()

    def die(self):
        play_sfx("player_death.wav", pitch=0.9, volume=0.9)
        self.enabled = False
        game_over_parent.enabled = True
        mouse.locked = False

    def use_skill(self):
        if self.hero_type == "Tracer":
            play_sfx("blink.wav", pitch=1.2, volume=0.7)
            self.position += self.forward * 10
            self.skill_cd = 3.0
        elif self.hero_type == "Reinhardt":
            play_sfx("shield_up.wav", pitch=0.9, volume=0.8)
            shield = Entity(
                parent=self,
                model="cube",
                scale=(4, 3, 0.2),
                position=(0, 0, 2),
                color=color.cyan,
                alpha=0.5,
            )
            destroy(shield, delay=4.0)
            self.skill_cd = 8.0
        elif self.hero_type == "Pharah":
            play_sfx("jetpack.wav", pitch=1.1, volume=0.8)
            self.y += 12
            self.skill_cd = 5.0

    def use_ult(self):
        self.ult_charge = 0
        self.ult_cd = 10.0
        play_sfx("ult_activate.wav", pitch=1.0, volume=1.0)

        if self.hero_type == "Tracer":
            for e in enemies:
                if distance(self.position, e.position) < 12:
                    e.hp -= 180
        elif self.hero_type == "Pharah":
            for e in enemies:
                e.hp -= 200
        elif self.hero_type == "Reinhardt":
            for e in enemies:
                if distance(self.position, e.position) < 15:
                    e.y = 0.5
                    invoke(setattr, e, "y", 1.25, delay=2.5)


# ---------------------------------------------------------
# UI & MENUS
# ---------------------------------------------------------
crosshair = Entity(parent=camera.ui, model="quad", color=color.white, scale=(0.01, 0.01))

hp_text = Text(text="", position=(-0.85, 0.45), scale=1.4, color=color.green)
ammo_text = Text(text="", position=(-0.85, 0.39), scale=1.3, color=color.yellow)
cd_text = Text(text="", position=(-0.85, 0.33), scale=1.2, color=color.white)
ult_text = Text(text="", position=(-0.85, 0.27), scale=1.2, color=color.cyan)

damage_overlay = Entity(parent=camera.ui, model="quad", color=color.red, scale=(2, 2), alpha=0)

player = None

# ---------------------------------------------------------
# PAUSE MENU & TOGGLE SYSTEM
# ---------------------------------------------------------
pause_menu_parent = Entity(parent=camera.ui, enabled=False)

# พื้นหลังเมนูโปร่งแสง
Entity(parent=pause_menu_parent, model="quad", color=color.black66, scale=(2, 2))

Text(parent=pause_menu_parent, text="GAME PAUSED", position=(-0.16, 0.25), scale=2.5, color=color.yellow)

btn_resume = Button(parent=pause_menu_parent, text="Resume Game (Press Q)", color=color.azure, scale=(0.4, 0.08), position=(0, 0.05))
btn_change_hero = Button(parent=pause_menu_parent, text="Change Hero", color=color.orange, scale=(0.4, 0.08), position=(0, -0.06))
btn_quit = Button(parent=pause_menu_parent, text="Quit Game", color=color.red, scale=(0.4, 0.08), position=(0, -0.17))

def resume_game():
    pause_menu_parent.enabled = False
    if player and player.enabled:
        mouse.locked = True

def open_hero_select():
    pause_menu_parent.enabled = False
    menu_parent.enabled = True
    if player:
        player.enabled = False
    mouse.locked = False

btn_resume.on_click = resume_game
btn_change_hero.on_click = open_hero_select
btn_quit.on_click = application.quit

def toggle_pause_menu():
    if not player or menu_parent.enabled or game_over_parent.enabled:
        return
        
    pause_menu_parent.enabled = not pause_menu_parent.enabled
    mouse.locked = not pause_menu_parent.enabled


# ---------------------------------------------------------
# START & GAME OVER MENUS
# ---------------------------------------------------------
def select_hero(hero_name):
    global player
    if player:
        destroy(player)
        
    menu_parent.enabled = False
    game_over_parent.enabled = False
    pause_menu_parent.enabled = False
    mouse.locked = True
    
    play_sfx("select_hero.wav", pitch=1.0, volume=0.7)
    spawn_enemies()
    player = HeroPlayer(hero_type=hero_name)


menu_parent = Entity(parent=camera.ui)
Text(parent=menu_parent, text="CHOOSE YOUR HERO", position=(-0.22, 0.3), scale=2, color=color.yellow)

btn_tracer = Button(parent=menu_parent, text="Tracer (High Speed & 40 Ammo)", color=color.orange, scale=(0.45, 0.08), position=(0, 0.1))
btn_rein = Button(parent=menu_parent, text="Reinhardt (Tank & Infinite Melee)", color=color.azure, scale=(0.45, 0.08), position=(0, -0.02))
btn_pharah = Button(parent=menu_parent, text="Pharah (Jump Boost & 6 Rockets)", color=color.magenta, scale=(0.45, 0.08), position=(0, -0.14))

btn_tracer.on_click = lambda: select_hero("Tracer")
btn_rein.on_click = lambda: select_hero("Reinhardt")
btn_pharah.on_click = lambda: select_hero("Pharah")

game_over_parent = Entity(parent=camera.ui, enabled=False)
Text(parent=game_over_parent, text="YOU DIED", position=(-0.12, 0.2), scale=3, color=color.red)
btn_restart = Button(parent=game_over_parent, text="Back to Hero Selection", color=color.dark_gray, scale=(0.4, 0.1), position=(0, -0.05))

def return_to_menu():
    game_over_parent.enabled = False
    menu_parent.enabled = True
    mouse.locked = False

btn_restart.on_click = return_to_menu

mouse.locked = False
app.run()