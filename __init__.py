# SPDX-FileCopyrightText: Jose David Montoya
#
# SPDX-License-Identifier: MIT

"""
Color helper functions and styles
"""


def get_hex(color: str) -> int:
    """Function to convert Color styles to HEX
    :param str color: string representation of Hex color"""
    return int(color[1:], 16)
