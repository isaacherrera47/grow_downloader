#!/bin/bash
echo "https://github.com/grow/grow/releases/download/$1/Grow-SDK-Mac-$1.zip"
curl -L "https://github.com/grow/grow/releases/download/$1/Grow-SDK-Mac-$1.zip" --output "$1.zip"

echo "Ok, we've got the file, let's unzip $1.zip"
unzip -u "$1.zip"
rm "$1.zip"
echo "I removed that unused zip :)"
mv "grow" "grow$2"
mkdir -p "$HOME/bin"
mv "grow$2" "$HOME/bin/grow$2"
echo "I moved grow file to $HOME/bin folder"

echo "Do you want to append path to .zshrc?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo "path += (\"\$HOME/bin\")" >> "$HOME/.zshrc"; echo "Path was added to your bash profile"; break;;
        No ) break;;
    esac
done

echo "Done! grow file is now available in $HOME/bin"