import requests
import yaml
from bs4 import BeautifulSoup
#Modefied https://github.com/mzfr/gtfo for one of my project. Was Kinda lazy to code simple stuff :P 
URL = "https://lolbas-project.github.io/"
RAW_URL = "https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS-Project.github.io/master/_lolbas/"
def get_exe():
    """Get a dictionary of all the binaries.

    The format of the dictionary is:
        {'name of the binary': 'url to the binary'}
    """

    exe = dict()
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    tds = soup.find_all('a', class_='bin-name')

    for i in tds:
        exe[i.text] = i['href'][8:][:-1]

    return exe

def parse(data):
    """Parse and print the commands

    The yml file contains the following fields: Description, Command,
    Category, Privileges, OperatingSystem, UseCase, MitreID, MItreLink.

    If any more data has to be printed then we can just do that.

    For easy reference see the following yml file: RAW_URL/Libraries/Ieadvpack.md

    Arguments:
        data {list} -- list of dictionary having everything a command
        yml file contains
    """

    # TODO: Figure out a way to improve this printing
    cmd = data[0]['Commands']
    mitreID=cmd[0]['MitreID']
    name = ((data[0]['Name']).replace(".exe","")).lower()
    try:
        detection = data[0]['Detection'][0]['IOC']
        print "     '{0}':['{1}','{2}'],".format(name,detection,mitreID)
    except KeyError:
        detection = "No Public Signatures. Be Careful!"
        print "     '{0}':['{1}','{2}'],".format(name,detection,mitreID)
    return ""
    #return type(cmd)
    #for c in cmd:
        #print "# " + c['Description'] + "\n"
        #print "CMD:\t\t" + c["Command"]
        #print "Category:\t" + c["Category"]
        #print "Privileges:\t" + c["Privileges"]
        #print "\n"
    #    return c['Detection']

def main():
    exes = get_exe()
    l = [(k, v) for k, v in exes.items()]
    for i in l:
        p= i[1]
        url = RAW_URL + p + '.md'
        r = requests.get(url).text
        data = list(yaml.load_all(r, Loader=yaml.SafeLoader))
        #print data[0]['Detection']
        parse(data)
main()

def list_exe():
    """Display list of all the executables
    """
    exe = get_exe()

    def table(A, n=7): return [A[i:i+n] for i in range(0, len(A), n)]

    tab = table(list(exe.keys()))
    print tab
