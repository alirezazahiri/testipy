# Get Started

-   [Insert C++ or C Codes](#insert-c++-codes)
-   [Add Test Code](#add-test-code)
-   [Run Test Samples](#run-test-samples)
-   [Check Coverages](#check-coverages)
<hr>

## Insert C++ or C Codes
- you can easily add c++ or c files in [/inputs](./inputs) directory
    > *there is no need to add __.exe__ files in this directory, files are finally getting filtered by .cpp extension while program is on!*
<hr>

## Add Test Code
- for testing purposes there is a I/O returning function provided in [io_tst.py](./sample/io_tst.py) 
    ```py
    def main_code(test_index: int=0):
        """ RETURN THE I/O THAT IS COMPATIBLE WITH YOUR TEST """

        i = f"" # some input
        o = f"" # some output

        return i, o
    ```

> test_index is the index of the test that is running currently 
- > useful for I/O preserved tests 

<hr>

## Run Test Samples
- after inserting c++ (or C) codes, and adding the test code in specified directories, it is time to run [combo.py](./combo.py)
- linux & mac
    ```sh
    python3 combo.py
    ```
- windows
    ```sh
    py combo.py
    ```
<hr>

## Check Coverages
- finally you can get a brief coverage report for each c++ code, inside [statistics.txt](./statistics.txt)