python3 gen_test.py 100 250 113 > tests/test_random_01.in
python3 gen_test.py 1000 3000 117 > tests/test_random_02.in
python3 gen_test.py 10000 35000 119 > tests/test_random_03.in
python3 gen_test.py 50000 150000 123 > tests/test_random_04.in
python3 gen_test.py 100000 300000 997 > tests/test_random_05.in
python3 gen_edge_cases.py overflow        > tests/test_edge_06_overflow.in
python3 gen_edge_cases.py nopath          > tests/test_edge_07_no_path.in
python3 gen_edge_cases.py subliter        > tests/test_edge_08_rounding_error.in
python3 gen_edge_cases.py stress          > tests/test_edge_09_stress.in
python3 gen_edge_cases.py city_vs_country > tests/test_edge_10_fuel_economy.in

g++ wzor.cpp
./a.out < tests/test_random_01.in  > tests/test_random_01.out
./a.out < tests/test_random_02.in  > tests/test_random_02.out
./a.out < tests/test_random_03.in  > tests/test_random_03.out
./a.out < tests/test_random_04.in  > tests/test_random_04.out
./a.out < tests/test_random_05.in  > tests/test_random_05.out
./a.out < tests/test_edge_06_overflow.in  > tests/test_edge_06_overflow.out
./a.out < tests/test_edge_07_no_path.in  > tests/test_edge_07_no_path.out
./a.out < tests/test_edge_08_rounding_error.in  > tests/test_edge_08_rounding_error.out
./a.out < tests/test_edge_09_stress.in  > tests/test_edge_09_stress.out
./a.out < tests/test_edge_10_fuel_economy.in  > tests/test_edge_10_fuel_economy.out