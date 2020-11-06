hour = 0
minute = 0




def on_forever():
    global hour, minute
    pause(60000)
    if minute < 59:
        minute += 1
    else:
        minute = 0
        if hour < 23:
            hour += 1
        else:
            hour = 0
basic.forever(on_forever)


def on_gesture_shake():
    global hour, minute
    basic.show_string(str(hour) + ":" + str(minute))
input.on_gesture(Gesture.Shake, on_gesture_shake)


def on_button_pressed_a():
    global hour

    if hour < 23:
        hour += 1
    else:
        hour = 0
    basic.show_number(hour)
    pause(300)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    global minute

    if minute < 59:
        minute += 1
    else:
        minute = 0
    basic.show_number(minute)
    pause(300)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)