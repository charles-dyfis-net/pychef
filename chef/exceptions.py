# Exception hierarchy for chef
# Copyright (c) 2010 Noah Kantrowitz <noah@coderanger.net>

class ChefError(Exception):
    """Top-level Chef error."""

class ChefServerError(ChefError):
    """An error from a Chef server. May include a HTTP response code."""
    def __init__(self, message, code=None):
        ChefError.__init__(self, message)
        self.code = code
        
