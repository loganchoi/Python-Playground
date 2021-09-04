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

timeout 15 python3 make_move_test.py

timeout 15 python3 go_inside_cs_building_test.py

timeout 15 python3 go_outside_cs_building_test.py

timeout 15 python3 proximity_sensor_test.py
grade_update proximity 20

timeout 15 python3 check_base_test.py
grade_update check_base_class 10

timeout 15 python3 hero_functions_test.py
grade_update hero 10

timeout 15 python3 brother_jedd_functions_test.py
grade_update jedd 10

timeout 15 python3 food_vendor_functions_test.py
grade_update food_vendor 10

timeout 15 python3 hugging_mom_functions_test.py
grade_update hugging_mom 10

timeout 15 python3 lost_student_functions_test.py
grade_update lost_student 10

timeout 15 python3 sweater_merchant_functions_test.py
grade_update sweater_merchant 10

mypy --strict --disallow-any-explicit ../rolla_quest.py
grade_update mypy 10

echo -e "Your grade is:\n$grade" >>$student_file

cd ..

# cleanup
rm -r __pycache__
rm -r unit_tests/__pycache__
rm -r unit_tests/.mypy_cache

