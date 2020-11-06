let hour = 0
let minute = 0
basic.forever(function on_forever() {
    
    pause(60000)
    if (minute < 59) {
        minute += 1
    } else {
        minute = 0
        if (hour < 23) {
            hour += 1
        } else {
            hour = 0
        }
        
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    basic.showString("" + hour + ":" + ("" + minute))
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (hour < 23) {
        hour += 1
    } else {
        hour = 0
    }
    
    basic.showNumber(hour)
    pause(300)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (minute < 59) {
        minute += 1
    } else {
        minute = 0
    }
    
    basic.showNumber(minute)
    pause(300)
    basic.clearScreen()
})
