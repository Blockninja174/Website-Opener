import webbrowser
import sites
import config

websites = sites.list

def browser():
    if config.default_browser == "chrome":
        return config.chrome_path
    elif config.default_browser == "opera":
        return config.opera_path
    elif config.default_browser == "edge":
        return config.edge_path
    else:
        print("Browser not found, please check config.py")

print("Default browser is " + config.default_browser)
def main():
    name = input("What is the website you would like to open?")
    if name in websites:
        print("Opening " + name + "...")
        webbrowser.get(browser()).open(websites[name])
        if config.repeat == False:
            exit()
    elif "." in name:
        print("Opening " + name + "...")
        webbrowser.get(browser()).open("https://" + name)
        if config.repeat == False:
            exit()
    elif name == "exit" or name == "quit":
        exit()
    else:
        webbrowser.get(browser()).open("https://www.google.com/search?q=" + name)
        if config.repeat == False:
            exit()

main()
while config.repeat == True:
    main()

