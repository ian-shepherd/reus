Welcome to reus's documentation!
================================

**reus** is a Python library for getting soccer data and information from 
`fbref <https://fbref.com/>`_, `fotmob <http://fotmob.com/>`_, and `transfermarkt <http://transfermarkt.com/>`_.
You can view the code on |github_link|.

.. |github_link| raw:: html

   <a href="https://github.com/ian-shepherd/reus" target="_blank">Github</a>

To install Reus::

		pip install reus
	
Please scrape responsibly. Do not make calls faster than 1 per 3 seconds. If you are iterating over multiple pages, please use a sleep time of at least 3 seconds. ::
      
      time.sleep(4)

It is a minor inconvenience to you but lets us all keep accessing the data.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   fbref
   fotmob
   transfermarkt


.. note::

   This project is under active development.
   
   
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
