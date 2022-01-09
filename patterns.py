from blacklistparser import BlacklistParser

#
# Note: specific transforms do not mean much at this point (anymore), all available
# transformations are automatically applied and same results filtered
#

# Some patterns and number I found on the net or came up with, ymmv
PATTERNS = [
    """
    name rotor
    transform M
    x
    .x
    ..x
    """,
    """
    name box
    transform R
    missing 1
    xx
    xx
    xx
    """,
    """
    name box2
    xx
    xx
    """,
    """
    name line
    transform R
    xxx
    """,
    """
    name sequence over borders
    transform R, M, RM
    xxx....
    ....xxx
    """,
    """
    name sequence over borders-b
    transform R, M, RM
    xxx....
    .......
    ....xxx
    """,
    """
    name sequence over borders-c
    transform R, M, RM
    xxx....
    .......
    .......
    ....xxx
    """,
    """
    name sequence over borders-d
    transform R, M, RM
    xxx....
    .......
    .......
    .......
    ....xxx
    """,
    """
    name sequence over borders-e
    transform R, M, RM
    xxx....
    .......
    .......
    .......
    .......
    ....xxx
    """,
    """
    name sequence over borders-f
    transform R, M, RM
    xxx....
    .......
    .......
    .......
    .......
    ....xxx
    """,
    """
    name ring
    transform R
    missing 1
    .x.
    x.x
    x.x
    .x.
    """,
    """
    name pyramid-a
    transform R, L, F
    missing 1
    ..x
    .xxx
    x...x
    """,
    """
    name pyramid-b
    transform R, L, F
    missing 1
    .x
    xxx
    x.x
    """,
    """
    name pyramid-c
    transform R, L, F
    missing 1
    .x
    .x
    x.x
    x.x
    """,
    """
    name pyramid-d
    transform R, L, F
    missing 1
    ..x
    ..x.
    .x.x
    x...x
    """,
    """
    name pyramid-e
    transform R, L, F
    missing 1
    x.x.x
    .x.x.
    ..x..
    """,
    """
    name pisa
    transform R, M, RM
    missing 1
    ..x
    .xx
    xx.
    x..
    """,
    """
    name cross-a
    transform R, L, F
    missing 1
    .x
    xxx
    .x.
    .x.
    """,
    """
    name cross-b
    ...x...
    x..x..x
    ...x...
    """,
    """
    name cross-c
    missing 1
    ...x...
    .......
    x..x..x
    .......
    ...x...
    """,
    """
    name cross-d
    missing 1
    ..x..
    x.x.x
    ..x..
    """,
    """
    name snail-a
    transform R, M, RM
    missing 1
    .xxx
    xxx
    """,
    """
    name snail-b
    transform R, M, RM
    missing 1
    ...xxx
    xxx...
    """,
    """
    name stairs
    transform R, M, RM
    missing 1
    xx
    ..x..
    ...xx
    """,
    """
    name z
    transform R, M, RM
    xx...
    .....
    ...xx
    """,
    """
    name z-b
    transform R, M, RM
    xx..
    ....
    ..xx
    """,
    """
    name z-c
    transform R, M, RM
    xx..
    ..xx
    """,
    """
    name z-d
    transform R, M, RM
    xx.
    ...
    .xx
    """,
    """
    name u-a
    transform R, L, F
    missing 1
    x...x
    .....
    x...x
    .x.x.
    """,
    """
    name u-b
    transform R, L, F
    missing 1
    x...x
    x...x
    .x.x.
    """,
    """
    name u-c
    transform R, L, F
    missing 1
    x..x
    x..x
    .xx.
    """,
    """
    name u-d
    transform R, L, F
    missing 1
    x...x
    .....
    x...x
    .....
    .x.x.
    """,
    """
    name fish
    transform R, L, F
    missing 1
    x.x
    .x.
    x.x
    .x
    """,
    """
    name checked
    transform R, L, F, M, RM, LM
    missing 1
    ...x
    ..x.x
    .x...x
    x.....
    """,
    """
    name ruby
    transform R
    missing 1
    x.....x
    .......
    ...x...
    ...x...
    .......
    x.....x
    """,
    """
    name ruby-b
    transform R
    missing 1
    x.....x
    ...x...
    .......
    .......
    ...x...
    x.....x
    """,
    """
    name bus-a
    transform R
    missing 1
    x.x
    ...
    x.x
    ...
    x.x
    """,
    """
    name bus-b
    transform R
    missing 1
    x..x
    ....
    x..x
    ....
    x..x
    """,
    """
    name bus-c
    transform R
    missing 1
    x...x
    .....
    x...x
    .....
    x...x
    """,
    """
    name bus-d
    transform R
    missing 1
    x....x
    ......
    x....x
    ......
    x....x
    """,
    """
    name bus-e
    transform R
    missing 1
    x.....x
    .......
    x.....x
    .......
    x.....x
    """,
    """
    name c-a
    transform R, L, M
    missing 1
    .xx
    x..
    .xx
    """,
    """
    name c-b
    transform R, L, M
    missing 1
    .xx
    x..
    x..
    .xx
    """,
    """
    name s
    transform R, L, F
    .xx
    .x.
    xx.
    """,
    """
    name s big
    transform R, L, F, M, RM, LM
    missing 1
    .x.
    x..
    .x.
    ..x
    .x.
    x..
    """,
    """
    name battle-a
    transform R
    missing 1
    x.x
    x.x
    x.x
    """,
    """
    name battle-b
    transform R
    missing 1
    x..x
    x..x
    x..x
    """,
    """
    name battle-c
    transform R
    missing 1
    x...x
    x...x
    x...x
    """,
    """
    name battle-d
    transform R
    missing 1
    x....x
    x....x
    x....x
    """,
    """
    name battle-e
    transform R
    missing 1
    x.....x
    x.....x
    x.....x
    """,
    """
    name little check board
    transform R, M, RM
    x.x.
    .x.x
    """,
    """
    name x-a
    missing 1
    x..x
    .xx
    x..x
    """,
    """
    name x-b
    transform R
    missing 1
    x...x
    .x.x
    x...x
    """,
    """
    name x-c
    transform R
    missing 1
    x....x
    .x..x
    x....x
    """,
    """
    name x-d
    transform R
    missing 1
    x.....x
    .x...x
    x.....x
    """,
    """
    name pin-a
    missing 1
    x.x
    .x.
    x.x
    """,
    """
    name pin-b
    x...x
    ..x.
    x...x
    """,
    """
    name pin-c
    x...x
    .....
    ..x..
    .....
    x...x
    """,
    """
    name corners
    missing 1
    x.....x
    .......
    .......
    .......
    .......
    .......
    x.....x
    """,
    """
    name corner
    transform R, L, F
    xx
    x.
    """,
    """
    name corner wide
    transform R, L, F
    x.x
    ...
    x..
    """,
    """
    name corner full
    transform R, L, F
    xxx
    xx.
    x..
    """,
    """
    name parallel
    transform R, M, F, RM
    ..x..
    .x..x
    x..x.
    ..x..
    """,
    """
    name 10er Abstand-a
    numbers 1, 10, 20, 30, 40, 49
    missing 1
    """,
    """
    name 10er Abstand-b
    numbers 1, 11, 21, 31, 41, 49
    missing 1
    """,
    """
    name 10er Abstand-c
    numbers 2, 12, 22, 32, 42, 49
    missing 1
    """,
    """
    name 10er Abstand-d
    numbers 3, 13, 23, 33, 38, 49
    missing 1
    """,
    """
    name 10er Abstand-e
    numbers 4, 14, 24, 34, 44, 49
    missing 1
    """,
    """
    name 10er Abstand-f
    numbers 5, 15, 25, 35, 45, 49
    missing 1
    """,
    """
    name 5er Abstand
    numbers 5, 10, 15, 20, 25, 30
    missing 1
    """,
    """
    name 5er Abstand-b
    numbers 10, 15, 20, 25, 30, 35
    missing 1
    """,
    """
    name 5er Abstand-c
    numbers 15, 20, 25, 30, 35, 40
    missing 1
    """,
    """
    name 5er Abstand-d
    numbers 20, 25, 30, 35, 40, 45
    missing 1
    """,
    """
    name Pasch
    numbers 1, 11, 22, 33, 44, 49
    missing 2
    """,
    """
    name Erste Lottozahlen 1955
    numbers 13, 41, 3, 23, 12, 16
    """,
    """
    name Gewinn am Tag d dt Einheit
    numbers 13, 28, 35, 46, 48, 49
    """,
    """
    name Meistgezogene nummern lt. lottozahlenonline.de
    numbers 6, 32, 49, 26, 38, 31, 33
    missing 1
    """,
    """
    name Eurojackpott Rekord Juni 2018-a
    numbers 14, 19, 21, 30, 32, 4
    missing 1
    """,
    """
    name Eurojackpott Rekord Juni 2018-b
    numbers 14, 19, 21, 30, 32, 7
    missing 1
    """,
    """
    name lottostiftung.de max gewinn
    numbers 9, 10, 24, 28, 39, 42
    missing 1
    """,
    """
    name lottozahlen.de max gewinn 1
    numbers 28, 30, 31, 34, 41, 48
    missing 1
    """,
    """
    name lottozahlen.de max gewinn 2
    numbers 5, 13, 15, 26, 30, 44
    missing 1
    """,
    """
    name lottozahlen.de max gewinn 3
    numbers 5, 12, 13, 33, 38, 39
    missing 1
    """,
    """
    name lottozahlen.de max gewinn 4
    numbers 10, 14, 18, 24, 33, 44
    missing 1
    """,
    """
    name lottozahlen.de max gewinn 5
    numbers 2, 3, 15, 20, 31, 35
    missing 1
    """,
    """
    name Widerholter 6er
    numbers 15, 25, 27, 30, 42, 4
    missing 1
    """,
    """
    name Widerholter 5er
    numbers 2, 9, 14, 38, 40, 44
    missing 1
    """,
    """
    name lottoland.de erster dt. millionaer
    numbers 14, 26, 31, 40, 48, 49
    missing 1
    """,
    """
    name lottoland.de hoechster einzel
    numbers 31, 41, 48, 28, 30, 31
    missing 1
    """,
    """
    name lottoland.de hoechster jackpott
    numbers 9, 10, 24, 28, 39, 42
    missing 1
    """,
    """
    name lottoland.de hoechster einzel us
    numbers 4, 8, 19, 27, 34, 10
    missing 1
    """,
    """
    name lottoland.de hoechster jackpott us
    numbers 6, 7, 16, 23, 26, 4
    missing 1
    """,
    """
    name lottoland.de hoechste kombination
    numbers 38, 39, 43, 45, 46, 47
    missing 1
    """,
    """
    name lottoland.de hoechste kombination +1
    numbers 38, 39, 43, 45, 46, 48
    missing 1
    """,
    """
    name lottoland.de niederlande zuvor 1977
    numbers 9, 17, 18, 20, 29, 40
    missing 1
    """
]
