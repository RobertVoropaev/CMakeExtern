cmake_minimum_required(VERSION 2.8) 
project(cmake_extern_lib)

set(SOURCE_LIB lib.cpp)		# Установка переменной со списком исходников

add_library(lib STATIC ${SOURCE_LIB})# Создание статической библиотеки
