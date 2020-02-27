# OpenSesame build scripts for Windows

Copyright 2020 Sebastiaan Mathôt


## About

These scripts build Anaconda environments for OpenSesame, and package them as `.zip` and `.exe` installers. 


## Use

```
python build.py [target] [options]
```

Target can be one of:

- `--py37`
- `--py37-megapack`
- `--py27`

Options can be:

- `--frozen` to build with fixed package versions determined by previous builds
- `--zip` to create `.zip` archive for distribution
- `--exe` to create `.exe` installer for distribution
- `--clear` to clear the `conda`` environment folder before building
- `--all` is equal to `--zip`, `--exe`, and `--clear`


## Requirements

- Anaconda
- NSIS installer
- 7zip


## License

This code is distributed under the terms of the GNU General Public License 3. The full license should be included in the file COPYING, or can be obtained from:

- <http://www.gnu.org/licenses/gpl.txt>
