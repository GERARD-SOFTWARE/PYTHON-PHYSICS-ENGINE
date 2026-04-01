import math
import tkinter as tk

window = tk.Tk()
window_height = 400
window_width = 400
window.geometry(f"{window_width}x{window_height}")

def on_window_resize(event):
    global window_width, window_height
    window_width = event.width
    window_height = event.height

window.bind("<Configure>", on_window_resize) 

canvas = tk.Canvas(window, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

gravity = 0.3

# class Object:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

class Ball(object):
    def __init__(self, radius, x, y):
        balls.append(self)
        self.radius = radius
        self.x = x
        self.y = y
        self.y_velocity = 0
        self.x_velocity = 0

    def coordinate_update(self):
        self.y_velocity += gravity
        self.y += self.y_velocity
        # self.x_velocity += gravity
        # self.x += self.y_velocity

        if (self.y - self.radius) <= 0:
            overshoot = 0 - (self.y - self.radius)
            self.y = (0 + self.radius) + overshoot
            self.y_velocity = -self.y_velocity
        if (self.y + self.radius) >= window_height:
            overshoot = (self.y + self.radius) - window_height
            print(overshoot)
            self.y = (window_height - self.radius) - overshoot
            self.y_velocity = -self.y_velocity
        # if (self.x - self.radius) <= 0:
        #     overshoot = 0 - (self.x - self.radius)
        #     self.x = (0 + self.radius) + overshoot
        #     self.x_velocity = -self.x_velocity
        # if (self.x + self.radius) >= window_height:
        #     overshoot = (self.x + self.radius) - window_height
        #     print(overshoot)
        #     self.x = (window_height - self.radius) - overshoot
        #     self.x_velocity = -self.x_velocity

balls = []
ball1 = Ball(25, 100, 200)
ball2 = Ball(25, 200, 100)
ball3 = Ball(25, 300, 400)
ball4 = Ball(25, 400, 300)

def update_all():
    canvas.delete("all")
    for ball in balls:
        ball.coordinate_update()
        canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, 
                           ball.x + ball.radius, ball.y + ball.radius, 
                           fill="white")
    window.after(16, update_all)

print(balls)
update_all()

window.mainloop()