import math
import turtle


def da_giac(t, ban_kinh, so_canh):
    # Vẽ đa giác đều nội tiếp đường tròn bán kính ban_kinh, tâm là vị trí hiện tại
    x, y = t.position()
    huong = t.heading()
    t.penup()
    t.forward(ban_kinh)
    t.left(90 + 180 / so_canh)
    t.pendown()
    canh = 2 * ban_kinh * math.sin(math.pi / so_canh)
    for _ in range(so_canh):
        t.forward(canh)
        t.left(360 / so_canh)
    # Nhấc bút, đưa về tâm và hướng cũ để hình sau không bị lem nét
    t.penup()
    t.goto(x, y)
    t.setheading(huong)


def hoa_tiet(t, ban_kinh, so_canh_hoa):
    # "Khối tự tạo" nhận 2 tham số: bán kính và số cánh hoa
    for _ in range(so_canh_hoa):
        da_giac(t, ban_kinh, 6)
        t.left(360 / so_canh_hoa)


def main():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    for ban_kinh in range(40, 161, 40):
        hoa_tiet(t, ban_kinh, 12)
    turtle.done()


if __name__ == "__main__":
    main()
