# -*- coding: utf-8 -*-

from . import models
from . import report
from . import wizard


def post_init_hook(env):
    """
    Update the account payment mode.
    """
    modes = env["account.payment.mode"].search(
        [("payment_type", "=", "inbound"), ("bank_account_link", "=", "fixed")]
    )
    modes.write({"donation": True})
