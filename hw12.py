import tkinter as tk
import random
import math

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,specieIN, dexIN,catchrateIn,speedIn):
        self.specie = specieIN
        self.dex = dexIN
        self.catchrate = catchrateIn
        self.speed = speedIn
        self.probability = min((int(self.catchrate)+1), 151) / 449.5

    def __str__ (self):
        s = self.specie
        return s


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        #how many safari ball
        self.balls = 30
        self.pokemonList = self.readFile()
        #end of read file

        self.pokemonCaught = []
        #initialize current pokemon
        self.currentPokemon = self.pokemonList[random.randint(0,len(self.pokemonList)-1)]

        #currentPokemon variables these need to be renewed
        self.currentCatchRate = int(self.currentPokemon.catchrate)
        self.currentPossibility = min((self.currentCatchRate+1), 151) / 449.5
        self.currentSpeed = int(self.currentPokemon.speed)
        self.currentRunawayRate = int(self.currentPokemon.speed) * 2 / 256
        self.isAngry = False
        self.isEating = False
        self.eatingRound = 0
        self.angryRound = 0
        #but you must use your Pokemon class in some capacity

        #don't forget to initialize any instance variables you want to track here

        self.initFrame(master)
        self.createWidgets()

        #call nextPokemon() method here to initialize your first random pokemon
        #self.nextPokemon = self.nextPokemon()


    def initFrame(self, master):
        #DO NOT MODIFY: These lines set basic window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()


    def readFile(self):
        inputfile = open("pokedex.csv","r")
        s = inputfile.readline()
        s2 = s.split(",")
        dexIndex = s2.index("Dex")
        pokemonIndex = s2.index("Pokemon")
        catchrateIndex = s2.index("Catch Rate")
        speedIndex = s2.index("Speed\n")
        pokemonList = []
        s = inputfile.readline()
        s2 = s.split(",")
        while (s2 != ['']):
            p = Pokemon(s2[pokemonIndex],s2[dexIndex],s2[catchrateIndex],s2[speedIndex])
            pokemonList +=[p]
            s = inputfile.readline()
            s2 = s.split(",")
        inputfile.close()
        return pokemonList

    #read in the data file from pokedex.csv at some point here
    def getPokemonImage(self, pokemon):
        currentDex = str(int(pokemon.dex))
        return tk.PhotoImage(file ="sprites/" + currentDex + ".gif")

    def createWidgets(self):
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.balls) +" left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.grid(column =1, row = 1)

        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.grid(column =2, row = 1)
        # Throw Rock
        self.throwRockButton = tk.Button(self)
        self.throwRockButton["text"] = "Throw Rock"
        self.throwRockButton["command"] = self.throwRock
        self.throwRockButton.grid(column =1, row = 2)

        #Throw bait
        self.throwBaitButton = tk.Button(self)
        self.throwBaitButton["text"] = "Throw bait"
        self.throwBaitButton["command"] = self.throwBait
        self.throwBaitButton.grid(column =2, row = 2)

        #A label for status messages has been completed for you as an example:
        self.statusLabel = tk.Label(bg="grey")
        self.statusLabel["text"] = "You encountered a wild " + str(self.currentPokemon.specie)
        self.statusLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.
        self.pokemonImageLabel = tk.Label(bg="white")

        self.image = self.getPokemonImage(self.currentPokemon)
        self.pokemonImageLabel["image"] = self.image
        self.pokemonImageLabel.pack()

        #Complete and pack the catchRateLabel here.
        self.catchLabel = tk.Label(bg="grey")
        self.catchLabel["text"] = "You chance of catching it is " + str(math.floor(self.currentPokemon.probability * 100)) + "%"
        self.catchLabel.pack(fill="x", padx=5, pady=5)

        #Complete and pack the pokemonRunaway here.
        self.pokemonRunawayLabel = tk.Label(bg="grey")
        self.pokemonRunawayLabel["text"] = "Runaway chance of the pokemon is" + str(math.floor(self.currentRunawayRate * 100)) + "%"
        self.pokemonRunawayLabel.pack(fill="x", padx=5, pady=5)

    def nextPokemon(self):
        #reset all current variable
        self.isAngry = False
        self.isEating = False
        self.eatingRound = 0
        self.angryRound = 0
        self.currentPokemon = self.pokemonList[random.randint(0,len(self.pokemonList)-1)]
        self.currentCatchRate = int(self.currentPokemon.catchrate)
        self.currentPossibility = min((self.currentCatchRate+1), 151) / 449.5
        self.currentSpeed = int(self.currentPokemon.speed)
        self.currentRunawayRate = self.calculateRunawayRate()

        self.updateWidgets()

    def endAdventure(self):
        #TODO
        #print("You need to implement this and then remove this print statement")
        if len(self.pokemonCaught)== 0:
            pokemonCaughtinString = "Oops, you caught 0 pokemon"
        else:
            if len(self.pokemonCaught) == 1:
                pokemonCaughtinString = "You caught 1 pokemon \n"
            else:
                pokemonCaughtinString = "You caught " + str(len(self.pokemonCaught))+" pokemons \n"
            for i in self.pokemonCaught:
                pokemonCaughtinString += str(i.specie) + "\n"
        #remove label and button

        self.pokemonImageLabel.pack_forget()
        self.throwButton.grid_forget()
        self.runButton.grid_forget()
        self.throwRockButton.grid_forget()
        self.throwBaitButton.grid_forget()
        self.statusLabel.pack_forget()
        self.catchLabel.pack_forget()
        self.pokemonRunawayLabel.pack_forget()

        #show pokemoncaught
        self.endLabel = tk.Label(bg="grey")
        self.endLabel["text"] = "You're all out of balls, hope you had fun!"
        self.endLabel.pack(fill="x", padx=5, pady=5)

        #self.resultlabel = tk.Label()
        self.resultlabel = tk.Label(bg="grey", text = pokemonCaughtinString)
        self.resultlabel.pack(fill="x", padx=5, pady=5)

        #This method must:

            #display advengture completion message
            #list captured pokemon

        #hint: to remove a widget from the layout, you can call the pack_forget() method
            #for example, self.pokemonImageLabel.pack_forget() removes the pokemon image

    def updateWidgets(self):
        self.checkStatuslabel()         #check if angry or eating, modify the catch rate and possibility
        self.throwButton["text"] = "Throw Safari Ball (" + str(self.balls) +" left)"
        self.image = self.getPokemonImage(self.currentPokemon)
        self.pokemonImageLabel["image"] = self.image
        self.catchLabel["text"] = "You chance of catching it is " + str(math.floor(self.currentPossibility * 100)) + "%"
        self.pokemonRunawayLabel["text"] = "Runaway chance of the pokemon is" + str(math.floor(self.currentRunawayRate * 100)) + "%"
        #print("catch" + str(self.currentPokemon.probability))


    def checkStatuslabel(self):
        #print(str(self.angryRound) + "angryRound")
        if self.angryRound != 0:
            #print("angry" + str(self.angryRound))
            self.angryRound -=1
            self.statusLabel["text"] = "The wild " + str(self.currentPokemon.specie) +" is angry!"

        elif self.eatingRound != 0:
            #print("eating" + str(self.eatingRound))
            self.eatingRound -=1
            self.statusLabel["text"] = "The wild " + str(self.currentPokemon.specie) +" is eating!"

        #if elf.eatingRound == 0:

        else:
            self.statusLabel["text"] = "You encountered a wild " + str(self.currentPokemon.specie)



    def throwBall(self):
        #print("throwball")
        if self.balls > 0:
            self.balls -= 1
            self.updateWidgets()
            #return a random number in the range of 0.0 and 1.0
            catchProb = random.random()
            if catchProb <= self.currentPokemon.probability:
                self.pokemonCaught.append(self.currentPokemon)
                self.statusLabel["text"] = "You caught it!"
                self.nextPokemon()
            else:
                self.statusLabel["text"] = "Aargh! It escaped!"
                self.pokemonRunaway()
        else:
            self.endAdventure()

        #This method must:

            #decrement the number of balls remaining
            #check to see if endAdventure() should be called
            #otherwise, try to catch the pokemon

        #Don't forget to update the throwButton's text to reflect one less pokeball
        #Don't forget to call runAway to generate a new pokemon if this one is caught

    def throwRock(self):

        self.isAngry = True
        self.isEating = False

        self.angryRound = random.randint(1,5)
        self.eatingRound = 0

        self.currentCatchRate = self.currentCatchRate * 2
        if self.currentCatchRate >255:
            self.currentCatchRate = 255
        self.currentPossibility = min((self.currentCatchRate+1), 151) / 449.5


        self.currentRunawayRate = self.calculateRunawayRate()
        self.pokemonRunaway()
        self.updateWidgets()

    def throwBait(self):
        #print("throw bait")
        self.isAngry = False
        self.isEating = True

        self.eatingRound = random.randint(1,5)
        self.angryRound = 0
        self.currentCatchRate = self.currentCatchRate//2
        self.currentPossibility = min((self.currentCatchRate+1), 151) / 449.5


        self.currentRunawayRate = self.calculateRunawayRate()
        self.pokemonRunaway()
        self.updateWidgets()

    def pokemonRunaway(self):
        x = self.currentSpeed % 256
        x = x*2
        if x > 255:
            self.nextPokemon()
        else:
            if self.isAngry == True:    #If the Pokémon is angry, double X again (if it becomes greater than 255, make it 255 instead).
                x = x*2
                if x> 255:
                    x = 255
            if self.isEating == True:
                x = x//4
            r = random.randint(0,255)
            if r < x:
                self.nextPokemon()

    def calculateRunawayRate(self):
        RunawayRate = 2 * self.currentSpeed/256
        if self.isAngry:
            RunawayRate =  min(255, 4* self.currentSpeed)/256
        if self.isEating:
            RunawayRate =(self.currentSpeed/2)/256
        #print("runawayrate" + str(RunawayRate))
        return RunawayRate


#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
