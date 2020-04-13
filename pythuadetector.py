def uadetect(ua):
    if ("Nintendo DSi" in ua) == True:
        browser = "Nintendo DSi Browser"
    elif ("Silk" in ua) == True:
        browser = "Silk"
    elif ("python-requests" in ua) == True:
        browser = "python-requests"
    elif ("AppleTV" in ua) == True:
        browser = "iTunes"
    elif ("iTunes" in ua) == True:
        browser = "iTunes"
    elif ("wOSBrowser" in ua) == True:
        platform = "webOS Browser"
    elif ("XBMC" in ua) == True:
        browser = "XBMC"
    elif ("wget" in ua) == True:
        browser = "Wget"
    elif ("Wget" in ua) == True:
        browser = "Wget"
    elif ("curl" in ua) == True:
        browser = "cURL"
    elif ("cURL" in ua) == True:
        browser = "cURL"
    elif ("Roblox" in ua) == True:
        browser = "Roblox"
    elif ("Windows-Media-Player" in ua) == True:
        browser = "Windows Media Player"
    elif ("WinHTTP" in ua) == True:
        browser = "Microsoft Windows HTTP Services"
    elif ("WindowsPowerShell" in ua) == True:
        browser = "Windows Power Shell"
    elif ("Tesla" in ua) == True:
        browser = "Tesla Browser"
    elif ("QtCarBrowser" in ua) == True:
        browser = "Tesla Browser"
    elif ("FBIOS" in ua) == True:
        browser = "Facebook App"
    elif ("FB_IAB" in ua) == True:
        browser = "Facebook App"
    elif ("Nitro" in ua) == True:
        browser = "Nintendo DS Browser"
    elif ("Nintendo DS" in ua) == True:
        browser = "Nintendo DS Browser"
    elif ("NintendoBrowser" in ua) == True:
        browser = "Nintendo Browser"
    elif ("Nintendo 3DS" in ua) == True:
        browser = "Netfront Browser NX"
    elif ("Dalvik" in ua) == True:
        browser = "Java-based Browser"
    elif ("PlayStation 4" in ua) == True:
        browser = "PlayStation 4 Browser"
    elif ("Wii" in ua) == True:
        browser = "Internet Channel"
    elif ("NokiaBrowser" in ua) == True:
        browser = "Nokia Browser"
    elif ("PlayStation Vita" in ua) == True:
        browser = "Silk"
    elif ("PlayStation Portable" in ua) == True:
        browser = "NetFront"
    elif ("PLAYSTATION 3" in ua) == True:
        browser = "NetFront"
    elif ("AOL" in ua) == True:
        browser = "AOL Browser"
    elif ("SamsungBrowser" in ua) == True:
        browser = "Samsung Browser"
    elif ("Netscape" in ua) == True:
        browser = "Netscape Navigator"
    elif ("Maxthon" in ua) == True:
        browser = "Maxthon"
    elif ("YaBrowser" in ua) == True:
        browser = "Yandex Browser"
    elif ("Yowser" in ua) == True:
        browser = "Yandex Browser"
    elif ("S40OviBrowser" in ua) == True:
        browser = "Ovi"
    elif ("UC Browser" in ua) == True:
        browser = "UCBrowser"
    elif ("UCBrowser" in ua) == True:
        browser = "UCBrowser"
    elif ("UBrowser" in ua) == True:
        browser = "UCBrowser"
    elif ("Kindle" in ua) == True:
        browser = "Kindle Browser"
    elif ("IEMobile" in ua) == True:
        browser = "Microsoft IEMobile"
    elif ("Edg" in ua) == True:
        browser = "Microsoft Edge"
    elif ("Vivaldi" in ua) == True:
        browser = "Vivaldi"
    elif ("Firefox" in ua) == True:
        browser = "Mozilla Firefox"
    elif ("Chrome" in ua) == True:
        browser = "Google Chrome"
    elif ("CriOS" in ua) == True:
        browser = "Google Chrome"
    elif ("MSIE" in ua) == True:
        browser = "Microsoft Internet Explorer"
    elif ("Trident" in ua) == True:
        browser = "Microsoft Internet Explorer"
    elif ("Opera" in ua) == True:
        browser = "Opera"
    elif ("BlackBerry" in ua) == True:
        browser = "BlackBerry Browser"
    elif ("Safari" in ua) == True:
        browser = "Safari"
    else:
        browser = "Unknown Browser"

    if ("Nintendo DSi" in ua) == True:
        platform = "Nintendo DSi"
    elif ("Nitro" in ua) == True:
        platform = "Nintendo DS"
    elif ("Nintendo DS" in ua) == True:
        platform = "Nintendo DS"
    elif ("Nintendo Switch" in ua) == True:
        platform = "Nintendo Switch"
    elif ("New Nintendo 3DS" in ua) == True:
        platform = "New Nintendo 3DS"
    elif ("Nintendo 3DS" in ua) == True:
        platform = "Nintendo 3DS"
    elif ("PlayStation 4" in ua) == True:
        platform = "PlayStation 4"
    elif ("PlayStation 5" in ua) == True:
        platform = "PlayStation 5"
    elif ("WiiU" in ua) == True:
        platform = "Nintendo Wii U"
    elif ("Wii" in ua) == True:
        platform = "Nintendo Wii"
    elif ("PlayStation Vita" in ua) == True:
        platform = "PlayStation Vita"
    elif ("Playstation Vita" in ua) == True:
        platform = "PlayStation Vita"
    elif ("PlayStation Portable" in ua) == True:
        platform = "PlayStation Portable"
    elif ("PLAYSTATION 3" in ua) == True:
        platform = "PlayStation 3"
    elif ("Xbox One" in ua) == True:
        platform = "Xbox One"
    elif ("SHIELD Build" in ua) == True:
        platform = "Nvidia SHIELD"
    elif ("OUYA Build" in ua) == True:
        platform = "OUYA"
    elif ("Xbox 360" in ua) == True:
        platform = "Xbox 360"
    elif ("Xbox" in ua) == True:
        if ("Windows NT 6.1" in ua) == True:
            platform = "Xbox 360"
        else:
            platform = "Xbox"
    elif ("CrKey" in ua) == True:
        platform = "Google Chromecast"
    elif ("CrOS" in ua) == True:
        platform = "Chrome OS"
    elif ("Glass" in ua) == True:
        platform = "Glass OS (Android)"
    elif ("Hudl" in ua) == True:
        platform = "Tesco Hudl (Android)"
    elif ("GoogleTV" in ua) == True:
        platform = "Google TV"
    elif ("Roku" in ua) == True:
        platform = "Roku Box"
    elif ("AppleTV" in ua) == True:
        platform = "Apple TV"
    elif ("Glass" in ua) == True:
        platform = "Google Glass"
    elif ("PlayStation" in ua) == True:
        platform = "PlayStation"
    elif ("Nintendo Game Boy" in ua) == True:
        platform = "Nintendo Switch"
    elif ("hpwOS" in ua) == True:
        platform = "HP webOS"
    elif ("HPwOS" in ua) == True:
        platform = "HP webOS"
    elif ("Windows Phone" in ua) == True:
        platform = "Windows Phone"
    elif ("Windows Mobile" in ua) == True:
        platform = "Windows Mobile"
    elif ("Windows NT 10.0" in ua) == True:
        platform = "Microsoft Windows 10"
    elif ("Windows NT 6.3" in ua) == True:
        platform = "Microsoft Windows 8.1"
    elif ("Windows NT 6.2" in ua) == True:
        platform = "Microsoft Windows 8"
    elif ("Windows NT 6.1" in ua) == True:
        platform = "Microsoft Windows 7"
    elif ("Windows NT 6.0" in ua) == True:
        platform = "Microsoft Windows Vista"
    elif ("Windows NT 5.1" in ua) == True:
        platform = "Microsoft Windows XP"
    elif ("Windows NT 5.0" in ua) == True:
        platform = "Microsoft Windows 2000"
    elif ("Windows NT" in ua) == True:
        platform = "Microsoft Windows NT"
    elif ("Windows 98" in ua) == True:
        platform = "Microsoft Windows 98"
    elif ("Windows 95" in ua) == True:
        platform = "Microsoft Windows 95"
    elif ("Windows 3.1" in ua) == True:
        platform = "Microsoft Windows 3.1"
    elif ("Windows" in ua) == True:
        platform = "Microsoft Windows"
    elif ("mingw" in ua) == True:
        platform = "Microsoft Windows"
    elif ("iPod" in ua) == True:
        platform = "iPod touch (iOS)"
    elif ("iPhone" in ua) == True:
        platform = "iPhone (iOS)"
    elif ("iPad" in ua) == True:
        platform = "iPad (iOS)"
    elif ("iOS" in ua) == True:
        platform = "iOS"
    elif ("Mac OS X" in ua) == True:
        platform = "Mac OS X"
    elif ("Macintosh" in ua) == True:
        platform = "Mac OS"
    elif ("Mac PowerPC" in ua) == True:
        platform = "Mac OS"
    elif ("Mac_PowerPC" in ua) == True:
        platform = "Mac OS"
    elif ("Mac PPC" in ua) == True:
        platform = "Mac OS"
    elif ("Mac_PPC" in ua) == True:
        platform = "Mac OS"
    elif ("KF" in ua) == True:
        platform = "Fire OS (Android)"
    elif ("Kindle" in ua) == True:
        platform = "Fire OS (Android)"
    elif ("Tesla" in ua) == True:
        platform = "Tesla Car"
    elif ("Android" in ua) == True:
        platform = "Android"
    elif ("Linux" in ua) == True:
        platform = "Linux"
    elif ("linux" in ua) == True:
        platform = "Linux"
    elif ("SymbOS" in ua) == True:
        platform = "Symbian"
    elif ("S40" in ua) == True:
        platform = "Symbian"
    elif ("S60" in ua) == True:
        platform = "Symbian"
    elif ("Series30" in ua) == True:
        platform = "Symbian"
    elif ("Series40" in ua) == True:
        platform = "Symbian"
    elif ("Series60" in ua) == True:
        platform = "Symbian"
    elif ("SymbianOS" in ua) == True:
        platform = "Symbian"
    elif ("OS X" in ua) == True:
        platform = "Mac OS X"
    elif ("BlackBerry" in ua) == True:
        platform = "BlackBerry OS"
    else:
        platform = "Unknown Platform"
    
    print (browser+" on "+platform)
