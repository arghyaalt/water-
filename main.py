def on_button_pressed_a():
    music.play_melody("C D C D E - - - ", 199)
    if mins == 1:
        pump.start_duration(Pump.LEFT, 100, 60)
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(784, music.beat(BeatFraction.WHOLE))
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        music.play_tone(659, music.beat(BeatFraction.WHOLE))
        music.play_tone(587, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        basic.show_leds("""
            . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
                        . . . . .
        """)
    else:
        if mins == 2:
            pump.start_duration(Pump.LEFT, 100, 120)
            music.play_tone(523, music.beat(BeatFraction.WHOLE))
            music.play_tone(587, music.beat(BeatFraction.WHOLE))
            music.play_tone(659, music.beat(BeatFraction.WHOLE))
            music.play_tone(698, music.beat(BeatFraction.WHOLE))
            music.play_tone(784, music.beat(BeatFraction.WHOLE))
            music.play_tone(784, music.beat(BeatFraction.WHOLE))
            music.play_tone(698, music.beat(BeatFraction.WHOLE))
            music.play_tone(659, music.beat(BeatFraction.WHOLE))
            music.play_tone(587, music.beat(BeatFraction.WHOLE))
            music.play_tone(523, music.beat(BeatFraction.WHOLE))
            basic.show_leds("""
                . # . # .
                                . . . . .
                                # . . . #
                                . # # # .
                                . . . . .
            """)
        else:
            if mins == 3:
                pump.start_duration(Pump.LEFT, 100, 180)
                music.play_tone(523, music.beat(BeatFraction.WHOLE))
                music.play_tone(587, music.beat(BeatFraction.WHOLE))
                music.play_tone(659, music.beat(BeatFraction.WHOLE))
                music.play_tone(698, music.beat(BeatFraction.WHOLE))
                music.play_tone(784, music.beat(BeatFraction.WHOLE))
                music.play_tone(784, music.beat(BeatFraction.WHOLE))
                music.play_tone(698, music.beat(BeatFraction.WHOLE))
                music.play_tone(659, music.beat(BeatFraction.WHOLE))
                music.play_tone(587, music.beat(BeatFraction.WHOLE))
                music.play_tone(523, music.beat(BeatFraction.WHOLE))
                basic.show_leds("""
                    . # . # .
                                        . . . . .
                                        # . . . #
                                        . # # # .
                                        . . . . .
                """)
            else:
                if mins == 4:
                    pump.start_duration(Pump.LEFT, 100, 240)
                    music.play_tone(523, music.beat(BeatFraction.WHOLE))
                    music.play_tone(587, music.beat(BeatFraction.WHOLE))
                    music.play_tone(659, music.beat(BeatFraction.WHOLE))
                    music.play_tone(698, music.beat(BeatFraction.WHOLE))
                    music.play_tone(784, music.beat(BeatFraction.WHOLE))
                    music.play_tone(784, music.beat(BeatFraction.WHOLE))
                    music.play_tone(698, music.beat(BeatFraction.WHOLE))
                    music.play_tone(659, music.beat(BeatFraction.WHOLE))
                    music.play_tone(587, music.beat(BeatFraction.WHOLE))
                    music.play_tone(523, music.beat(BeatFraction.WHOLE))
                    basic.show_leds("""
                        . # . # .
                                                . . . . .
                                                # . . . #
                                                . # # # .
                                                . . . . .
                    """)
                else:
                    if mins == 5:
                        pump.start_duration(Pump.LEFT, 100, 300)
                        music.play_tone(523, music.beat(BeatFraction.WHOLE))
                        music.play_tone(587, music.beat(BeatFraction.WHOLE))
                        music.play_tone(659, music.beat(BeatFraction.WHOLE))
                        music.play_tone(698, music.beat(BeatFraction.WHOLE))
                        music.play_tone(784, music.beat(BeatFraction.WHOLE))
                        music.play_tone(784, music.beat(BeatFraction.WHOLE))
                        music.play_tone(698, music.beat(BeatFraction.WHOLE))
                        music.play_tone(659, music.beat(BeatFraction.WHOLE))
                        music.play_tone(587, music.beat(BeatFraction.WHOLE))
                        music.play_tone(523, music.beat(BeatFraction.WHOLE))
                        basic.show_leds("""
                            . # . # .
                                                        . . . . .
                                                        # . . . #
                                                        . # # # .
                                                        . . . . .
                        """)
                    else:
                        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global mins
    mins = 0
    pump.stop(Pump.LEFT)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(698, music.beat(BeatFraction.WHOLE))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
    music.play_tone(698, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global mins
    if mins < 6:
        mins += 1
    else:
        mins = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_leds("""
        . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

mins = 0
mins = 0
basic.show_leds("""
    . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
""")

def on_forever():
    if mins == 1:
        basic.show_leds("""
            . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        . # # # .
        """)
    if mins == 2:
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . # # # .
                        . # . . .
                        . # # # .
        """)
    if mins == 3:
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . . # . .
                        . . . # .
                        . # # # .
        """)
    if mins == 4:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . # # # .
                        . . . # .
                        . . . # .
        """)
    if mins == 5:
        basic.show_leds("""
            . # # # .
                        . # . . .
                        . # # . .
                        . . . # .
                        . # # # .
        """)
basic.forever(on_forever)
