#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(ob):
    """Return a list of an object's available attributes."""
    return (dir(ob))
