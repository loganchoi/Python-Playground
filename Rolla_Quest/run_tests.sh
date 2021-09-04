#!/bin/bash

grade_update()
{
    # updates grade and prints based on return code of preceeding statement
    # usage: grade_update test_name points_to_add
    return_status=$?
    echo Test for "$1": >>$student_file
    if (( return_status == 0 ))
    then
        echo pass for "$2" points >>$student_file
        (( grade = grade + "$2" ))
    else
        echo fail for 0 more points >>$student_file
    fi
    echo >>$student_file
}

grade=0
student_file=../results.txt

cd unit_tests

if [[ -f $student_file ]]
then
    rm $student_file
fi

timeout 15 python3 is_valid_move_test.py
grade_update valid_move 25

timeout 15 python3 make_move_test.py
grade_update make_move 25

timeout 15 python3 go_inside_cs_building_test.py
grade_update go_inside 25

timeout 15 python3 go_outside_cs_building_test.py
grade_update go_outside 25

echo -e "Your grade is:\n$grade" >>$student_file

cd ..

# cleanup
rm -r __pycache__
rm -r unit_tests/__pycache__

