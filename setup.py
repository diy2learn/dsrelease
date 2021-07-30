#!/usr/bin/env python

# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    entry_points={"console_scripts": ["dsrelease = dsrelease.main:program.run"]}
)
