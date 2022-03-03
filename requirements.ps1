iwr -useb get.scoop.sh | iex

scoop install git
regedit /s "$HOME\scoop\apps\7zip\current\install-context.reg"
git config --global credential.helper manager-core

scoop bucket add extras

scoop install python
regedit /s "$HOME\scoop\apps\python\current\install-pep-514.reg"
python -m pip install matplotlib

scoop install mingw
scoop install gow
scoop install swig
scoop install scipy

scoop install vscode
code --install-extension ms-python.python
code --install-extension ms-vscode.cpptools-extension-pack 
code --list-extensions 
