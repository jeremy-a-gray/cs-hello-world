# ******************************************************************************
#
# cs-hello-world, python hello world project
#
# Copyright 2024 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# ******************************************************************************

"""Hello, world! tests."""

# import pytest

import hello


def test_prints_hello_world(capsys):
    """Should print 'Hello, world!'"""
    hello.hello()
    actual = capsys.readouterr().out.strip()
    expected = "Hello, world!"

    assert actual == expected


# @pytest.mark.parametrize(
#     "msg",
#     [
#         "Mercury",
#         "Venus",
#         "Earth",
#         "Mars",
#         "Jupiter",
#         "Saturn",
#         "Uranus",
#         "Neptune",
#     ],
# )
# def test_prints_hello_planets(msg, capsys):
#     """Should hello the planets."""
#     hello.hello(msg)
#     actual = capsys.readouterr().out.strip()
#     expected = msg

#     assert actual == expected


# @pytest.mark.parametrize(
#     "msg",
#     [
#         "Larry",
#         "Moe",
#         "Curly",
#         "Shemp",
#     ],
# )
# def test_prints_hello_stooges(msg, capsys):
#     """Should hello the stooges."""
#     hello.hello(msg)
#     actual = capsys.readouterr().out.strip()
#     expected = msg

#     assert actual == expected
