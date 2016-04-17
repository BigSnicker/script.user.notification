import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "It's time for your medication."
line2 = " "
line3 = "Please take it before pressing OK" 

xbmcgui.Dialog().ok("Hello Guys", line1, line2, line3)
