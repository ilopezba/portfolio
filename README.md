portfolio
=========

**A django portfolio for artists that want to show and sell their works**<br>
_This Project is under development. If you have any ideas or things you want me to add to the project you are welcome, send me an email: salvatore[:at:]universojuegos.es_


<h2>Structure:</h2><br>
The portfolio has 'pages'. Pages can be shown in the menu.<br>
Each page contains 'sections'. For example:
 - _Page_ **Photography**<br>
		+ _Section_ **Landscapes**<br>
		+ _Section_ **People**<br>
 - _Page_ **Stocks**<br>
		+ _Section_ **Textures**<br>

*You can create your own structure with the django admin panel*

This structure is also applied to the 'Shop' (/shop/page/section/---)

<h2>Content:</h2><br>
Each section can contain different kinds of 'art'. The main type of content (the one that is currently implemented) is 'Image'.
But an 'Image' is more complex than you may think, because each Image contains one or more 'Image Versions'. This way you can 
upload a black and white version of the original photo without creating a new 'Image' object that has no relationship with the 
original one.

You can choose which 'Images' will be available in the shop so that users can buy them. 


More content types can be added (t-shirts? paintings?) if needed.
