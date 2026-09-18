@echo off
echo Setting up Terminote...

python -m pip install --upgrade pip
pip install -e .

echo Setup complete! Type in 'terminote' in the terminal to use!
pause