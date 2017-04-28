#!/bin/bash
# Indique au système que l'argument qui suit est le programme utilisé pour exécuter ce fichier
# En règle générale, les "#" servent à mettre en commentaire le texte qui suit comme ici
rm form/manager/*.pyc
rm form/models/*.pyc
rm form/migrations/*.pyc
rm form/ajax/*.pyc
rm form/*.pyc
rm form/views/*.pyc
rm Project/*.pyc
rm -rf media/*
tree > tree.txt
exit 0
