def getImage(cityName):
    cities={"Hyderabad":"https://wallpapercave.com/wp/wp10257499.jpg",
           "Delhi":"https://wallpapercave.com/wp/wp9429743.jpg",
           "Mumbai":"https://wallpapercave.com/wp/wp7526612.jpg",
           "London":"https://wallpapercave.com/wp/wp3787066.jpg",
           "Kolkata":"https://wallpapercave.com/wp/wp8621025.jpg",
           "Chennai":"https://wallpapercave.com/uwp/uwp3839387.jpeg",
           "Kukatpally":"",
           "New York":"https://wallpapercave.com/uwp/uwp4253840.webp",
           "Warangal":"https://wallpapercave.com/wp/wp12177356.jpg"
           }
    try:
        return cities[cityName]
    except:
        return cities['Hyderabad']