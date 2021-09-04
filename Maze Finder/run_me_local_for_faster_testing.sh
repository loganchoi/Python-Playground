#!/usr/bin/env sh

echo "These tests are in the order of how they should be written, and completeness"
timeout 15 python3 fill_matrix_git-version_test.py <unit_test_fstream_readin.txt
timeout 15 python3 find_start_test.py
timeout 15 python3 at_end_test.py
timeout 15 python3 valid_move_test.py
timeout 15 python3 find_exit_test.py
echo
echo "Running sample_input/output pair and diffs:"
timeout 15 python3 maze.py <sample_input.txt >output.txt
sdiff output.txt sample_output.txt
echo
echo "Running key_input/output pair and diffs:"
timeout 15 python3 maze.py <key_input.txt >output.txt
sdiff output.txt key_output.txt
rm output.txt
rm -r __pycache__

