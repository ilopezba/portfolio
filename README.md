portfolio
=========

**A django portfolio for artists that want to show and sell their work**


Structure:
The portfolio has 'pages'. Pages can be shown in the menu.
Each page contains sections. For example:
 - _Page_ **Photography**
		+ _Section_ **Landscapes**
		+ _Section_ **People**
 - _Page_ **Stocks**
		+ _Section_ **Textures**

*You can create your own structure with the django admin panel*

Content:
Each section can contain different kinds of 'art'. The main type of content (the one that is currently implemented) is 'Images'.
But an 'Image' is more complex than you may think, because each Image contains one or more 'Image Versions'. This way you can 
upload a black and white version of the original photo without creating a new 'Image' object that has no relationship with the 
original photo.
