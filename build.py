# coding=utf-8

import os
import sys
import subprocess

CONDA_FOLDER = r'conda'
OS_VERSION = '3.3.0a59'
BUILD_VERSION = '1'
MAKENSIS = r'..\nsis-3.05\makensis.exe'
ZIP = r'..\7zip\7z.exe'
ENV_TARGET = CONDA_FOLDER + r'\envs\opensesame_{version}'
if '--py2' in sys.argv:
    BAT_TMPL = r'bat\build-env-py2.bat.tmpl'
    NSI_TMPL = r'nsi\py2.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\envs\rapunzel-py2\\'
    VERSION = OS_VERSION + '-py27-win64-' + BUILD_VERSION
else:
    BAT_TMPL = r'bat\build-env.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\envs\rapunzel\\'
    VERSION = OS_VERSION + '-py37-win64-' + BUILD_VERSION


# First build the environment
print('Creating build.bat')
with open(BAT_TMPL) as fd:
    tmpl = fd.read()
with open('build.bat', 'w') as fd:
    fd.write(tmpl.format(env_folder=ENV_FOLDER))
print('Running build.bat')
subprocess.run(['build.bat'])

# Now build the installer
print('Creating build.nsi')
with open(NSI_TMPL) as fd:
    tmpl = fd.read()
with open('build.nsi', 'w') as fd:
    fd.write(tmpl.format(env_folder=ENV_FOLDER, version=VERSION))
print('Compiling build.nsi')
subprocess.run([MAKENSIS, '/V4', '/P3', 'build.nsi'])

# And then zip the environment
print('Moving environment')
os.rename(ENV_FOLDER, ENV_TARGET.format(version=VERSION))
print('Zipping environment')
subprocess.run([
    ZIP,
    'a',
    '-y',
    'opensesame_{}.zip'.format(VERSION),
    ENV_TARGET.format(version=VERSION)
])
print('Done!')
