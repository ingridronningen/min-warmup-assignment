from pathlib import Path
import sys

# Dette er start-koden til den første programmeringsoppgave i ING 301
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.

def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open

    with open(file_name, "r", encoding="utf-8") as f:     # åpner fil, leser (r), håndterer spesielle tegn
        lines = f.read().splitlines()                     # f.read = leser hele innholdet i filen som en lang tekststreng, .splitlines() = deler opp den lange strengen ved hvert linjeskift 
    return lines                                          # sender tilbake en liste 

def lines_to_words(lines):
    """
    Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
    og deler linjene opp i enkelte ord. Enhver linje blir delt opp der det er blanktegn (= whitespaces).
    Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
    kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.
    Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
    blir behandlet likt.
    OBS! Pass også på at du ikke legger til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

    F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
    """
    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig
    
    words = []                                      # oppretter en tom liste
    for line in lines:                              # går gjennom hver enkelt linje i teksten "lines"
        for word in line.split():                   # går gjennom hvert ord i "line" - .split() = deler hver setning i ett og ett ord
            word = word.lower().strip(".,:;?!")     # for hvert ord: .lower() = små bokstaver, .strip(".,:;?!") = fjerner tegnsettingen fra start og slutt av ord
            if word:                                # sjekker om ord eksisterer og det ikke bare er en tom streng: ""
                words.append(word)                  # legger til rene ord i listen "words"
            
    return words                                    # returnerer listen words

def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    frequency = {}                      # lager en dick {nøkkel:verdi}

    for word in words:                  # for alle ord i listen "words"
        if word in frequency:           # sjekker om ord allerede finnes i dick frequency
            frequency[word] += 1        # om ja: legger 1 i denne nøkkelen 
        else:                           # om nøkkelen ikke finnes allerede
            frequency[word] = 1         # legger set inn i ordboken med verdi 1

    return frequency                    # returnerer ordbok 


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']

def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    for word in FILL_WORDS:                 # for alle ord i teksten "Fill_words"
        if word in frequency_table:         # om disse ordene finnes i "frequency_table"
            del frequency_table[word]       # fjern ord fra frequency_table
    return frequency_table                  # returner frequency_table


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!

    if par_1[1] >= par_2[1]:        # om par_1 komponent 1 (altså tallet) er større eller lik par_2 komponent 1 (tall)
        return par_1                # returneres par_1
    else:                           # om ikke 
        return par_2                # returneres par_2


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    
    most_frequent = ("", -1)                                # lager en "dummy-variabel" som fungerer som en foreløbig beholder. Starter med tom tekststreng og tallet -1
    for pair in frequency_table.items():                    # for pair i dict - .items() = gjør om ordbot til en liste med par (tupler)
        most_frequent = largest_pair(most_frequent, pair)   # bruker kodene fra tidligere:
                                                                # largest_pair (nåværende beholder, nytt par) -> sjekker om hvem som er størst, og den legges inn i largest_pair

    return most_frequent[0]                                 # returnerer most_frequens som består av paret med høyest tall, siden vi bare skal ha ord ikke tall velger den posisjon [0] som ordet står i 


############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()