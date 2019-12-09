# (c) 2019 Nokia
#
# Licensed under the BSD 3 Clause license
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
---
author: nokia
terminal: sros
short_description: CLI shell support for Nokia SR OS devices (classic-cli and md-cli)
version_added: "2.9"
"""

import re

from ansible.plugins.terminal import TerminalBase
from ansible.errors import AnsibleConnectionFailure


class TerminalModule(TerminalBase):

    terminal_stdout_re = [
        re.compile(br"\r?\n\r?\n\!?\*?(\((ex|gl|pr|ro)\))?\[.*\]\r?\n[ABCD]\:\S+\@\S+\#\s"),
        re.compile(br"\r?\n\*?[ABCD]:[\w\-\.\>]+\#\s")
    ]

    terminal_stderr_re = [
        re.compile(br"[\r\n]Error: .*[\r\n]+"),
        re.compile(br"[\r\n](MINOR|MAJOR|CRITICAL): .*[\r\n]+")
    ]

    def on_open_shell(self):
        try:
            prompt = self._get_prompt().strip()
            if b'\n' in prompt:
                # node is running md-cli
                self._exec_cli_command(b'environment more false')
                self._exec_cli_command(b'//environment no more')
            else:
                # node is running classic-cli
                self._exec_cli_command(b'environment no more')

        except AnsibleConnectionFailure:
            raise AnsibleConnectionFailure('unable to set terminal parameters')
