#!/bin/bash

# ==============================
# File Analyzer Script
# ==============================

# Check if directory argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

DIR="$1"

# Check if directory exists
if [ ! -d "$DIR" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi

echo "=============================="
echo "Analyzing Directory: $DIR"

# List all files with sizes
echo -e "\n Files with Sizes:"
find "$DIR" -type f -exec ls -lh {} \;

# Total file count
FILE_COUNT=$(find "$DIR" -type f | wc -l)
echo -e "\n Total Files: $FILE_COUNT"

# Total directory size
TOTAL_SIZE=$(du -sh "$DIR" | cut -f1)
echo -e "Total Directory Size: $TOTAL_SIZE"

# Largest file
LARGEST_FILE=$(find "$DIR" -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n 1)
echo -e "\n Largest File:"
echo "$LARGEST_FILE"

echo -e "\n=============================="
echo "Analysis Complete"
echo "=============================="
