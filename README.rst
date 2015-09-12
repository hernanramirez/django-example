========================
django-examples
========================

Proyecto de ejemplos para Djeango 1.8.4

Para ejecutar el siguiente proyecto deberá seguir los siguientes pasos:

#. Crear ambiente de trabajo
#. Instalar Django
#. Instalar las dependencias


Working Environment
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv venv_examples



Instala las dependencias of Dependencias
========================================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*


Módulos probados
================

- Exportar a excel con django-import-export==0.2.8
- Por hacer importar desde excel con django-import-export==0.2.8

