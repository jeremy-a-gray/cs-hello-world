# ******************************************************************************
#
# cs-hello-world, python hello world project
#
# Copyright 2024 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# ******************************************************************************

"""Goodbye tests."""

import pytest

import hello


def test_prints_goodbye_world(capsys):
    """Should print 'Goodbye, world!'"""
    hello.goodbye()
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, world!"

    assert actual == expected


@pytest.mark.parametrize(
    "msg",
    [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ],
)
def test_prints_goodbye_planets(msg, capsys):
    """Should goodbye the planets."""
    hello.goodbye(msg)
    actual = capsys.readouterr().out.strip()
    expected = msg

    assert actual == expected


@pytest.mark.parametrize(
    "msg",
    [
        "Larry",
        "Moe",
        "Curly",
        "Shemp",
    ],
)
def test_prints_goodbye_stooges(msg, capsys):
    """Should goodbye the stooges."""
    hello.goodbye(msg)
    actual = capsys.readouterr().out.strip()
    expected = msg

    assert actual == expected
