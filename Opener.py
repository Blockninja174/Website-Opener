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
name = input("What is the website you would like to open?")
if name in websites:
    webbrowser.get(browser()).open(websites[name.lower()])
elif name == ("exit") or ("quit"):
    exit()
elif "." in name:
    webbrowser.get(browser()).open(name.lower())
else:
    webbrowser.get(browser()).open(name.lower() + ".com")
