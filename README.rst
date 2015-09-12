========================
django-examples
========================

Proyecto de ejemplos para Django 1.8.4

Para ejecutar el siguiente proyecto deberá seguir los siguientes pasos:

#. Crear ambiente de trabajo
#. Instalar Django
#. Instalar las dependencias


Ambiente de trabajo
===================

Existen varios ambientes de trabajo, para este proyecto he usado Virtualenv.

Virtualenv Only
---------------

Primero asegurate que tienes (http://www.virtualenv.org) instalado. Luego
que lo tengas crea el ambiente::

    $ virtualenv venv_examples



Instala las dependencias of Dependencias
========================================

Dependiendo del embiente puedes instalar las dependencias locales o de 
prodcción::

Para desarrollo::

    $ pip install -r requirements/local.txt

Para producción::

    $ pip install -r requirements.txt

*note: en nuestro caso hemos probado los modulos para desarrollo


Módulos probados
================

- Exportar a excel con django-import-export==0.2.8
- Por hacer importar desde excel con django-import-export==0.2.8

