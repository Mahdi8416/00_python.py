# A clock whose hands instead of lines, a sequence of time displays that time.

from tkinter import *
import math
import time
import pygame

pygame.mixer.init()

try:
    tick_sound = pygame.mixer.Sound("D:\\clock_tiktok_4.mp3")
except pygame.error as e:
    print(f"Error loading sound: {e}")

window = Tk()
window.title("Classic Clock")

window.resizable(False, False)
window.minsize(900, 650)
window.maxsize(900, 650)

window_width = 900
window_height = 650
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(background="black")
BACKGROUND_COLOR = "#1e1e1e"
CLOCK_COLOR = "#d9d9d9"

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=window_height, width=window_width)
canvas.pack()

circle_radius = 290
center_x = window_width / 2
center_y = window_height / 2
canvas.create_oval(center_x - circle_radius, center_y - circle_radius,
                   center_x + circle_radius, center_y + circle_radius,
                   outline="black", width=3, fill=CLOCK_COLOR)


def calculate_position(angle, radius):
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y - radius * math.sin(math.radians(angle))
    return x, y


def tik_tok_sound():
    try:
        tick_sound.stop()
        tick_sound.play()
    except Exception as e:
        print(f"Error playing sound: {e}")


def draw_numbers():
    numbers = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

    positions = {
        "12": 90, "1": 60, "2": 30, "3": 0, "4": 330, "5": 300, "6": 270, "7": 240,
        "8": 210, "9": 180, "10": 150, "11": 120
    }

    for number, angle in positions.items():
        x, y = calculate_position(angle, circle_radius - 30)
        canvas.create_text(x, y, text=number, font=("Arial", 24, "bold"), fill="black")


draw_numbers()

canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black", outline="black")


def draw_time_numbers():
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec
    am_pm = time.strftime("%p")

    hour_angle = 90 - (hour * 30 + (minute / 2))
    minute_angle = 90 - (minute * 6)
    second_angle = 90 - (second * 6)

    canvas.delete("time_numbers")
    canvas.delete("am_pm")

    # hour hand
    for i in range(150, 300, 30):
        x_hour, y_hour = calculate_position(hour_angle, circle_radius - i)
        canvas.create_text(x_hour, y_hour, text=str(hour), font=("Arial", 26, "bold"), fill="red", tags="time_numbers")

    # minute hand
    for i in range(90, 300, 30):
        x_minute, y_minute = calculate_position(minute_angle, circle_radius - i)
        canvas.create_text(x_minute, y_minute, text=str(minute), font=("Arial", 24, "bold"), fill="#4da6ff",
                           tags="time_numbers")

    # second hand
    for i in range(70, 300, 30):
        x_second, y_second = calculate_position(second_angle, circle_radius - i)
        canvas.create_text(x_second, y_second, text=str(second), font=("Arial", 23, "bold"), fill="#ffd700",
                           tags="time_numbers")

    # am_pm
    canvas.create_text(center_x, center_y - circle_radius - 15, text=am_pm, font=("Vazir", 12, "bold"), fill="white",
                       tags="am_pm")

    tik_tok_sound()
    window.after(1000, draw_time_numbers)


draw_time_numbers()

window.mainloop()
