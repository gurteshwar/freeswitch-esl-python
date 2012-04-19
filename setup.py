from distutils.core import setup, Extension

setup (name = 'FreeSWITCH-esl-python',
       version = '0.1vdev',
       ext_modules=[Extension('_ESL',sources=['swig/esl_wrap.cpp',
                                              'src/esl.c',
                                              'src/esl_json.c',
                                              'src/esl_event.c',
                                              'src/esl_threadmutex.c',
                                              'src/esl_config.c',
                                              'src/esl_oop.cpp',
                                              'src/esl_buffer.c'],
       include_dirs=['include/'])],
       packages = ['freeswitchESL'],
       pymodules = ['ESL'],
       description = 'Auto-generated swig python module for FreeSWITCH mod_esl with a binary component.',)
	   
