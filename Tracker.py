from bs4 import BeautifulSoup
import requests
import tkinter as tk
def findCov():
    
    html_text = requests.get(f'https://www.nytimes.com/interactive/2021/us/covid-cases.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    states = soup.find('td', class_= "num cases svelte-17z9x2b").text
    #state = states.find('a')

    return states

def stateCov():
    stateog = textfield.get()
    state = (stateog.replace(' ', '-')).lower()
    stateog = stateog.title()
    html_text = requests.get(f'https://www.nytimes.com/interactive/2021/us/{state}-covid-cases.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    try:
        states = soup.find('td', class_= "num cases svelte-17z9x2b").text
    except AttributeError:
        mainlabel['text']= "Enter a valid state."
    #state = states.find('a')

    mainlabel['text']= f'COVID Cases in {stateog}: ' + states
    

def reload():
    new_data = findCov()
    mainlabel['text'] = "COVID Cases in the US: " + new_data

findCov()

root = tk.Tk()
root.geometry("900x700")
root.title("The Best COVID Tracker")
f = ("arial", 25, "bold")
s = ("arial", 25, "normal")
#corner = ("arial", 10, "normal")

mainlabel = tk.Label(root, text="Enter a state below. ", font = s)
mainlabel.pack()

textfield = tk.Entry(root, width_=50)
textfield.pack()

mainlabel = tk.Label(root, text="COVID Cases in the US: " + findCov(), font = f)
mainlabel.pack()

gbtn = tk.Button(root, text = "Get Data", font = f, relief = 'solid', command = stateCov)
gbtn.pack()

ubtn = tk.Button(root, text = "Total Cases", font = f, relief = 'solid', command = reload)
ubtn.pack()

root.mainloop()
