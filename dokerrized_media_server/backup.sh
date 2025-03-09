#!/bin/bash

# Tworzenie zmiennej z datą i godziną
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Ścieżka do folderu kopii zapasowej
BACKUP_DIR="/WebAppGK/backup_$TIMESTAMP"

# Tworzenie folderu na kopię zapasową
mkdir -p "$BACKUP_DIR"

# Kopiowanie wszystkich plików projektu
cp -r /WebAppGK/server.py "$BACKUP_DIR/"
cp -r /WebAppGK/templates "$BACKUP_DIR/"
cp -r /WebAppGK/static "$BACKUP_DIR/"
cp -r /WebAppGK/files "$BACKUP_DIR/"

echo "✅ Kopia zapasowa utworzona w: $BACKUP_DIR"

