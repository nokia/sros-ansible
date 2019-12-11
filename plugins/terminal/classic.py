# (c) 2019 Nokia
#
# Licensed under the BSD 3 Clause license
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
---
author: nokia
terminal: nokia.sros.classic
short_description: Classic-CLI terminal support for Nokia SR OS devices
version_added: "2.9"
"""

import re

from ansible.plugins.terminal import TerminalBase
from ansible.errors import AnsibleConnectionFailure


class TerminalModule(TerminalBase):

    terminal_stdout_re = [
        re.compile(br"\r?\n\*?[ABCD]:[\w\-\.\>]+[#\$]\s")
    ]

    terminal_stderr_re = [
        re.compile(br"[\r\n]Error: .*[\r\n]+")
    ]

    def on_open_shell(self):
        try:
            self._exec_cli_command(b'environment no more')

        except AnsibleConnectionFailure:
            raise AnsibleConnectionFailure('unable to set terminal parameters')
