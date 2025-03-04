# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.cmd.common import arguments
from spack.cmd.compiler import compiler_list

description = "list available compilers"
section = "system"
level = "short"


def setup_parser(subparser):
    subparser.add_argument(
        "--scope", action=arguments.ConfigScope, help="configuration scope to read/modify"
    )


def compilers(parser, args):
    compiler_list(args)
