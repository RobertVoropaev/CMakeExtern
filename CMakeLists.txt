cmake_minimum_required(VERSION 2.8)
project(cmake_extern)

### Path ###

set(MAIN_DIR ${CMAKE_CURRENT_SOURCE_DIR}/B)
set(INDEX_DIR ${MAIN_DIR}/C)
set(LIB_DIR ${MAIN_DIR}/A)

set(MAIN_FILE ${MAIN_DIR}/main.h ${MAIN_DIR}/main.cpp)
set(INDEX_FILE ${INDEX_DIR}/index.h)
set(PY_PRE_FILE ${INDEX_DIR}/preparing.py)

### Generate index ###

find_package(PythonInterp REQUIRED)

add_custom_command(
    COMMAND "${PYTHON_EXECUTABLE}" 
    		"${PY_PRE_FILE}" 
    		--dir "${INDEX_DIR}"    
    OUTPUT "${INDEX_FILE}")

add_custom_target(generate_header ALL
    DEPENDS "${INDEX_FILE}")

### Add library ###

include_directories(${LIB_DIR})

add_executable(main ${MAIN_FILE})
add_subdirectory(${LIB_DIR})

target_link_libraries(main lib)

### Doxygen ###

find_package(Doxygen)
if (DOXYGEN_FOUND)
    set(DOXYGEN_IN ${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile.in)
    set(DOXYGEN_OUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)

    configure_file(${DOXYGEN_IN} ${DOXYGEN_OUT} @ONLY)

    add_custom_target( doc_doxygen ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_OUT}
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM )
else (DOXYGEN_FOUND)
  message("Doxygen need to be installed to generate the doxygen documentation")
endif (DOXYGEN_FOUND)
