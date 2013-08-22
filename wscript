#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2012 SjB <steve@sagacity.ca>. All Rights Reserved.

import os
from waflib import Utils, Options, Logs

APPNAME = 'EtoExample'
VERSION = '0.0.1'
REVISION = ''

top = '.'
out = 'build'

sjb_waftooldir = 'waftools/sjb-waftools/extra'

def init(ctx):
    Logs.warn('Waf script for {0}'.format(APPNAME))

def cheRk(ctx):
    Logs.warn('Waf checking {0}'.format(APPNAME))

def options(ctx):
    ctx.load('cs_extra etoform', tooldir=sjb_waftooldir)

    ctx.add_option('--debug', '-d', dest='debug', action='store_true', default=False,
        help='Enable debug build')
    ctx.add_option('--default-assembly-dir', type='string', dest='default_assembly_dir',
        help='Location of local assembly repository', default=None)


def configure(conf):
    conf.load('cs_extra etoform', tooldir=sjb_waftooldir)

    assembly_search_path = Options.options.default_assembly_dir or os.environ.get('DEFAULT_ASSEMBLY_DIR', './libs')
    conf.check_etoform(path_list = generate_path_list(assembly_search_path, 'Eto'))

    if Options.options.debug:
        conf.set_define('DEBUG')

    conf.env.APPNAME = APPNAME
    conf.set_define(Utils.unversioned_sys_platform().upper())


def generate_path_list(path, module):
    return '{0} {0}/{1}'.format(path, module)

def build(bld):
    modules = ['Scrollable']

    bld.recurse(modules)
