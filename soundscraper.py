from selenium import webdriver
import requests
import bs4
import os

# new, top, mix, track, and artist urls
top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search/sounds?q="
artist_url = "http://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

# create the selenium browser
browser = webdriver.Chrome("/Users/ian/Downloads/chromedriver")
browser.get("https://soundcloud.com")

# main menu
print()
print(">>> Welcome to the Python Soundcloud Scraper!")
print(">>> Explore the Top / New & Hot Charts for all Genres")
print(">>> Search for tracks, artists, and mixes")
print()

while True:
    print(">>> Menu")
    print(">>> 1 - Search for a track")
    print(">>> 2 - Search for an artist")
    print(">>> 3 - Search for a mix")
    print(">>> 4 - Top Charts")
    print(">>> 5 - New & Hot Charts")
    print(">>> 0 - Exit")
    print()

    choice = int(input(">>> Your choice: "))

    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue

    # search for an artist
    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue

    # search for a mix
    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url_end)
        continue

    # get the top 50 tracks for a genre
    if choice == 4:
        request = requests.get(top_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print(">>> Genres Available: ")
            print()
            genres = soup.select("a[href*=genre]")[2:]
            genre_links = []

            # print out all of the available genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> Your choice (x to go back to the main menu): ")
            print()

            if choice == "x":
                break
            else:
                choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index + 1) + ": " + track.text)
                print()

            # song selection loop
            while True:
                choice = input(">>> Your choice (x to re-select a new genre): ")
                print()

                if choice == "x":
                    break
                else:
                    choice = int(choice) - 1

                print("Now playing: " + track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])

    # get the new and hot tracks for a genre
    if choice == 5:
        request = requests.get(new_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print(">>> Genres Available: ")
            print()
            genres = soup.select("a[href*=genre]")[2:]
            genre_links = []

            # print out all of the available genres
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))

            print()
            choice = input(">>> Your choice (x to go back to the main menu): ")
            print()

            if choice == "x":
                break
            else:
                choice = int(choice)

            url = "http://soundcloud.com" + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")

            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []

            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index + 1) + ": " + track.text)
                print()

            # song selection loop
            while True:
                choice = input(">>> Your choice (x to re-select a new genre): ")
                print()

                if choice == "x":
                    break
                else:
                    choice = int(choice) - 1

                print("Now playing: " + track_names[choice])
                print()

                browser.get("http://soundcloud.com" + track_links[choice])


print()
print("Goodbye!")
print()
