"""Collect all default values for autotests."""


class Defaults:
    """Collect fixed data for autotests."""

    title = 'Фильтр для гласных'
    input_text = """Сменялись в детстве радугой дожди,
Сияньем солнца — сумрачные тени.
Но в зрелости не требуй и не жди
Таких простых и скорых утешений.

Самуил Яковлевич Маршак"""
    output_text = 'Здесь будет текст после фильтрации!'

    # most popular tablet resolution according to statcounter (06/2022)
    tablet_width = 768
    tablet_height = 1024

    # average tablet resolution based on statcounter rating (06/2022)
    mobile_width = 390
    mobile_height = 800
