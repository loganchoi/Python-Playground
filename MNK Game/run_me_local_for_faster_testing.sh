#!/usr/bin/env sh

echo "These tests are in the order of how they should be written, and completeness"
echo
echo "Running draw_board output and diffs"
cd unit_tests
timeout 15 python3 check_draw_board.py >output.txt
sdiff output.txt draw_board_output.txt
timeout 15 python3 check_player_letter.py <input_player_letter.txt
timeout 15 python3 check_space_free.py
echo
echo "Running valid_player_move output and diffs"
timeout 15 python3 check_valid_player_move.py <valid_player_move_input.txt >output.txt
sdiff output.txt valid_player_move_output.txt
timeout 15 python3 check_across.py
timeout 15 python3 check_down.py
timeout 15 python3 check_diagonal_right.py
timeout 15 python3 check_diagonal_left.py
timeout 15 python3 check_board_full.py
timeout 15 python3 check_valid_random_moves.py
rm output.txt
rm -r __pycache__
cd ..
echo
echo "Running player_win_input/output pair and diffs"
timeout 15 python3 mnk_game.py <whole_games/player_win_input.txt >output.txt
sdiff output.txt whole_games/player_win_output.txt
echo
echo "Running ai_win_input/output pair and diffs"
timeout 15 python3 mnk_game.py <whole_games/ai_win_input.txt >output.txt
sdiff output.txt whole_games/ai_win_output.txt
echo
echo "Running game_tie_input/output pair and diffs"
timeout 15 python3 mnk_game.py <whole_games/game_tie_input.txt >output.txt
sdiff output.txt whole_games/game_tie_output.txt
echo
echo "Running player_win_ai_win_input/output pair and diffs"
timeout 15 python3 mnk_game.py <whole_games/player_win_ai_win_input.txt >output.txt
sdiff output.txt whole_games/player_win_ai_win_output.txt
rm output.txt
rm -r __pycache__

