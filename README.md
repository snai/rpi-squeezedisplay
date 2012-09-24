A small tool for displaying squeezeslave [1] information (such as current playig title, artist, etc) on a SPI LCD display connected to a raspberry pi

As display I am using a BitWizard SPI LCD [2].
BitWizard also provides a tool for accessing the SPI expansion Board on the rpi. [3]

The information is optained by the Logitech Media Server CLI [4]. There has been some great work [5] which I will use to control the CLI with python.

### Requirements ###

* Python2
* PyLMS (see [5] for install Instructions)
* appropriate Hardware (SPI Display, Raspberry PI)

### Links ###

[1] http://wiki.slimdevices.com/index.php/SqueezeSlave  
[2] http://www.bitwizard.nl/catalog/product_info.php?products_id=94  
[3] https://github.com/rewolff/bw_rpi_tools.git  
[4] http://wiki.slimdevices.com/index.php/Logitech_Media_Server_CLI  
[5] https://github.com/jingleman/PyLMS
