# ******************************************************************************
#
# cs-hello-world, python hello world project
#
# Copyright 2024 Jeremy A Gray <grayj2@wcslive.com>.
#
# All rights reserved.
#
# ******************************************************************************

"""Hello tests."""

import hello


def test_hello_world_prints_hello_world(capsys):
    """Should print 'Hello, world!'"""
    hello.hello_world()
    actual = capsys.readouterr().out.strip()
    expected = "Hello, world!"

    assert actual == expected


def test_hello_prints_hello_world(capsys):
    """Should print 'Hello, world!'"""
    hello.hello()
    actual = capsys.readouterr().out.strip()
    expected = "Hello, world!"

    assert actual == expected


def test_prints_hello_larry(capsys):
    """Should hello Larry."""
    hello.hello("Larry")
    actual = capsys.readouterr().out.strip()
    expected = "Hello, Larry!"

    assert actual == expected


def test_prints_hello_moe(capsys):
    """Should hello Moe."""
    hello.hello("Moe")
    actual = capsys.readouterr().out.strip()
    expected = "Hello, Moe!"

    assert actual == expected


def test_prints_hello_curly(capsys):
    """Should hello Curly."""
    hello.hello("Curly")
    actual = capsys.readouterr().out.strip()
    expected = "Hello, Curly!"

    assert actual == expected


def test_prints_hello_shemp(capsys):
    """Should hello Shemp."""
    hello.hello("Shemp")
    actual = capsys.readouterr().out.strip()
    expected = "Hello, Shemp!"

    assert actual == expected
