import microbit
from raylib.pyray import PyRay
from raylib.colors import * 

pyray = PyRay()

pyray.init_window(800, 600, "Microbit Raylib Test")

while not pyray.window_should_close():

    pyray.begin_drawing()
    pyray.clear_background([255,255,255])

    pyray.draw_text("Microbit data", 10, 10, 20, [255,0,0,255])
    pyray.draw_text("--------------", 10, 25, 20, [255,0,0,255])
    pyray.draw_text("Accelerometer values: " + str(microbit.accelerometer.get_values()), 10, 40, 20, [255,0,0,255])
    pyray.draw_text("Temperature: " + str(microbit.temperature()), 10, 70, 20, [255,0,0,255])
    
    
    pyray.end_drawing()   

    if microbit.pin0.is_touched():
        microbit.display.show("0")
        microbit.sleep(50)
        microbit.display.clear()
    elif microbit.pin1.is_touched():
        microbit.display.show("1")
        microbit.sleep(50)
        microbit.display.clear()
    
    if microbit.button_a.was_pressed():
        microbit.display.show("A")
        microbit.sleep(500)
        microbit.display.clear()
    elif microbit.button_b.was_pressed():
        microbit.display.show("B")
        microbit.sleep(500)
        microbit.display.clear()

pyray.close_window()
microbit.sleep(250)
