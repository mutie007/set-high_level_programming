#!/usr/bin/python3
"""Defines a LockedClass that restricts dynamic attribute creation."""


class LockedClass:
    """Represents a class that only allows the first_name attribute."""

    __slots__ = ["first_name"]
