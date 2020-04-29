cmake_minimum_required(VERSION 2.8)
find_package(PythonInterp REQUIRED)

project(cmake_extern)

set(MAIN_DIR B)
set(INDEX_DIR ${MAIN_DIR}/C)
set(LIB_DIR ${MAIN_DIR}/A)

set(MAIN_FILE ${MAIN_DIR}/main.h ${MAIN_DIR}/main.cpp)
set(INDEX_FILE ${INDEX_DIR}/index.h)

set(PY_PRE_FILE preparing.py)
execute_process(COMMAND python3 ${PY_PRE_FILE}
                WORKING_DIRECTORY ${INDEX_DIR})

include_directories(${LIB_DIR})

add_executable(main ${MAIN_FILE})
add_subdirectory(${LIB_DIR})

target_link_libraries(main lib)


