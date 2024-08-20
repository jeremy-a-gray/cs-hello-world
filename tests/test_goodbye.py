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

import hello


def test_goodbye_world_prints_goodbye_world(capsys):
    """Should print 'Goodbye, world!'"""
    hello.goodbye_world()
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, world!"

    assert actual == expected


def test_goodbye_prints_goodbye_world(capsys):
    """Should print 'Goodbye, world!'"""
    hello.goodbye()
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, world!"

    assert actual == expected


def test_prints_goodbye_larry(capsys):
    """Should goodbye Larry."""
    hello.goodbye("Larry")
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, Larry!"

    assert actual == expected


def test_prints_goodbye_moe(capsys):
    """Should goodbye Moe."""
    hello.goodbye("Moe")
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, Moe!"

    assert actual == expected


def test_prints_goodbye_curly(capsys):
    """Should goodbye Curly."""
    hello.goodbye("Curly")
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, Curly!"

    assert actual == expected


def test_prints_goodbye_shemp(capsys):
    """Should goodbye Shemp."""
    hello.goodbye("Shemp")
    actual = capsys.readouterr().out.strip()
    expected = "Goodbye, Shemp!"

    assert actual == expected
