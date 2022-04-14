input.onButtonPressed(Button.AB, function () {
    mins = 0
    pump.stop(Pump.LEFT)
    music.playTone(523, music.beat(BeatFraction.Whole))
    music.playTone(587, music.beat(BeatFraction.Whole))
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(698, music.beat(BeatFraction.Whole))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.playTone(784, music.beat(BeatFraction.Whole))
    music.playTone(698, music.beat(BeatFraction.Whole))
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(587, music.beat(BeatFraction.Whole))
    music.playTone(523, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.B, function () {
    if (mins < 6) {
        mins += 1
    } else {
        mins = 0
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showLeds(`
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        `)
})
let mins = 0
mins = 0
basic.showLeds(`
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    `)
basic.forever(function () {
    if (mins == 1) {
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            . # # # .
            `)
    }
    if (mins == 2) {
        basic.showLeds(`
            . # # # .
            . . . # .
            . # # # .
            . # . . .
            . # # # .
            `)
    }
    if (mins == 3) {
        basic.showLeds(`
            . # # # .
            . . . # .
            . . # . .
            . . . # .
            . # # # .
            `)
    }
    if (mins == 4) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . # # # .
            . . . # .
            . . . # .
            `)
    }
    if (mins == 5) {
        basic.showLeds(`
            . # # # .
            . # . . .
            . # # . .
            . . . # .
            . # # # .
            `)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        music.playMelody("C D C D E - - - ", 199)
        if (mins == 1) {
            pump.startDuration(Pump.LEFT, 100, 60)
            music.playTone(523, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(523, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
                `)
        } else if (mins == 2) {
            pump.startDuration(Pump.LEFT, 100, 120)
            music.playTone(523, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(523, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
                `)
        } else if (mins == 3) {
            pump.startDuration(Pump.LEFT, 100, 180)
            music.playTone(523, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(523, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
                `)
        } else if (mins == 4) {
            pump.startDuration(Pump.LEFT, 100, 240)
            music.playTone(523, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(523, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
                `)
        } else if (mins == 5) {
            pump.startDuration(Pump.LEFT, 100, 300)
            music.playTone(523, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(784, music.beat(BeatFraction.Whole))
            music.playTone(698, music.beat(BeatFraction.Whole))
            music.playTone(659, music.beat(BeatFraction.Whole))
            music.playTone(587, music.beat(BeatFraction.Whole))
            music.playTone(523, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
                `)
        } else {
        	
        }
    }
})
